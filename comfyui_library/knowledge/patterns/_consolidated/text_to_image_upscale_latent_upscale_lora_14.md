---
name: text_to_image_upscale_latent_upscale_lora_14
type: Text To Image
frequency: 3
level: weak
coverage: 0.778333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, ImageSmartSharpen+, JoinImageWithAlpha, KSampler, KSamplerAdvanced, LatentUpscaleBy, LoraLoaderModelOnly, PrimitiveFloat, ResizeImageMaskNode, ResolutionSelector, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SimpleMathDual+, SplitImageWithAlpha, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2新模型开源二采出图4种图片放大汇总工作流详拆_2100305559923806210.json, 图片生成/文生图/Krea2生图+SeedVR2-int8放大 (1)_2101836851886780417.json, 图片生成/文生图/💗Krea2新模型开源二采出图！4种图片放大汇总工作流详拆系列09集_2098393973126688769.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2新模型开源二采出图4种图片放大汇总工作流详拆_2100305559923806210.json、图片生成/文生图/Krea2生图+SeedVR2-int8放大 (1)_2101836851886780417.json、图片生成/文生图/💗Krea2新模型开源二采出图！4种图片放大汇总工作流详拆系列09集_2098393973126688769.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `ImageSmartSharpen+`
- `JoinImageWithAlpha`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SimpleMathDual+`
- `SplitImageWithAlpha`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_DLSS5Enhance` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `VOSR2ModelLoader` —— 2/3 个有
- `VOSR2Upscale` —— 2/3 个有
- `easy float` —— 2/3 个有
- `easy getNode` —— 2/3 个有
- `easy int` —— 2/3 个有
- `easy setNode` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `HAIGC_SaveImagesToZip` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 4 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |
| 宽度 | 1024 | 80 - 1024 | 3 | 37% |
| 高度 | 1024 | 80 - 1024 | 3 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 4，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- 宽度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
