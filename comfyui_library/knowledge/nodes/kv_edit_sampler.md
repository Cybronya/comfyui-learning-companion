# KV_Edit_Sampler

## 节点类型

`KV_Edit_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL_KVEDIT`（1 次）
- `condition:CONDITION_KV`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[330777409, "randomize", 28, 1.5, 28, 3.5, 1, 1, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
