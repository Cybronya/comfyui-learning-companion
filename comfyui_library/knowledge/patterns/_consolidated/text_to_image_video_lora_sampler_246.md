---
name: text_to_image_video_lora_sampler_246
type: Text To Image
frequency: 2
level: weak
coverage: 0.921
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DiffusionModelLoaderKJ, EmptyLatentImage, GetImageRangeFromBatch, GetImageSize, ImageResizeKJv2, JWInteger, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/跳舞动作不限时长复刻 SCAIL2单人图生视频迁移方案_2104357540426502145.json, 视频生成/文生视频/Scail2动作迁移｜单人多人都支持｜文生视频图生视频一路通吃_2102572579264487425.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_246

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/跳舞动作不限时长复刻 SCAIL2单人图生视频迁移方案_2104357540426502145.json、视频生成/文生视频/Scail2动作迁移｜单人多人都支持｜文生视频图生视频一路通吃_2102572579264487425.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `ImageResizeKJv2`
- `JWInteger`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `TensorLoopClose`
- `TensorLoopOpen`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `Int` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `SAM3_TrackToMask` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `WanChunkFeedForward` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
