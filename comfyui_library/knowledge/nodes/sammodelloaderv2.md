# SamModelLoaderV2

## 节点类型

`SamModelLoaderV2`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_file:COMBO`（1 次）
- `use_cache:BOOLEAN`（1 次）

## 输出

- `model:SAM_MODEL`（1 次）
- `model_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sam_vit_h_4b8939.pth", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
