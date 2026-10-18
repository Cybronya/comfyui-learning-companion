# AceMusicModelLoader

## 节点类型

`AceMusicModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `device:COMBO`（4 次）
- `cpu_offload:BOOLEAN`（4 次）
- `torch_compile:BOOLEAN`（4 次）
- `overlapped_decode:BOOLEAN`（4 次）

## 输出

- `model:ACEMUSIC_MODEL`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["cuda", false, false, false]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
