# HiDreamSampler

## 节点类型

`HiDreamSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt:STRING`（2 次）

## 输出

- `image:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["fast", "A cat holding a sign \"lum3on\"", "880 × 1168 (Portrait)", 53197087, "fixed", 15, 0, 0, 0]`（1 次）
- `["fast", "", "880 × 1168 (Portrait)", 180898495, "randomize", 16, 0, 0, 0]`（1 次）
- `["fast", "", "1024 × 1024 (Square)", 45850005, "randomize", -1, -1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
