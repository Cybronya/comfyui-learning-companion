---
name: text_to_image_video_upscale_lora_4
type: Text To Image
frequency: 4
level: strong
coverage: 0.5295
common_nodes: [AILab_ImageCrop, AILab_ImagePreview, BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, Display Int (rgthree), DownloadAndLoadGIMMVFIModel, EmptyLatentImage, GIMMVFI_interpolate, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageFromBatch, ImageResizeKJv2, ImageScaleToMaxDimension, ImageStitch, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingSD3, PreviewAnimation, PreviewImage, RMBG, RepeatImageBatch, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, SetNode, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanSCAILToVideo, easy boolean, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Scail2不限时长视频编辑 动作迁移与主体替换双支持_2095809955990433794.json, 视频生成/图生视频/Scail2不限时长视频编辑 动作迁移与主体替换双支持_2096554280982503425.json, 视频生成/图生视频/Scail2不限时长视频编辑_动作迁移与主体替换双支持_2101171204244721665.json, 视频生成/图生视频/Scail2不限时长视频编辑_动作迁移与主体替换双支持_2101448926615400450.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Scail2不限时长视频编辑 动作迁移与主体替换双支持_2095809955990433794.json、视频生成/图生视频/Scail2不限时长视频编辑 动作迁移与主体替换双支持_2096554280982503425.json、视频生成/图生视频/Scail2不限时长视频编辑_动作迁移与主体替换双支持_2101171204244721665.json、视频生成/图生视频/Scail2不限时长视频编辑_动作迁移与主体替换双支持_2101448926615400450.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_ImageCrop`
- `AILab_ImagePreview`
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `Display Int (rgthree)`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyLatentImage`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `ImageStitch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingSD3`
- `PreviewAnimation`
- `PreviewImage`
- `RMBG`
- `RepeatImageBatch`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanSCAILToVideo`
- `easy boolean`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy int`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/4 个有
- `孤海注释` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
