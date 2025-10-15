class AutoRestartMonitor:
    def should_restart(self, last_heartbeat_sec: int) -> bool:
        return last_heartbeat_sec > 60
