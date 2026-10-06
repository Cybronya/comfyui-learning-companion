# SeCModelLoader

## 节点类型

`SeCModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model_file:COMBO`（5 次）
- `device:COMBO`（5 次）
- `use_flash_attn:BOOLEAN`（5 次）
- `allow_mask_overlap:BOOLEAN`（5 次）

## 输出

- `model:SEC_MODEL`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bfloat16", "auto", true, true]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
