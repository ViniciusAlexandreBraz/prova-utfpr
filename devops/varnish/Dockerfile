# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Plone Foundation <collective@plone.org>" \
      org.label-schema.name="prova-utfpr-varnish" \
      org.label-schema.description="prova-utfpr Varnish image." \
      org.label-schema.vendor="Plone Foundation"

COPY etc/varnish.vcl /etc/varnish/default.vcl
