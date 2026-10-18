# RunningHubRVCZipModelLoader

## 节点类型

`RunningHubRVCZipModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `zip_file:COMBO`（2 次）
- `device:COMBO`（2 次）
- `is_half:BOOLEAN`（2 次）

## 输出

- `rvc_model:RVC_MODEL`（2 次）
- `info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["05b88fdd2bbfdb5c99f8efd579e27626353457d5c7d263058222d179ac643237.zip", "auto", true, null]`（1 次）
- `["e31f4f79dfbd8a5787297d50bd4840a5eaf9ff9342924b58e07bbbfeadaf78ec.zip", "auto", true, null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
