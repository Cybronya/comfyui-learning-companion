# workflow>右下图

## 节点类型

`workflow>右下图`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `prompt:STRING`（1 次）

## 输出

- `遮罩:MASK`（1 次）
- `原始大小:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["clip_l.safetensors", "t5xxl_fp8_e4m3fn.safetensors", "flux", "default", "ae.safetensors", "flux1-dev-kontext_fp8_scale`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
