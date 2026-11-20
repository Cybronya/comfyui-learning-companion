---
name: unknown_workflow_video_upscale_latent_upscale_17
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.900714
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/LTX2.0线稿控制视频生成（48G）_2008544083928682497.json, 平台全量/video_ltx2_canny_to_video_unpack_2008733579580284929.json, 平台全量/video_ltx2_pose_to_video_unpack_2008737413929115649.json, 视频生成/图生视频/LTX2.0 最新图生视频工作流（48G）_2017463595512111106.json, 视频生成/图生视频/LTX_2_First_Last_I2V_ttp_v2_2009559520669863938.json, 视频生成/图生视频/LTX_2_首尾帧工作流_2019655709050281986.json, 视频生成/图生视频/LTX_2_首尾帧工作流_2019956098375094274.json, 视频生成/图生视频/LTX_2_首尾帧生视频_2010957418854879234.json, 视频生成/图生视频/LTX_2首尾帧工作流_2020659052396683265.json, 视频生成/图生视频/「Supermate」LTX_2_首尾帧工作流_2009326383134150658.json, 视频生成/图生视频/「Supermate」LTX_2_首尾帧工作流_2057293549762334721.json, 视频生成/图生视频/【加速】LTX2.0 图生视频工作流_2017478785842548737.json, 视频生成/图生视频/图生视频--LTX_2_首尾帧工作流_2057285774952980482.json, 视频生成/图生视频/大凯辰光 LTX-2 首尾帧工作流PLus版在线工作流_2009604954146742273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_17

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/LTX2.0线稿控制视频生成（48G）_2008544083928682497.json、平台全量/video_ltx2_canny_to_video_unpack_2008733579580284929.json、平台全量/video_ltx2_pose_to_video_unpack_2008737413929115649.json、视频生成/图生视频/LTX2.0 最新图生视频工作流（48G）_2017463595512111106.json、视频生成/图生视频/LTX_2_First_Last_I2V_ttp_v2_2009559520669863938.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 13/14 个有
- `VAEDecode` —— 13/14 个有
- `LoadImage` —— 12/14 个有
- `EmptyImage` —— 11/14 个有
- `LTXVPreprocess` —— 11/14 个有
- `ResizeImagesByLongerEdge` —— 11/14 个有
- `BetaSamplingScheduler` —— 9/14 个有
- `LTXVFirstLastFrameControl_TTP` —— 9/14 个有
- `MemoryCleaner` —— 8/14 个有
- `ImageResizeKJv2` —— 6/14 个有
- `LTXVImgToVideoInplace` —— 4/14 个有
- `INTConstant` —— 3/14 个有
- `LTXVAddGuide` —— 3/14 个有
- `VAEDecodeTiled` —— 3/14 个有
- `GetVideoComponents` —— 2/14 个有
- `ImageFromBatch` —— 2/14 个有
- `LoadVideo` —— 2/14 个有
- `PrimitiveBoolean` —— 2/14 个有
- `PrimitiveFloat` —— 2/14 个有
- `SaveImage` —— 2/14 个有
- `AIO_Preprocessor` —— 1/14 个有
- `Any To String (mtb)` —— 1/14 个有
- `Canny` —— 1/14 个有
- `DWPreprocessor` —— 1/14 个有
- `ImageScaleToMaxDimension` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `Qwen3_VQA` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `SmartImageConcat` —— 1/14 个有
- `Textbox` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有
- `easy textSwitch` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 24 - 25 | 14 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，14 个样本，取值集中（一致性 99%）
