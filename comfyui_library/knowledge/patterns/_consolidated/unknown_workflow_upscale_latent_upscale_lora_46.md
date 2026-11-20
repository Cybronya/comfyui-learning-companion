---
name: unknown_workflow_upscale_latent_upscale_lora_46
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.87425
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAddGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [平台全量/LTX-2 Canny控制生成视频_2008900065330470913.json, 平台全量/LTX-2 线稿控制生成视频_2008944993523732482.json, 平台全量/LTX-2姿势控制生成视频_2008876367240237057.json, 平台全量/LTX-2深度控制生成视频_2008887286984876033.json, 平台全量/LTX2.0深度控制视频生成-48G专用_2008857194787250178.json, 平台全量/LTX2.0线稿控制视频生成-48G专用_2008853903592398850.json, 平台全量/video_ltx2_depth_to_video_unpack_2008730641403219969.json, 视频生成/文生视频/LTX-视频_2013202671984971778.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_46

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/LTX-2 Canny控制生成视频_2008900065330470913.json、平台全量/LTX-2 线稿控制生成视频_2008944993523732482.json、平台全量/LTX-2姿势控制生成视频_2008876367240237057.json、平台全量/LTX-2深度控制生成视频_2008887286984876033.json、平台全量/LTX2.0深度控制视频生成-48G专用_2008857194787250178.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 7/8 个有
- `ImageFromBatch` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `LoadVideo` —— 7/8 个有
- `VAEDecode` —— 7/8 个有
- `VHS_VideoCombine` —— 7/8 个有
- `LTXVImgToVideoInplace` —— 6/8 个有
- `Canny` —— 5/8 个有
- `CreateVideo` —— 5/8 个有
- `LoadImage` —— 5/8 个有
- `PrimitiveBoolean` —— 5/8 个有
- `PrimitiveFloat` —— 5/8 个有
- `PrimitiveInt` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `BasicGuider` —— 4/8 个有
- `BasicScheduler` —— 4/8 个有
- `DisableNoise` —— 4/8 个有
- `ImageInvert` —— 4/8 个有
- `LotusConditioning` —— 4/8 个有
- `SetFirstSigma` —— 4/8 个有
- `UNETLoader` —— 4/8 个有
- `VAEEncode` —— 4/8 个有
- `VAELoader` —— 4/8 个有
- `Label (rgthree)` —— 3/8 个有
- `DWPreprocessor` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `CM_FloatToInt` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `Fast Bypasser (rgthree)` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Get resolution [Crystools]` —— 1/8 个有
- `ImageBatchMulti` —— 1/8 个有
- `ImageScale` —— 1/8 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/8 个有
- `LTXVPreprocess` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `ResizeImagesByLongerEdge` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `VHS_VideoInfo` —— 1/8 个有
- `easy compare` —— 1/8 个有
- `easy ifElse` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
