Simple application to test tcp connections periodically from a cloud foundry application to somethign else.

Edit manifest.yml and adjust the applicationn name, and the env.testhosts and env.testports for your needs and then:

    cf push

results are written to the log.

    cf log tcptest

to see results of connection attempts every 5 seconds.


