---
name: text_to_image_upscale_lora_sampler_10
type: Text To Image
frequency: 8
level: weak
coverage: 0.861625
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/✅《极致美学》-Zimage_MJ风格_2079739133559398402.json, 图片生成/文生图/三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769.json, 图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein-提示词扩写版_2071872383069286402.json, 图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein_2071613444608057345.json, 图片生成/文生图/图像模仿洗图-高质量三采样-krea2+Klein+zimage_2072250385414311938.json, 图片生成/文生图/极致美学-Zimage_mj风格版-高清_2079533122739331073.json, 图片生成/文生图/极致美学-Zimage_mj风格版-高清_2096071482471436290.json, 图片生成/文生图/极致美学高清生成｜Z-Image MJ风格版文生图制作_2096334353323347969.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/✅《极致美学》-Zimage_MJ风格_2079739133559398402.json、图片生成/文生图/三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769.json、图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein-提示词扩写版_2071872383069286402.json、图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein_2071613444608057345.json、图片生成/文生图/图像模仿洗图-高质量三采样-krea2+Klein+zimage_2072250385414311938.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
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
- `GetNode` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `CLIPLoaderGGUF` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `GetImageSize+` —— 4/8 个有
- `ImageCASharpening+` —— 4/8 个有
- `PhotoShakeNode` —— 4/8 个有
- `RunningHub Deepcleaner` —— 4/8 个有
- `TTResolutionSelector` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `easy imageSize` —— 4/8 个有
- `RH_LLMAPI_Pro_Node` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `孤海注释` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有
- `solarL_SaveImagesToZip` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 10 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 8 | 19% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 0.25 - 1 | 8 | 49% |
| 宽度 | 1024 | 80 - 1080 | 8 | 65% |
| 高度 | 1024 | 80 - 1480 | 8 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，8 个样本，取值分散，一致性仅 49%
- 宽度 中位数 1024，观测区间 80 - 1080，8 个样本
- 高度 中位数 1024，观测区间 80 - 1480，8 个样本
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
