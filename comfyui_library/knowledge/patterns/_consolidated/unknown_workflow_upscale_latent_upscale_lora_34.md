---
name: unknown_workflow_upscale_latent_upscale_lora_34
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.642875
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/2012334757446684674.json, 视频生成/图生视频/2019749362657660929.json, 视频生成/图生视频/2016324555433840641.json, 视频生成/图生视频/2073298883534483458.json, 视频生成/图生视频/2010303270488641537.json, 视频生成/图生视频/2013159959533461506.json, 视频生成/图生视频/2010620501831458818.json, 视频生成/图生视频/2010611172453654529.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_34

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2012334757446684674.json、视频生成/图生视频/2019749362657660929.json、视频生成/图生视频/2016324555433840641.json、视频生成/图生视频/2073298883534483458.json、视频生成/图生视频/2010303270488641537.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：64%

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

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `Int` —— 6/8 个有
- `VAEDecodeTiled` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `LTXVImgToVideoInplace` —— 5/8 个有
- `PrimitiveInt` —— 5/8 个有
- `LayerUtility: PurgeVRAM V2` —— 4/8 个有
- `ShowText|pysssss` —— 4/8 个有
- `SimpleMath+` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `GetNode` —— 3/8 个有
- `JoinStrings` —— 3/8 个有
- `LTXVFirstLastFrameControl_TTP` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `Qwen3_VQA` —— 3/8 个有
- `ResizeImagesByLongerEdge` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `TextInput_` —— 3/8 个有
- `CreateVideo` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `VAEDecode` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 8 | 89% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，8 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
