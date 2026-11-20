---
name: image_to_image_sampler_clip_unet_66
type: Image To Image
frequency: 6
level: strong
coverage: 0.899
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/13种预设-Kontext_1945390387328634881.json, 图片生成/图生图/AI小兵哥-Kontext一句话改图工作流_1948010995596832769.json, 图片生成/图生图/FLUX.1Kontext.dev-单多图测试_1939156551691067393.json, 图片生成/图生图/Kontext&Lora_1940383341097152513.json, 图片生成/图生图/Kontext-Lora&ACE++_1940386151624765441.json, 图片生成/图生图/Kontext_HiDream结论&对比_1949809872876519426.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/13种预设-Kontext_1945390387328634881.json、图片生成/图生图/AI小兵哥-Kontext一句话改图工作流_1948010995596832769.json、图片生成/图生图/FLUX.1Kontext.dev-单多图测试_1939156551691067393.json、图片生成/图生图/Kontext&Lora_1940383341097152513.json、图片生成/图生图/Kontext-Lora&ACE++_1940386151624765441.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `RH_Translator` —— 5/6 个有
- `SDXLEmptyLatentSizePicker+` —— 5/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `LoadKontextPresets` —— 3/6 个有
- `KepStringLiteral` —— 2/6 个有
- `OllamaVision` —— 2/6 个有
- `RH_Captioner` —— 2/6 个有
- `ShowText` —— 2/6 个有
- `BasicScheduler` —— 1/6 个有
- `CFGNorm` —— 1/6 个有
- `DualCFGGuider` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `InstructPixToPixConditioning` —— 1/6 个有
- `JanusImageUnderstanding` —— 1/6 个有
- `JanusModelLoader` —— 1/6 个有
- `KSamplerSelect` —— 1/6 个有
- `QuadrupleCLIPLoader` —— 1/6 个有
- `RandomNoise` —— 1/6 个有
- `SamplerCustomAdvanced` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 768x1280 (0.6) | - | 5 | 80% |
| 高度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 最常用 768x1280 (0.6)，5 个样本，一致性 80%
- 高度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
