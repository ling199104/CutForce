# CutForce
前置: 用pipenv安裝相依套件

```
!pip install pipenv
!pipenv shell
!pipenv install
```

採M(V)C - RESTful 架構，前後端分離的API Server
##基本業務分布
###帳號系統
```
controllers
└ _UserLogin.py
└ _UserLogout.py
└ _UserSignUp.py

models
└ _UserTable.py
└ _ApplyFileTable.py
└ _TokenTable.py
```
###上傳檔案
```
controllers
└ UploadVideoFile.py
```
###分析音軌
```
controllers
└ SilencePrediction.py

models
└ FFmpegConcatenation.py
```
###下載影片
```
controllers
└ DownloadVideoFile.py

models
└ FFmpegConcatenation.py 
```
###下載Xml
```
controllers
└ DownloadXmlFile.py

models
└ GetVideoInfo.py
└ XmlExtraction.py
```