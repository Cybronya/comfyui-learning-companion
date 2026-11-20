---
name: unknown_workflow_video_upscale_latent_upscale_50
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.720125
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.0 音视频同步-图生视频工作流_2009919579048382465.json, 视频生成/图生视频/LTX2.0+图生视频工作流（48G）_2009073353373519874.json, 视频生成/图生视频/LTX2.0+图生视频工作流（48G）_2048596027241930753.json, 视频生成/图生视频/LTX2.0-图生视频（优化版）全自动反推提示词_2011039306126725122.json, 视频生成/图生视频/LTX2.0-首尾帧生视频（优化版）_2011355814191177729.json, 视频生成/图生视频/LTX2.0-首尾帧生视频（优化版）全自动反推提示词_2011038713081499649.json, 视频生成/图生视频/LTX2.0首尾帧_首中尾帧生视频V1（附自动生提示词） 适合人物开车，动态适宜_2009647759535644673.json, 视频生成/图生视频/ltx-2图片首尾帧图生视频数字人视频生成对口型数字人大语言模型优化提示词（48gb）_2011496236766994433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_50

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX2.0 音视频同步-图生视频工作流_2009919579048382465.json、视频生成/图生视频/LTX2.0+图生视频工作流（48G）_2009073353373519874.json、视频生成/图生视频/LTX2.0+图生视频工作流（48G）_2048596027241930753.json、视频生成/图生视频/LTX2.0-图生视频（优化版）全自动反推提示词_2011039306126725122.json、视频生成/图生视频/LTX2.0-首尾帧生视频（优化版）_2011355814191177729.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
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
- `PrimitiveInt` —— 6/8 个有
- `ShowText|pysssss` —— 6/8 个有
- `Int` —— 5/8 个有
- `JoinStrings` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `Qwen3_VQA` —— 5/8 个有
- `TextInput_` —— 5/8 个有
- `VAEDecodeTiled` —— 5/8 个有
- `VRAMReserver` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `ImageConcatMulti` —— 4/8 个有
- `LTXVFirstLastFrameControl_TTP` —— 4/8 个有
- `LTXVImgToVideoInplace` —— 4/8 个有
- `MemoryCleaner` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `ResizeImagesByLongerEdge` —— 4/8 个有
- `VAEDecode` —— 4/8 个有
- `ImageResizeKJv2` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `FloatConstant` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `LTXVMiddleFrame_TTP` —— 1/8 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `ShellAgentPluginOutputText` —— 1/8 个有
- `ToFloat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 8 | 92% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，8 个样本，取值集中（一致性 92%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
