---
name: unknown_workflow_upscale_latent_upscale_lora_38
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.859571
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/2053476061249323010.json, 视频生成/图生视频/2038606312925306881.json, 视频生成/图生视频/2041874975627415554.json, 视频生成/图生视频/2079742870340325377.json, 视频生成/图生视频/2040620367496089602.json, 视频生成/图生视频/2033053099966865410.json, 视频生成/图生视频/2078421854469050370.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_38

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2053476061249323010.json、视频生成/图生视频/2038606312925306881.json、视频生成/图生视频/2041874975627415554.json、视频生成/图生视频/2079742870340325377.json、视频生成/图生视频/2040620367496089602.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LTXVImgToVideoInplace` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `ResizeImagesByLongerEdge` —— 6/7 个有
- `VAEDecodeTiled` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `ResizeImageMaskNode` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `Int` —— 4/7 个有
- `LoadAudio` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `RH_LLMAPI_Pro_Node` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `CR Integer To String` —— 3/7 个有
- `GetAudioDurationFromAudio` —— 3/7 个有
- `MathExpression|pysssss` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 3/7 个有
- `easy promptReplace` —— 3/7 个有
- `LTXVImgToVideoInplaceKJ` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LTXVReferenceAudio` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RecordAudio` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `SolidMask` —— 1/7 个有
- `VAEDecode` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
