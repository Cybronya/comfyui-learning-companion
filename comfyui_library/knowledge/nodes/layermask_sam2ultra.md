# LayerMask: SAM2Ultra

## 节点类型

`LayerMask: SAM2Ultra`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `bboxes:BBOXES`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sam2_hiera_base_plus.safetensors", "fp16", "all", "0,", false, "VITMatte", 6, 4, 0.15, 0.99, true, "cuda", 2]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
