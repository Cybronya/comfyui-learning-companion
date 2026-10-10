# ADE_AnimateDiffCombine

## 节点类型

`ADE_AnimateDiffCombine`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `frame_rate:INT`（2 次）
- `loop_count:INT`（2 次）
- `filename_prefix:STRING`（2 次）
- `format:COMBO`（2 次）
- `pingpong:BOOLEAN`（2 次）
- `save_image:BOOLEAN`（2 次）
- `deprecation_warning:ADEWARN`（2 次）

## 输出

- `GIF:GIF`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, 0, "Upscale", "image/gif", false, true, "", "/view?filename=Upscale_00001_egpzk_1767684286.gif&subfolder=&type=outpu`（1 次）
- `[8, 0, "AnimateDiff", "image/gif", false, true, "", "/view?filename=AnimateDiff_00001_nfaae_1767684234.gif&subfolder=&ty`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
