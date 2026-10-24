# workflow>面部参考

## 节点类型

`workflow>面部参考`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `图像:IMAGE`（5 次）
- `attn_mask:MASK`（5 次）
- `options:OPTIONS`（5 次）
- `model:MODEL`（3 次）
- `LoRA:PEFTLORA`（2 次）
- `ApplyPulidFlux model:MODEL`（2 次）
- `image:IMAGE`（2 次）

## 输出

- `遮罩:MASK`（3 次）
- `model:MODEL`（3 次）
- `图像:IMAGE`（2 次）
- `caption:STRING`（2 次）
- `json数据:JSON`（2 次）
- `Seg:SEGS`（2 次）
- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["CUDA", "pulid_flux_v0.9.0.safetensors", true, false, false, false, false, false, 0.4, "VITMatte", 6, 6, 0.01, 0.99, tr`（3 次）
- `["Florence-2-large", "fp16", "sdpa", "CUDA", "pulid_flux_v0.9.1.safetensors", "head", "caption_to_phrase_grounding", tru`（1 次）
- `["Florence-2-large", "fp16", "sdpa", "CUDA", "pulid_flux_v0.9.1.safetensors", "head", "caption_to_phrase_grounding", tru`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
