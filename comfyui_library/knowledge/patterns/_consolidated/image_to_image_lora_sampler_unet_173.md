---
name: image_to_image_lora_sampler_unet_173
type: Image To Image
frequency: 3
level: strong
coverage: 0.96
common_nodes: [CLIPLoader, ImageResizeKJv2, ImageScaleBy, Int, KSampler, LoadImage, LoraLoaderModelOnly, RFInversion, SaveImage, UNETLoader, UnofficialExtensions, UntwistingRoPE, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit-2511-图像风格迁移_2065965901253537794.json, 图片生成/图生图/Qwen-image-2512-按风格生图像_2065616312424030209.json, 图片生成/图生图/【万物皆可转绘】Untwisting RoPE 免训练任意风格迁移 qwen_2070160171820732418.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_173

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-edit-2511-图像风格迁移_2065965901253537794.json、图片生成/图生图/Qwen-image-2512-按风格生图像_2065616312424030209.json、图片生成/图生图/【万物皆可转绘】Untwisting RoPE 免训练任意风格迁移 qwen_2070160171820732418.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RFInversion`
- `SaveImage`
- `UNETLoader`
- `UnofficialExtensions`
- `UntwistingRoPE`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `TextConcatenate` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 616 | - | 2 | 83% |
| 高度 | 896 | - | 2 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 616，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 896，样本不足，未给区间，2 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
