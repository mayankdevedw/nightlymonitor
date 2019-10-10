# Nightly Monitoring Bot
(Owners: Asif & Mayank)


## Plan:
- Run the Bot parallel, may be cron job or along with every L2 run
- Check the following for each run items:
    - Resource Allocation
    - Deployment Failure (60% Threshold)
- Actions:
    - Re-Launch
        - Res Aloc: Direct for DC
        - Res Aloc: RR for AWS Account full
            - Use the Terminator Script, what will be passed = GTN
        - Dep Failure: Below threshold 
    - Match the Failed Stack Trace with History + Jira
    - Send mail
        - For Dep Failure: Above threshold
        - Duplicate Failure reasons
        - Suggested Jira(s) in mail++
    - Relaunch limit: 2
- One Shared Object to keep the stats (1 Thread to Monitor)
- Multiple threads to start the component item/GTN status and report to shared object
    - Failed GTN & Completed GTN not to add in the Queue
    - Blocking Queue we have to use for thread safe
    - Check every 5/10min, First 1hr of run
    - Check till all are failed/completed or when Action is triggered
- Ability to turn off the monitoring



## Implement:
- Phase 1: Check failed & Re-Launch
- Phase 2: Comparing Log & Suggesting
- Phase 3: Quasar CLI integration


I/p: Read the GTNs from the Quanta URL



