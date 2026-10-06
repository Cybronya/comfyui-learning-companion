# VOSR2ModelLoader

## 节点类型

`VOSR2ModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `model:COMBO`（23 次）
- `dtype:COMBO`（23 次）

## 输出

- `model:VOSR2_MODEL`（23 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["VOSR2", "fp16"]`（13 次）
- `["VOSR2", "default"]`（10 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
