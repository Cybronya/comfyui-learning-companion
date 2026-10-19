---
name: unknown_workflow_video_upscale_latent_upscale_40
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7613
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2009919579048382465.json, 视频生成/图生视频/2009073353373519874.json, 视频生成/图生视频/2048596027241930753.json, 视频生成/图生视频/2011039306126725122.json, 视频生成/图生视频/2011355814191177729.json, 视频生成/图生视频/2011038713081499649.json, 视频生成/图生视频/2009647759535644673.json, 视频生成/图生视频/2011496236766994433.json, 视频生成/文生视频/LTX-2图_3图NVFP4首尾帧_2009643807456890881.json, 视频生成/文生视频/LTX-2图_3图首尾帧_2009549891193806850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_40

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2009919579048382465.json、视频生成/图生视频/2009073353373519874.json、视频生成/图生视频/2048596027241930753.json、视频生成/图生视频/2011039306126725122.json、视频生成/图生视频/2011355814191177729.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
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
- `PrimitiveInt` —— 8/10 个有
- `LTXVFirstLastFrameControl_TTP` —— 6/10 个有
- `ResizeImagesByLongerEdge` —— 6/10 个有
- `ShowText|pysssss` —— 6/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `Int` —— 5/10 个有
- `JoinStrings` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `Qwen3_VQA` —— 5/10 个有
- `TextInput_` —— 5/10 个有
- `VAEDecodeTiled` —— 5/10 个有
- `VRAMReserver` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `ImageConcatMulti` —— 4/10 个有
- `LTXVImgToVideoInplace` —— 4/10 个有
- `MemoryCleaner` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `VAEDecode` —— 4/10 个有
- `FloatConstant` —— 3/10 个有
- `INTConstant` —— 3/10 个有
- `LTXVMiddleFrame_TTP` —— 3/10 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 3/10 个有
- `LayerUtility: PurgeVRAM V2` —— 3/10 个有
- `ImpactSwitch` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `ShellAgentPluginOutputText` —— 1/10 个有
- `ToFloat` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 10 | 93% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，10 个样本，取值集中（一致性 93%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
