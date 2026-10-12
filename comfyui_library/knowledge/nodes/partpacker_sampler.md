# PartPacker_Sampler

## 节点类型

`PartPacker_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:PartPacker_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 输出

- `model_path:STRING`（2 次）
- `mesh:MESH`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[100000, 384, 704219931, "randomize", 50, 7, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
