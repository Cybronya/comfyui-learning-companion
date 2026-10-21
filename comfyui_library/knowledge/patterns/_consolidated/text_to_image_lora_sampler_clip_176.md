---
name: text_to_image_lora_sampler_clip_176
type: Text To Image
frequency: 7
level: weak
coverage: 0.887
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json, 图片生成/文生图/全新工作流！动漫生图+风格转绘二合一！_2058011143603576833.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108431762991964161.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108886341202300929.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108891627866640386.json, 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109018096492175361.json, 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_176

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json、图片生成/文生图/全新工作流！动漫生图+风格转绘二合一！_2058011143603576833.json、数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108431762991964161.json、数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108886341202300929.json、数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108891627866640386.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageSharpen` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PreviewAny` —— 5/7 个有
- `QwenImagePromptOptimizer` —— 5/7 个有
- `QwenImagePromptStyler` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `solarL_SaveImagesToZip` —— 2/7 个有
- `孤海注释` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `DrawMaskOnImage` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `JoinStringMulti` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1344 | 80 - 2048 | 7 | 30% |
| 高度 | 1280 | 80 - 2048 | 7 | 30% |
| 采样步数 | 30 | 4 - 40 | 7 | 45% |
| Prompt 约束强度(CFG) | 2 | 1 - 5 | 7 | 50% |
| 采样算法 | er_sde | - | 7 | 43% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1344，观测区间 80 - 2048，7 个样本，取值分散，一致性仅 30%
- 高度 中位数 1280，观测区间 80 - 2048，7 个样本，取值分散，一致性仅 30%
- 采样步数 中位数 30，观测区间 4 - 40，7 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 43%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
