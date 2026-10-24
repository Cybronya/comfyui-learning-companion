---
name: text_to_image_upscale_lora_sampler_19
type: Text To Image
frequency: 10
level: weak
coverage: 0.8486
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 二次采样+细节修复_2079377686283243522.json, 图片生成/文生图/krea2+zit+flux2-klein三采极致图_2080093488003248130.json, 图片生成/文生图/✅《极致美学》-Zimage_MJ风格_2079739133559398402.json, 图片生成/文生图/三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769.json, 图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein-提示词扩写版_2071872383069286402.json, 图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein_2071613444608057345.json, 图片生成/文生图/图像模仿洗图-高质量三采样-krea2+Klein+zimage_2072250385414311938.json, 图片生成/文生图/极致美学-Zimage_mj风格版-高清_2079533122739331073.json, 图片生成/文生图/极致美学-Zimage_mj风格版-高清_2096071482471436290.json, 图片生成/文生图/邪修krea2单模型双采，细节拉满！（萌妹lora版）_2079122786253103105.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/krea2 二次采样+细节修复_2079377686283243522.json、图片生成/文生图/krea2+zit+flux2-klein三采极致图_2080093488003248130.json、图片生成/文生图/✅《极致美学》-Zimage_MJ风格_2079739133559398402.json、图片生成/文生图/三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769.json、图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein-提示词扩写版_2071872383069286402.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
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
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 9/10 个有
- `GetNode` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 7/10 个有
- `easy cleanGpuUsed` —— 7/10 个有
- `easy imageSize` —— 7/10 个有
- `TTResolutionSelector` —— 6/10 个有
- `CLIPLoaderGGUF` —— 5/10 个有
- `GetImageSize+` —— 3/10 个有
- `ImageCASharpening+` —— 3/10 个有
- `PhotoShakeNode` —— 3/10 个有
- `RH_LLMAPI_Pro_Node` —— 3/10 个有
- `RunningHub Deepcleaner` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `ColorMatchV2` —— 2/10 个有
- `ConditioningKrea2Rebalance` —— 2/10 个有
- `KSamplerAdvanced` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `LatentUpscaleBy` —— 2/10 个有
- `easy promptList` —— 2/10 个有
- `GODMT_MergeList` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `MemoryCleaner` —— 1/10 个有
- `ResolutionSelector` —— 1/10 个有
- `Text` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 5 - 10 | 8 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 10 | 0% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 0.675 | 0.25 - 1 | 8 | 43% |
| 宽度 | 1024 | 1024 - 1920 | 10 | 77% |
| 高度 | 1024 | 1024 - 1480 | 10 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 5 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，10 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 0.675，观测区间 0.25 - 1，8 个样本，取值分散，一致性仅 43%
- 宽度 中位数 1024，观测区间 1024 - 1920，10 个样本
- 高度 中位数 1024，观测区间 1024 - 1480，10 个样本，取值集中（一致性 82%）
- 高发问题（12/10 个样本）：Steps较低可能导致细节不足
