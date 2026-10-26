---
name: text_to_image_upscale_sampler_clip_29
type: Text To Image
frequency: 3
level: weak
coverage: 0.867
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageSharpen, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2 洗图+放大_2036703228607340546.json, 图片生成/文生图/Krea2双采+Klein一次放大加细节+seedvr二次放大，高清化极致观感_2073725632059625473.json, 图片生成/文生图/Z Image极致人体文生图16_9横幅｜编号187和123精选款_2111294102447935489.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux2 洗图+放大_2036703228607340546.json、图片生成/文生图/Krea2双采+Klein一次放大加细节+seedvr二次放大，高清化极致观感_2073725632059625473.json、图片生成/文生图/Z Image极致人体文生图16_9横幅｜编号187和123精选款_2111294102447935489.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `Float` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `StringReplace` —— 1/3 个有
- `YC Color Match` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1920 | 3 | 25% |
| 高度 | 1024 | 80 - 1080 | 3 | 37% |
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 5 | 4 - 10 | 3 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | euler | - | 3 | 33% |
| 调度器 | simple | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1920，3 个样本，取值分散，一致性仅 25%
- 高度 中位数 1024，观测区间 80 - 1080，3 个样本，取值分散，一致性仅 37%
- 采样步数 中位数 5，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
