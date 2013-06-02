# -*- coding: utf-8 -*-
from annoying.decorators import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from servers.models import ScanTask, Server


@login_required
def scans(request, server_id):
    server = Server.objects.get_by_user_and_server(request.user, server_id)
    if not server:
        return redirect('dashboard:servers')
    if request.method == 'POST':
        scan_task = ScanTask(user=request.user, server=server)
        scan_task.save()
        return redirect('servers:scan', server_id=server.pk, scan_id=scan_task.pk)

    scans = ScanTask.objects.get_by_server(server)
    ctx = {
        'scans': scans,
        'server': server,
    }
    return render(request, 'servers/scans.html', ctx)

@login_required
def scan(request, server_id, scan_id):
    server = Server.objects.get_by_user_and_server(request.user, server_id)
    if not server:
        return redirect('dashboard:servers')
    scan_task = ScanTask.objects.get_by_id(scan_id)
    if not scan_task or scan_task.user != request.user:
        return redirect('servers:scans', server_id=server.pk)
    ctx = {
        'scan': scan_task,
        'server': server,
    }
    if request.is_ajax():
        return JsonResponse({'stdout_colored': scan_task.stdout_colored})
    else:
        return render(request, 'servers/scan.html', ctx)


@login_required
def server(request, server_id):
    server = Server.objects.get_by_user_and_server(request.user, server_id)
    if not server:
        return redirect('dashboard:servers')
    scans = ScanTask.objects.get_by_server(server)
    ctx = {
        'scans': scans,
        'server': server,
    }
    return render(request, 'servers/server.html', ctx)

@login_required
def servers(request):
    servers = Server.objects.get_by_user(request.user)
    ctx = {'servers': list(servers)}
    return render(request, 'servers/servers.html', ctx)