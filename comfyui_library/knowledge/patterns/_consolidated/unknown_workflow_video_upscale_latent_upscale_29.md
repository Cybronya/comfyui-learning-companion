---
name: unknown_workflow_video_upscale_latent_upscale_29
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.586091
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LH-DMT-LTX2.0-006.首尾帧生视频-音画同步_2012334757446684674.json, 视频生成/图生视频/LH-DMT-LTX2.0-006.首尾帧生视频-音画同步_2019749362657660929.json, 视频生成/图生视频/LH-DMT-LTX2.0-007.LTX2.0-图生视频（优化版）全自动反推提示词_2016324555433840641.json, 视频生成/图生视频/LTX-2 极速图生视频_2010303270488641537.json, 视频生成/图生视频/LTX2.0-图生视频（优化版）全自动反推提示词_2011039306126725122.json, 视频生成/图生视频/LTX2.0-首尾帧生视频（优化版）_2011355814191177729.json, 视频生成/图生视频/LTX2.0-首尾帧生视频（优化版）全自动反推提示词_2011038713081499649.json, 视频生成/图生视频/LTX2.0首尾帧_首中尾帧生视频V1（附自动生提示词） 适合人物开车，动态适宜_2009647759535644673.json, 视频生成/图生视频/LTX2.0首尾帧_首中尾帧生视频V2（附自动生提示词） 适合人物开车，动态适宜_2016865338914250754.json, 视频生成/图生视频/LTX2首尾帧图生视频_2010620501831458818.json, 视频生成/图生视频/ltx-2图片首尾帧图生视频数字人视频生成对口型数字人大语言模型优化提示词（48gb）_2011496236766994433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_29

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LH-DMT-LTX2.0-006.首尾帧生视频-音画同步_2012334757446684674.json、视频生成/图生视频/LH-DMT-LTX2.0-006.首尾帧生视频-音画同步_2019749362657660929.json、视频生成/图生视频/LH-DMT-LTX2.0-007.LTX2.0-图生视频（优化版）全自动反推提示词_2016324555433840641.json、视频生成/图生视频/LTX-2 极速图生视频_2010303270488641537.json、视频生成/图生视频/LTX2.0-图生视频（优化版）全自动反推提示词_2011039306126725122.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 10/11 个有
- `GetImageSize` —— 10/11 个有
- `ImageScaleBy` —— 10/11 个有
- `LTXVCropGuides` —— 10/11 个有
- `Int` —— 9/11 个有
- `JoinStrings` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/11 个有
- `Qwen3_VQA` —— 9/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `TextInput_` —— 9/11 个有
- `easy showAnything` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 8/11 个有
- `LTXVFirstLastFrameControl_TTP` —— 8/11 个有
- `ImageConcatMulti` —— 7/11 个有
- `PreviewImage` —— 7/11 个有
- `VAEDecodeTiled` —— 7/11 个有
- `PrimitiveInt` —— 6/11 个有
- `LayerUtility: PurgeVRAM V2` —— 5/11 个有
- `VRAMReserver` —— 5/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `MemoryCleaner` —— 4/11 个有
- `VAEDecode` —— 4/11 个有
- `GetNode` —— 3/11 个有
- `LTXVImgToVideoInplace` —— 3/11 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `INTConstant` —— 2/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `LTXVMiddleFrame_TTP` —— 2/11 个有
- `ShellAgentPluginOutputText` —— 2/11 个有
- `SimpleMath+` —— 2/11 个有
- `CM_FloatToInt` —— 1/11 个有
- `CM_IntToFloat` —— 1/11 个有
- `DF_Int_to_Float` —— 1/11 个有
- `FloatConstant` —— 1/11 个有
- `JWIntegerDiv` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `ResizeImagesByLongerEdge` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 11 | 89% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，11 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
