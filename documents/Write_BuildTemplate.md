# 编写构建模板

标准版本:v1-250205

## 字段

### 示例

```json
{
    "name": "ProjectNevada.build.debug",
    "standardVer": "v1-250205",
    "package": "com.cora.wear.todo.next",
    "designWidths":[
        336,
        192,
        432,
        466
    ],
    "type": "debug",
    "versioncodeUpdateRule": "+=1",
    "props": [
        "--enable-jsc",
        "--enable-custom-component",
        "--enable-protobuf"
    ],
    "buildinfoContent":{
        "buildTime": "%Y-%m-%d %H:%M:%S",
        "builder": "$systemuser",
        "buildTemplate": "$current_template"
    },
    "AppOption": {
        "AppStartUpMode": 0
    }
}
```

### name

编译模板的名称

引用:$current_template

### standardVer

编译模板标准版本

已发布版本:

* v1-250205

### package

VelaApp包名

引用:$package

### designWidths

App编译的DesignWidth.

支持多个designWidth, 以数组形式存储

### type

编译类型, debug对应命令aiot build, release对应aiot release

### versioncodeUpdateRule

manifest.json中versionCode字段的更新规则, 默认为不更新(+=0)

格式: "+=[递增大小]"

### props

编译时在主命令aiot build/release后添加的参数, 以数组形式存储

### buildInfoContent

编译信息, 将写入app src目录下的common/buildinfo.js中

#### buildTime

编译时间, 根据python模块datetime支持的格式填写

| 符号 | 对应值 |
| ---- | ------ |
| %Y   | 年     |
| %m   | 月     |
| %d   | 日     |
| %H   | 小时   |
| %M   | 分钟   |
| %S   | 秒     |

#### builder

编译者(默认为空)

支持的变量:

* $systemuser (系统用户名)

#### buildTemplate

编译模板名称, 默认为$current_template

### AppOption

应用选项, 将存储至src目录下的quickbuilder.app.option.js

内容由开发者自行填写, 为一个Object, 将在正式编译前由QuickBuilder转译为JS并存储至上述目录. Object中的Value类型支持string与int
