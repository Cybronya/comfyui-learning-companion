---
name: text_to_image_video_upscale_lora_2
type: Text To Image
frequency: 7
level: strong
coverage: 0.601
common_nodes: [AILab_ImagePreview, BatchImagesNode, BiRefNetRMBG, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, DownloadAndLoadGIMMVFIModel, EmptyLatentImage, Fast Muter (rgthree), GIMMVFI_interpolate, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageResizeKJv2, ImageScaleToMaxDimension, ImageStitch, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, RepeatImageBatch, SAM3_TrackPreview, SAM3_VideoTrack, SCAIL2ColoredMask, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy boolean, easy cleanGpuUsed, easy ifElse, easy int, easy loraStack, easy loraStackApply, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Scail2官流V2视频编辑｜不限时长动作迁移主体替换_2096298660555485185.json, 视频生成/图生视频/Scail2视频编辑不限时长｜动作迁移主体替换生成_2096293318664740865.json, 视频生成/图生视频/主体替换随意换｜Scail2不限时长动作迁移视频编辑_2096550991251460097.json, 视频生成/图生视频/官流V2升级版｜Scail2动作迁移主体替换不限时长_2096562131494858753.json, 视频生成/图生视频/官流V2版Scail2视频编辑 主体替换不限时长动作迁移_2095808579520524290.json, 视频生成/图生视频/官流V2版Scail2视频编辑_主体替换不限时长动作迁移_2100196788388065282.json, 视频生成/图生视频/官流V2版Scail2视频编辑_主体替换不限时长动作迁移_2100788222061273090.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Scail2官流V2视频编辑｜不限时长动作迁移主体替换_2096298660555485185.json、视频生成/图生视频/Scail2视频编辑不限时长｜动作迁移主体替换生成_2096293318664740865.json、视频生成/图生视频/主体替换随意换｜Scail2不限时长动作迁移视频编辑_2096550991251460097.json、视频生成/图生视频/官流V2升级版｜Scail2动作迁移主体替换不限时长_2096562131494858753.json、视频生成/图生视频/官流V2版Scail2视频编辑 主体替换不限时长动作迁移_2095808579520524290.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 7 个 workflow 都包含：
- `AILab_ImagePreview`
- `BatchImagesNode`
- `BiRefNetRMBG`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyLatentImage`
- `Fast Muter (rgthree)`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `ImageStitch`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `RepeatImageBatch`
- `SAM3_TrackPreview`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy int`
- `easy loraStack`
- `easy loraStackApply`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `WanAnimatePlus SCAIL_2 Flow Embeds` —— 5/7 个有
- `WanAnimatePlus SCAIL_2 Flow Sampler` —— 5/7 个有
- `WanAnimatePlus VAE Decode` —— 5/7 个有
- `孤海注释` —— 5/7 个有
- `InsertImagesToBatchIndexed` —— 4/7 个有
- `ModelAttentionBackend` —— 4/7 个有
- `StringConcatenate` —— 4/7 个有
- `UNETLoader_Any` —— 4/7 个有
- `UniBlockSwap` —— 4/7 个有
- `WanChunkFeedForward` —— 4/7 个有
- `DiffusionModelLoaderKJ` —— 3/7 个有
- `RMBG` —— 3/7 个有
- `SkipLayerGuidanceDiTSimple` —— 3/7 个有
- `wanBlock_Swap` —— 3/7 个有
- `BasicScheduler` —— 2/7 个有
- `CFGGuider` —— 2/7 个有
- `Display Int (rgthree)` —— 2/7 个有
- `EmptyImage` —— 2/7 个有
- `ImageBatchExtendWithOverlap` —— 2/7 个有
- `KSamplerSelect` —— 2/7 个有
- `ModelSamplingSD3` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `RandomNoise` —— 2/7 个有
- `SamplerCustomAdvanced` —— 2/7 个有
- `WanSCAILToVideo` —— 2/7 个有
- `easy compare` —— 2/7 个有
- `easy forLoopEnd` —— 2/7 个有
- `easy forLoopStart` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
