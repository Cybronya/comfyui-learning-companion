# workflow>krea2高清

## 节点类型

`workflow>krea2高清`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `configs:LIST`（1 次）
- `mask:MASK`（1 次）
- `pad_mode:COMBO`（1 次）
- `pad_color:COMBO`（1 次）
- `pad_color_rgb:STRING`（1 次）
- `pad_noise:FLOAT`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）

## 输出

- `遮罩:MASK`（1 次）
- `原始大小:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `config:ANY`（1 次）
- `CONDITIONING:CONDITIONING`（1 次）
- `ReferenceLatent CONDITIONING:CONDITIONING`（1 次）
- `mask:MASK`（1 次）
- `pad_info:ANY`（1 次）
- `Flux2KleinOutputExtractor_EditUtils pad_info:ANY`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_3_8b_fp8mixed.safetensors", "flux2", "default", "flux2-vae.safetensors", "", 43800613646712, "randomize", "euler"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
