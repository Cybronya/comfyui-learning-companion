---
name: unknown_workflow_lora_sampler_clip_156
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8755
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerAdvanced, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, Label (rgthree), LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/krea2+flux2 klein三采极致生图流_2075854570143703041.json, 图片生成/文生图/krea2+flux2 klein三采极致生图流（MUSE艺术版）_2050784159613898754.json, 图片生成/文生图/krea2+flux2 klein三采极致生图流（红潮艺术版）_2073728023936983042.json, 图片生成/文生图/krea2turbo 基础工作流+LORA+KLINE放大_2080283253579272193.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_156

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/krea2+flux2 klein三采极致生图流_2075854570143703041.json、图片生成/文生图/krea2+flux2 klein三采极致生图流（MUSE艺术版）_2050784159613898754.json、图片生成/文生图/krea2+flux2 klein三采极致生图流（红潮艺术版）_2073728023936983042.json、图片生成/文生图/krea2turbo 基础工作流+LORA+KLINE放大_2080283253579272193.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `ConditioningKrea2Rebalance` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `Int` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `TTP_Image_Assy` —— 3/4 个有
- `TTP_Image_Tile_Batch` —— 3/4 个有
- `TTP_Tile_image_size` —— 3/4 个有
- `easy imageSize` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `easy promptList` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Seed Generator` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 8 | 4 | 49% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 50% |
| 重绘幅度 | simple | - | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1024 - 1536 | 4 | 84% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 8，4 个样本，取值分散，一致性仅 49%
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 50%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1024 - 1536，4 个样本，取值集中（一致性 84%）
