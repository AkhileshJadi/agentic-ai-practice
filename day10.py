def build_incident_summary(ticket_id, priority, status):

    summary = f"Incident {ticket_id} is {priority} priority and is currently {status}."

    return summary


result = build_incident_summary("INC-101", "High", "Open")

print(result)