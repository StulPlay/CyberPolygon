from django.http import JsonResponse
import vagrant

API_KEY = "314159265"

def check_api_key(request):
    api_key = request.GET.get("api_key")

    if not api_key or api_key != API_KEY:
        return False
    return True

def list_vms(request):
    if not check_api_key(request):
        return JsonResponse({"error": "Invalid API key"}, status=403)

    if request.method == 'GET':
        v = vagrant.Vagrant()

        vms_status = v.status()
        vms = []

        for vm in vms_status:
            vm_name = vm.name
            state = vm.state
            vms.append({"name": vm_name, "state": state})

        return JsonResponse(vms, safe=False)

    return JsonResponse({"error": "Only GET requests are allowed"}, status=405)

def manage_vm(request, action):
    if not check_api_key(request):
        return JsonResponse({"error": "Invalid API key"}, status=403)

    vm_name = request.GET.get('vm_name')

    if not vm_name:
        return JsonResponse({"error": "No VM name provided"}, status=400)

    try:
        v = vagrant.Vagrant()
        result = {}

        if action == "start":
            out = v.up(vm_name=vm_name, stream_output=True)
            for s in out:
                if "Flag:" in s:
                    flag = s[s.find("Flag:") + len("Flag: "):].strip()
                    result["Flag"] = flag  # Записываем флаг в результат
                if "Generated password for vagrant:" in s:
                    passw = s[s.rfind("Generated password for vagrant:") + len("Generated password for vagrant: "):].strip()
                    result["Password"] = passw  # Записываем пароль в результат

        elif action == "stop":
            v.halt(vm_name=vm_name)
            result["Stop"] = "OK."

        elif action == "delete":
            v.destroy(vm_name=vm_name)
            result["Delete"] = "OK."

        elif action == "reload":
            v.reload(vm_name=vm_name)
            result["Reload"] = "OK"

        else:
            return JsonResponse({"error": f"Unknown action: {action}"}, status=400)

        return JsonResponse(result)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
