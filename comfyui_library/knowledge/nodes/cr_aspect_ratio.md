# CR Aspect Ratio

## 节点类型

`CR Aspect Ratio`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `width:INT`（3 次）
- `height:INT`（3 次）
- `aspect_ratio:COMBO`（3 次）
- `swap_dimensions:COMBO`（3 次）
- `upscale_factor:FLOAT`（3 次）
- `prescale_factor:FLOAT`（3 次）
- `batch_size:INT`（3 次）

## 输出

- `width:INT`（3 次）
- `height:INT`（3 次）
- `upscale_factor:FLOAT`（3 次）
- `prescale_factor:FLOAT`（3 次）
- `batch_size:INT`（3 次）
- `empty_latent:LATENT`（3 次）
- `show_help:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1536, 1536, "custom", "Off", 1, 1, 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
