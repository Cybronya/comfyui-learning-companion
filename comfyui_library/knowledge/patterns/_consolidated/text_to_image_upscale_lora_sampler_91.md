---
name: text_to_image_upscale_lora_sampler_91
type: Text To Image
frequency: 3
level: strong
coverage: 0.957
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, Image Crop Face, Image Paste Face, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, LoraLoader, MaraScottTextConcatenate_v1, MaskToSEGS, ModelSamplingFlux, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SDXLAspectRatioSelector, SEGSPreview, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, Text _O, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageScaleDownToSize]
problems: []
missing: []
members: [图片生成/图生图/自然随手拍风格 全能图片G4o 同款_1920307960541544449.json, 图片生成/图生图/自然随手拍风格_1920316909131337730.json, 图片生成/图生图/😍全能图片G4o随手自拍的你🌻_1921024423321866241.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/自然随手拍风格 全能图片G4o 同款_1920307960541544449.json、图片生成/图生图/自然随手拍风格_1920316909131337730.json、图片生成/图生图/😍全能图片G4o随手自拍的你🌻_1921024423321866241.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `Image Crop Face`
- `Image Paste Face`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `MaraScottTextConcatenate_v1`
- `MaskToSEGS`
- `ModelSamplingFlux`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SDXLAspectRatioSelector`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `Text _O`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageScaleDownToSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 832 - 832 | 3 | 100% |
| 高度 | 1216 | 1216 - 1216 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 0.55 | 0.55 - 0.55 | 3 | 100% |
| LoRA 模型强度 | 0.9 | 0.9 - 0.9 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，观测区间 832 - 832，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，观测区间 1216 - 1216，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 0.55，观测区间 0.55 - 0.55，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，观测区间 0.9 - 0.9，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
