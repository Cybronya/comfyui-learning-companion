---
name: unknown_workflow_upscale_latent_upscale_lora_38
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.83525
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/2053476061249323010.json, 视频生成/图生视频/2038606312925306881.json, 视频生成/图生视频/2041874975627415554.json, 视频生成/图生视频/2079742870340325377.json, 视频生成/图生视频/2030885319217782785.json, 视频生成/图生视频/2031213206097633281.json, 视频生成/图生视频/2040620367496089602.json, 视频生成/图生视频/2078421854469050370.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_38

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2053476061249323010.json、视频生成/图生视频/2038606312925306881.json、视频生成/图生视频/2041874975627415554.json、视频生成/图生视频/2079742870340325377.json、视频生成/图生视频/2030885319217782785.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `ResizeImagesByLongerEdge` —— 7/8 个有
- `VAEDecodeTiled` —— 7/8 个有
- `Int` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `LoadAudio` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `ResizeImageMaskNode` —— 6/8 个有
- `PrimitiveBoolean` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `CR Integer To String` —— 3/8 个有
- `CR Text` —— 3/8 个有
- `GetAudioDurationFromAudio` —— 3/8 个有
- `MathExpression|pysssss` —— 3/8 个有
- `RH_LLMAPI_NODE` —— 3/8 个有
- `RH_LLMAPI_Pro_Node` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `SolidMask` —— 3/8 个有
- `easy promptReplace` —— 3/8 个有
- `CM_FloatToInt` —— 2/8 个有
- `LTXVAudioVAEEncode` —— 2/8 个有
- `LTXVImgToVideoInplaceKJ` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `MelBandRoFormerModelLoader` —— 2/8 个有
- `MelBandRoFormerSampler` —— 2/8 个有
- `SetLatentNoiseMask` —— 2/8 个有
- `SoundFlow_GetLength` —— 2/8 个有
- `TrimAudioDuration` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `LTXVReferenceAudio` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `RecordAudio` —— 1/8 个有
- `VAEDecode` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有

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
