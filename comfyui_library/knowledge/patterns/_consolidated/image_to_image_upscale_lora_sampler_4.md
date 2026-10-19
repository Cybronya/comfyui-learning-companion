---
name: image_to_image_upscale_lora_sampler_4
type: Image To Image
frequency: 3
level: weak
coverage: 0.525667
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, SaveImage, Seed (rgthree), SimpleMath+, UltimateSDUpscale, UnetLoaderGGUF, Upscale Model Loader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [SimpleMath+, easy cleanGpuUsed, CR SDXL Aspect Ratio, Seed (rgthree), Upscale Model Loader, CR Text, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1970812659094482946.json, 图片生成/文生图/1971577017105838081.json, 图片生成/文生图/1971835496915791873.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1970812659094482946.json、图片生成/文生图/1971577017105838081.json、图片生成/文生图/1971835496915791873.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMath+`
- `UltimateSDUpscale`
- `UnetLoaderGGUF`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `CLIPLoader` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 3 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 0.4 | 0.1 - 1 | 3 | 25% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 0.4，观测区间 0.1 - 1，3 个样本，取值分散，一致性仅 25%
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+、easy cleanGpuUsed、CR SDXL Aspect Ratio、Seed (rgthree)、Upscale Model Loader
