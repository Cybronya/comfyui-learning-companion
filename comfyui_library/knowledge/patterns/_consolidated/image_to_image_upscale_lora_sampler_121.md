---
name: image_to_image_upscale_lora_sampler_121
type: Image To Image
frequency: 2
level: weak
coverage: 0.866
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, ImageScaleToMegapixels, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, ModelSamplingSD3, PreviewImage, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, Text, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SRPO+Wan2.2优化 （文生图，图生图，双模式）_1967898753619361793.json, 视频生成/文生视频/flux+SRPO+Wan2.2=极致美学+绝对细节_1967060110050725889.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_121

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/SRPO+Wan2.2优化 （文生图，图生图，双模式）_1967898753619361793.json、视频生成/文生视频/flux+SRPO+Wan2.2=极致美学+绝对细节_1967060110050725889.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ImageScaleToMegapixels`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `ModelSamplingSD3`
- `PreviewImage`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `Text`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BetterFilmGrain` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.075 | - | 2 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.075，样本不足，未给区间，2 个样本
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
