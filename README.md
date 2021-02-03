# truckxassignment
for this assignment I have used django rest framework for building API 
which is MTV base framework 
I have just covered two admin functions which are displaying all alarms of dashcam, and all alarms of dashcam with filters.
   all data models created and their use:- 1)alarm_types (use to store all type of different type of alarm ) this helps in reducing data redundancy.
2)alarmtable ( to save all alarm related details of dashcam)
3)file_list (save list of files name ) we can join with alarmtable using join operator.
 then serializer convert sqlite datamodels to json formate 
 Alarmserializer convert list of alarmtable data model to json formate but while converting it also add's addition information about alarm_type by foreign key and also helps in deserializing models
 API alarmList takes two parameter request and imei NO to identify dashcamp with help of imei we query all alarm of that dashmap from alarmtable then serialized it and send to admin.
 in alarmWithFilter with help of filters we filter on timestamp in given range along with type of alarm remaining if same as alarmlist API
 in alarmcreate we get data from dashcamp this is put request in this we save data in sqlite database. URL file is not uploaded which just map APIS to some url
