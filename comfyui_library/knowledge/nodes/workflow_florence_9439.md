# workflow/Florence

## 节点类型

`workflow/Florence`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `lora:PEFTLORA`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `caption:STRING`（1 次）
- `data:JSON`（1 次）
- `LATENT:LATENT`（1 次）
- `GrowMaskWithBlur mask:MASK`（1 次）
- `mask_inverted:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Florence-2-large", "fp16", "sdpa", "", "more_detailed_caption", true, false, 1024, 3, true, "", 1062473130068520, "ran`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
