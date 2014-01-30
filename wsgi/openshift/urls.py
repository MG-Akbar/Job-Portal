from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'article.views.home'),
    url(r'^signup/$', 'article.views.signup'),
    url(r'^register/$', 'article.views.register'),
    url(r'^error/$', 'article.views.error'),
    url(r'^login/$', 'article.views.login'),
    url(r'^signinerror/$', 'article.views.signinerror'),
    url(r'^logout/$', 'article.views.logout'),
    url(r'^profile/$', 'article.views.profile'),
    url(r'^profilec/$', 'article.views.profilec'),
    url(r'^rprofile/$', 'article.views.rprofile'),
    url(r'^rprofilec/$', 'article.views.rprofilec'),
    url(r'^edit_profile/$', 'article.views.editprofile'),
    url(r'^recruiter/$', 'article.views.recruiter'),
    url(r'^recruiters/$', 'article.views.recruiters'),
    url(r'^rregister/$', 'article.views.rregister'),
    url(r'^rerror/$', 'article.views.rerror'),
    url(r'^rlogin/$', 'article.views.rlogin'),
    url(r'^rsigninerror/$', 'article.views.rsigninerror'),
    url(r'^rlogout/$', 'article.views.rlogout'),
    url(r'^postjob/$', 'article.views.postjob'),
    url(r'^post_job/$', 'article.views.post_job'),
    url(r'^jobs/all/$', 'article.views.alljobs'),
    url(r'^jobs/get/(?P<articleid>\d+)/$','article.views.job'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^savechanges/$', 'article.views.savechanges'),
    url(r'^searchjob/$', 'article.views.searchjob'),
    url(r'^findjob/all/$', 'article.views.findjob'),
    url(r'^searchjobs/get/all/$', 'article.views.getsearchedjob'),
    url(r'^buyonline/$', 'article.views.buyonline'),
    url(r'^changepassword/$', 'article.views.change'),
    url(r'^processpassword/$', 'article.views.processpasswd'),
    url(r'^changepassword/incorrect/$', 'article.views.changeincorrect'),
    url(r'^changepasswordc/$', 'article.views.changec'),
    url(r'^processpassword/candidate/$', 'article.views.cprocesspasswd'),
    url(r'^changepasswordc/incorrect/$', 'article.views.changecincorrect'),
    url(r'^resumeservice/$', 'article.views.resumeservice'),
    url(r'^findresumes/$', 'article.views.findresumes'),
    url(r'^forgot/$', 'article.views.forgot'),
    url(r'^sendmail/$', 'article.views.sendmail'),
    url(r'^sendingsuccessfull/$', 'article.views.sendingsuccess'),
    url(r'^resetpassword/(?P<another>.*)/$', 'article.views.resetpassword'),
    url(r'^resettingpassword/$', 'article.views.resettingpassword'),
    url(r'^changedsuccessfull/$', 'article.views.changedsuccessfull'),
    url(r'^rforgot/$', 'article.views.rforgot'),
    url(r'^rsendmail/$', 'article.views.rsendmail'),
    url(r'^rsendingsuccessfull/$', 'article.views.rsendingsuccess'),
    url(r'^rresetpassword/(?P<another>.*)/$', 'article.views.rresetpassword'),
    url(r'^rresettingpassword/$', 'article.views.rresettingpassword'),
    url(r'^rchangedsuccessfull/$', 'article.views.rchangedsuccessfull'),
    url(r'^credit/$', 'article.views.credit'),
    url(r'^jobs/gets/(?P<articleid>\d+)/$', 'article.views.jobsearch'),
    url(r'^apply/(?P<articleid>\d+)/$', 'article.views.applied'),
    url(r'^appliedsuccessfully/$', 'article.views.applysuccess'),
    url(r'^(?P<another>.*)/$', 'article.views.unknown'),
)