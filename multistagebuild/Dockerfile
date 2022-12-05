FROM ubuntu AS compress-stage
WORKDIR /testfolder
COPY etc .
RUN tar zcvf etc-backup.tar.gz *

FROM ubuntu AS run-stage
WORKDIR /runtime
COPY --from=compress-stage /testfolder/etc-backup.tar.gz .
#ENTRYPOINT ["tar","tf","etc-backup.tar.gz"]
ENTRYPOINT ["cat","/dev/zero","/dev/null"]
