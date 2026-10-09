# T8_BreezeTTS_ModelLoader

## 节点类型

`T8_BreezeTTS_ModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `dtype:COMBO`（2 次）
- `device:COMBO`（2 次）
- `attention:COMBO`（2 次）
- `download_if_missing:BOOLEAN`（2 次）
- `accept_model_license:BOOLEAN`（2 次）

## 输出

- `model:BREEZE_T8_MODEL`（2 次）
- `model_info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "auto", "auto", true, true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
