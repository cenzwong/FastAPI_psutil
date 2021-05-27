# uvicorn main:app --reload --host 0.0.0.0

from typing import Optional

from fastapi import FastAPI
import importlib

from enum import Enum

class enumPsutilCPU(str, Enum):
    cpu_times = "cpu_times"
    cpu_percent = "cpu_percent"
    cpu_times_percent = "cpu_times_percent"
    cpu_count = "cpu_count"
    cpu_stats = "cpu_stats"
    cpu_freq = "cpu_freq"
    getloadavg = "getloadavg"

class enumPsutilMemory(str, Enum):
    virtual_memory = "virtual_memory"
    swap_memory = "swap_memory"

class enumPsutilDisks(str, Enum):
    disk_partitions = "disk_partitions"
    disk_usage = "disk_usage"
    disk_io_counters = "disk_io_counters"

class enumPsutilNetwork(str, Enum):
    net_io_counters = "net_io_counters"
    net_connections = "net_connections"
    net_if_addrs = "net_if_addrs"
    net_if_stats = "net_if_stats"

class enumPsutilSensors(str, Enum):
    sensors_temperatures = "sensors_temperatures"
    sensors_fans = "sensors_fans"
    sensors_battery = "sensors_battery"

class enumPsutilSysInfo(str, Enum):
    boot_time = "boot_time"
    boot_strftime = "boot_strftime"
    users = "users"

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/built-in/psutil/CPU/{_func}")
def psutil_cpu(_func: enumPsutilCPU, 
            percpu: Optional[bool] = None, 
            interval: Optional[int] = None,
            logical: Optional[bool] = None,
            ):
    psutil = importlib.import_module('psutil')

    q = {
        "percpu": None,
        "interval": None,
        "logical": None
    }

    if _func == enumPsutilCPU.cpu_times:
        q["percpu"] = percpu if percpu != None else False
        if q["percpu"] == False:
            return psutil.cpu_times(percpu = q["percpu"])._asdict()
        elif q["percpu"] == True:
            return list_obj2return(psutil.cpu_times(percpu = q["percpu"]))
    elif _func == enumPsutilCPU.cpu_percent:
        q["interval"] = interval if interval != None else None
        q["percpu"] = percpu if percpu != None else False
        return psutil.cpu_percent(interval = q["interval"], percpu = q["percpu"])
    elif _func == enumPsutilCPU.cpu_times_percent:
        q["interval"] = interval if interval != None else None
        q["percpu"] = percpu if percpu != None else False
        if q["percpu"] == False:
            return psutil.cpu_times_percent(interval = q["interval"], percpu = q["percpu"])._asdict()
        elif q["percpu"] == True:
            return list_obj2return(psutil.cpu_times_percent(interval = q["interval"], percpu = q["percpu"]))
    elif _func == enumPsutilCPU.cpu_count:
        q["logical"] = logical if logical != None else True
        return psutil.cpu_count(logical = q["logical"])     
    elif _func == enumPsutilCPU.cpu_stats:
        return psutil.cpu_stats()._asdict()  
    elif _func == enumPsutilCPU.cpu_freq:
        q["percpu"] = percpu if percpu != None else False
        if q["percpu"] == False:
            return psutil.cpu_freq(percpu = q["percpu"])._asdict()
        elif q["percpu"] == True:
            return list_obj2return(psutil.cpu_freq(percpu = q["percpu"]))
    elif _func == enumPsutilCPU.getloadavg:
        return psutil.getloadavg()  
    else:
        return "Wrong input"

# Memory
@app.get("/api/built-in/psutil/Memory/{_func}")
def psutil_memory(_func: enumPsutilMemory):
    psutil = importlib.import_module('psutil')

    if _func == enumPsutilMemory.virtual_memory:
        return psutil.virtual_memory()._asdict()
    elif _func == enumPsutilMemory.swap_memory:
        return psutil.swap_memory()._asdict()
    else:
        return "Wrong input"

