---
name: unknown_workflow_lora_sampler_clip_12
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.862273
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2042083663428460545.json, 视频生成/图生视频/2030927886542180353.json, 视频生成/图生视频/2037366573874290689.json, 视频生成/图生视频/2058356490804752385.json, 视频生成/图生视频/2043593704170070018.json, 视频生成/图生视频/2043581288925372417.json, 视频生成/图生视频/2031297244112101377.json, 视频生成/图生视频/2031346405217935361.json, 视频生成/图生视频/2054790441681342465.json, 视频生成/图生视频/2054484478025838593.json, 视频生成/图生视频/2039165345923080193.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2042083663428460545.json、视频生成/图生视频/2030927886542180353.json、视频生成/图生视频/2037366573874290689.json、视频生成/图生视频/2058356490804752385.json、视频生成/图生视频/2043593704170070018.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 10/11 个有
- `KSamplerSelect` —— 10/11 个有
- `LTXVLatentUpsampler` —— 10/11 个有
- `LatentUpscaleModelLoader` —— 10/11 个有
- `LTXVImgToVideoInplace` —— 9/11 个有
- `ResizeImagesByLongerEdge` —— 9/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `ResizeImageMaskNode` —— 8/11 个有
- `LTXVAudioVAEEncode` —— 7/11 个有
- `LoadAudio` —— 7/11 个有
- `PrimitiveBoolean` —— 7/11 个有
- `SetLatentNoiseMask` —— 7/11 个有
- `SolidMask` —— 7/11 个有
- `PrimitiveFloat` —— 6/11 个有
- `TrimAudioDuration` —— 6/11 个有
- `LTXVEmptyLatentAudio` —— 4/11 个有
- `PreviewAny` —— 4/11 个有
- `GetImageSize` —— 2/11 个有
- `LoraLoader` —— 2/11 个有
- `SimpleMath+` —— 2/11 个有
- `SoundFlow_GetLength` —— 2/11 个有
- `StringReplace` —— 2/11 个有
- `TextGenerateLTX2Prompt` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `AudioCrop` —— 1/11 个有
- `AudioInfo` —— 1/11 个有
- `Bjornulf_ShowInt` —— 1/11 个有
- `FishS2VoiceCloneTTS` —— 1/11 个有
- `ImageResize+` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `LTXVAddGuide` —— 1/11 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `PreviewAudio` —— 1/11 个有
- `Qwen3ASRLoader_DFT` —— 1/11 个有
- `Qwen3ASRTranscribe_DFT` —— 1/11 个有
- `SamplerEulerAncestral` —— 1/11 个有
- `StringConcatenate` —— 1/11 个有
- `string_util_StrConcat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 24 - 25 | 4 | 98% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，4 个样本，取值集中（一致性 98%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
