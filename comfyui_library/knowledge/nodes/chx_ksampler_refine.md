# chx_Ksampler_refine

## 节点类型

`chx_Ksampler_refine`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `context:RUN_CONTEXT`（1 次）
- `image:IMAGE`（1 次）

## 输出

- `context:RUN_CONTEXT`（1 次）
- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["RealESRGAN_x2plus.pth", "lanczos", 1, 143381945244397, "randomize", 0.3, "Preview", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
