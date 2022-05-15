
Windows Event Log fields, that present in every log:

```yml
fields:

  - original_name: ProviderName
    description: The source of the event log record (the application or service that logged the record).
    sample_value: 'Microsoft-Windows-Security-Auditing'
    elastic_ecs_name: winlog.provider_name
    splunk_cim_name: N/A
    otr_ossem_name: event_type

  - original_name: ProviderGuid
    description: A globally unique identifier that identifies the provider that logged the event.
    sample_value: '{54849625-5478-4994-A5BA-3E3B0328C30D}'
    elastic_ecs_name: winlog.provider_guid
    splunk_cim_name: N/A
    otr_ossem_name: N/A

  - original_name: EventID
    description: The event identifier. The value is specific to the source of the event.
    sample_value: '4688'
    elastic_ecs_name: winlog.event_id
    splunk_cim_name: EventCode
    otr_ossem_name: event_id

  - original_name: Version
    description: The version number of the event’s definition.
    sample_value: '0'
    elastic_ecs_name: winlog.version
    splunk_cim_name: N/A
    otr_ossem_name: N/A

  - original_name: Level
    description: The version number of the event’s definition.
    sample_value: '2'
    elastic_ecs_name: winlog.event_data.SeverityValue
    splunk_cim_name: N/A
    otr_ossem_name: N/A

  - original_name: Task
    description: >
      The task defined in the event. Task and opcode are typically used to identify the location in the 
      application from where the event was logged.
    sample_value: '13312'
    elastic_ecs_name: winlog.Task
    splunk_cim_name: N/A
    otr_ossem_name: N/A

  - original_name: Opcode
    description: >
      The opcode defined in the event. Task and opcode are typically used to identify the 
      location in the application from where the event was logged.
    sample_value: '0'
    elastic_ecs_name: winlog.opcode
    splunk_cim_name: OpCode
    otr_ossem_name: N/A

  - original_name: Keywords
    description: >
      The keywords are used to classify an event. It is a 64-bit mask, every bit of each may represent a keyword. 
      2 bits of this mask represent Audit Success and Audit Failure events.
    sample_value: '0x8020000000000000'
    elastic_ecs_name: winlog.keywords
    splunk_cim_name: action
    otr_ossem_name: N/A

  - original_name: TimeCreated
    description: The system time of when the event was logged.
    sample_value: '2015-11-12T02:24:52.377352500Z'
    elastic_ecs_name: process.start
    splunk_cim_name: timestamp
    otr_ossem_name: event_creation_time

  - original_name: EventRecordID
    description: >
      The record ID of the event log record. The first record written to an event log is record number 1, 
      and other records are numbered sequentially. If the record number reaches the maximum value (2^32 for 
      the Event Logging API and 2^64 for the Windows Event Log API), the next record number will be 0.
    sample_value: '2814'
    elastic_ecs_name: winlog.record_id
    splunk_cim_name: RecordNumber
    otr_ossem_name: N/A

  - original_name: ExecutionProcessID
    description: The the Client Server Runtime Process (csrss.exe) process ID.
    sample_value: '4'
    elastic_ecs_name: winlog.process.pid
    splunk_cim_name: N/A
    otr_ossem_name: N/A

  - original_name: ExecutionThreadID
    description: The Client Server Runtime Process (csrss.exe) thread ID.
    sample_value: '400'
    elastic_ecs_name: winlog.process.thread.id
    splunk_cim_name: N/A
    otr_ossem_name: N/A

  - original_name: Channel
    description: >
      The name of the channel from which this record was read. This value is 
      one of the names from the event_logs collection in the configuration.
    sample_value: 'Security'
    elastic_ecs_name: winlog.channel
    splunk_cim_name: sourcetype
    otr_ossem_name: event_sub_type

  - original_name: Computer
    description: >
      'The name of the computer that generated the record. When using Windows 
      event forwarding, this name can differ from `agent.hostname`.'
    sample_value: 'WIN-GG82ULGC9GO.contoso.local'
    elastic_ecs_name: winlog.computer_name
    splunk_cim_name: ComputerName
    otr_ossem_name: computer_name
```