# Disks
@app.get("/api/built-in/psutil/Disks/{_func}")
def psutil_disks(_func: enumPsutilDisks, 
                    all: Optional[bool] = None, 
                    path: Optional[str] = None, 
                    perdisk: Optional[bool] = None,
                    nowrap: Optional[bool] = None):
    psutil = importlib.import_module('psutil')
    q = {
        "all": None,
        "path": None,
        "perdisk": None,
        "nowrap": None
    }
    if _func == enumPsutilDisks.disk_partitions:
        q["all"] = all if all != None else False
        return list_obj2return(psutil.disk_partitions(all = q["all"]))
    elif _func == enumPsutilDisks.disk_usage:
        q["path"] = path if path != None else "/"
        return psutil.disk_usage(q["path"])._asdict()
    elif _func == enumPsutilDisks.disk_io_counters:
        q["perdisk"] = perdisk if perdisk != None else False
        q["nowrap"] = nowrap if nowrap != None else True
        if q["perdisk"] == False:
            return psutil.disk_io_counters(perdisk = q["perdisk"], nowrap = q["nowrap"])._asdict()
        elif q["perdisk"] == True:
            return dict_obj2return(psutil.disk_io_counters(perdisk = q["perdisk"], nowrap = q["nowrap"]))
    else:
        return "Wrong input"

# Network
@app.get("/api/built-in/psutil/Network/{_func}")
def psutil_network(_func: enumPsutilNetwork, 
                    pernic: Optional[bool] = None,
                    nowrap: Optional[bool] = None,
                    kind: Optional[str] = None):
    psutil = importlib.import_module('psutil')
    q = {
        "pernic": None,
        "nowrap": None,
        "kind": None
    }

    if _func == enumPsutilNetwork.net_io_counters:
        q["pernic"] = pernic if pernic != None else False
        q["nowrap"] = nowrap if nowrap != None else True

        if q["pernic"] == False:
            return psutil.net_io_counters(pernic = q["pernic"], nowrap = q["nowrap"])._asdict()
        elif q["pernic"] == True:
            return dict_obj2return(psutil.net_io_counters(pernic = q["pernic"], nowrap = q["nowrap"]))
        return 
    elif _func == enumPsutilNetwork.net_connections:
        q["kind"] = kind if kind != None else "inet"
        return list_obj2return(psutil.net_connections(kind = q["kind"]))
    elif _func == enumPsutilNetwork.net_if_addrs:
        return dict_list_obj2return(psutil.net_if_addrs())
    elif _func == enumPsutilNetwork.net_if_stats:
        return dict_obj2return(psutil.net_if_stats())       
    else:
        return "Wrong input"

# Sensors
@app.get("/api/built-in/psutil/Sensors/{_func}")
def psutil_sensors(_func: enumPsutilSensors, 
                    fahrenheit: Optional[bool] = False
                    ):
    psutil = importlib.import_module('psutil')
    q = {
        "fahrenheit": None
    }

    if _func == enumPsutilSensors.sensors_temperatures:
        q["fahrenheit"] = fahrenheit if fahrenheit != None else False
        return dict_list_obj2return(psutil.sensors_temperatures(fahrenheit = q["fahrenheit"]))
    elif _func == enumPsutilSensors.sensors_fans:
        return dict_list_obj2return(psutil.sensors_fans())
    elif _func == enumPsutilSensors.sensors_battery:
        ps = psutil.sensors_battery()
        if ps == None:
            return {}
        else:
            return obj2return(ps)
    else:
        return "Wrong input"

# Other system info
@app.get("/api/built-in/psutil/OtherSysInfo/{_func}")
def psutil_sensors(_func: enumPsutilSysInfo ):
    psutil = importlib.import_module('psutil')

    if _func == enumPsutilSysInfo.boot_time:
        return psutil.boot_time()
    elif _func == enumPsutilSysInfo.boot_strftime:
        datetime = importlib.import_module('datetime')
        return datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    elif _func == enumPsutilSysInfo.users:
        return list_obj2return(psutil.users())
    else:
        return "Wrong input"

def obj2return(ps):
    return ps._asdict()

def list_obj2return(ps):
    return [i._asdict() for i in ps]

def dict_list_obj2return(ps):
    for key, value in ps.items():
        ps[key] = [i._asdict() for i in value]
    return ps

def dict_obj2return(ps):
    for key, value in ps.items():
        ps[key] = value._asdict()
    return ps   
