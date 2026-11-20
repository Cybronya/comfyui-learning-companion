---
name: unknown_workflow_lora_sampler_clip_91
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.886143
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/krea2+flux2 klein三采极致生图流_2075854570143703041.json, 图片生成/文生图/krea2+flux2 klein三采极致生图流（MUSE艺术版）_2050784159613898754.json, 图片生成/文生图/krea2+flux2 klein三采极致生图流（红潮艺术版）_2073728023936983042.json, 图片生成/文生图/krea2turbo 基础工作流+LORA+KLINE放大_2080283253579272193.json, 平台全量/万能无损4K高清放大，（场景物体细节，人像增加皮肤细节真实感）_2072653203409297410.json, 平台全量/图片_视频高清修复工作流_2082826040807878657.json, 平台全量/高清放大修复2-8K_2049743364827951105.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/krea2+flux2 klein三采极致生图流_2075854570143703041.json、图片生成/文生图/krea2+flux2 klein三采极致生图流（MUSE艺术版）_2050784159613898754.json、图片生成/文生图/krea2+flux2 klein三采极致生图流（红潮艺术版）_2073728023936983042.json、图片生成/文生图/krea2turbo 基础工作流+LORA+KLINE放大_2080283253579272193.json、平台全量/万能无损4K高清放大，（场景物体细节，人像增加皮肤细节真实感）_2072653203409297410.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `ImageResize+` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `SeedVR2LoadDiTModel` —— 6/7 个有
- `SeedVR2LoadVAEModel` —— 6/7 个有
- `SeedVR2VideoUpscaler` —— 6/7 个有
- `TTP_Image_Assy` —— 6/7 个有
- `TTP_Image_Tile_Batch` —— 6/7 个有
- `TTP_Tile_image_size` —— 6/7 个有
- `easy imageSize` —— 6/7 个有
- `Label (rgthree)` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `EmptyLatentImage` —— 4/7 个有
- `KSamplerAdvanced` —— 4/7 个有
- `TTResolutionSelector` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `ConditioningKrea2Rebalance` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `Int` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `easy promptList` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `FlashVSRInitPipe` —— 1/7 个有
- `FlashVSRNodeAdv` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `Seed Generator` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有
- `孤海注释` —— 1/7 个有

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
