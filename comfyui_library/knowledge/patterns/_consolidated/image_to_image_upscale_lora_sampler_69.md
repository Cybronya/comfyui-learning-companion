---
name: image_to_image_upscale_lora_sampler_69
type: Image To Image
frequency: 3
level: strong
coverage: 0.825333
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/高清放大修复-2.0_8K_2087812199464132610.json, 图片生成/图生图/高清放大修复-2026年新版【真实细节】_2003273933614907393.json, 图片生成/图生图/👾怪獸-Qwen 2511-Unblur-Anything高清修复👾_2014653934102646786.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_69

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/高清放大修复-2.0_8K_2087812199464132610.json、图片生成/图生图/高清放大修复-2026年新版【真实细节】_2003273933614907393.json、图片生成/图生图/👾怪獸-Qwen 2511-Unblur-Anything高清修复👾_2014653934102646786.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `DownloadAndLoadFlorence2Model` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `Latent Noise Injection` —— 2/3 个有
- `ShowText` —— 2/3 个有
- `easy imageSizeBySide` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | kl_optimal | - | 3 | 67% |
| 重绘幅度 | 0.42 | 0.2 - 0.42 | 3 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 kl_optimal，3 个样本，一致性 67%
- 重绘幅度 中位数 0.42，观测区间 0.2 - 0.42，3 个样本
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
