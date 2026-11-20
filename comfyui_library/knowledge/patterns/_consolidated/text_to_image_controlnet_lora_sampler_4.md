---
name: text_to_image_controlnet_lora_sampler_4
type: Text To Image
frequency: 6
level: strong
coverage: 0.795333
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Get Image Size, GetImageSizeAndCount, ImageCASharpening+, ImageResize+, ImageScaleToTotalPixels, ImpactMinMax, ImpactSwitch, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaraScottIsEmptyOrNone_v1, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, RH_Captioner, SaveImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy showAnything, ttN concat]
problems: []
missing: []
members: [图片生成/图生图/Z-Image ControlNet 2.1 2601 八步最新洗图_2015610869585027073.json, 图片生成/图生图/Z-Image ControlNet 最新洗图+放大_2001098985597173761.json, 图片生成/图生图/Z-Image+ControlNet 最强洗图_2014936453461053441.json, 图片生成/图生图/图像4K放大 可指定头像 洗图 Z-Image+ControlNet 2_2003022377183244289.json, 图片生成/图生图/洗图 Z-Image+ControlNet 2+TTP +SeedVR2放大_2007687831925297154.json, 图片生成/文生图/Z-Image+ControlNet 2最新洗图_1996252169982590978.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-Image ControlNet 2.1 2601 八步最新洗图_2015610869585027073.json、图片生成/图生图/Z-Image ControlNet 最新洗图+放大_2001098985597173761.json、图片生成/图生图/Z-Image+ControlNet 最强洗图_2014936453461053441.json、图片生成/图生图/图像4K放大 可指定头像 洗图 Z-Image+ControlNet 2_2003022377183244289.json、图片生成/图生图/洗图 Z-Image+ControlNet 2+TTP +SeedVR2放大_2007687831925297154.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Get Image Size`
- `GetImageSizeAndCount`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `ImpactMinMax`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaraScottIsEmptyOrNone_v1`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `RH_Captioner`
- `SaveImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy showAnything`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `DepthAnything_V2` —— 1/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1536 | 1536 - 1536 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，6 个样本，取值集中（一致性 100%）
