---
name: unknown_workflow_video_lora_sampler_378
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.944667
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2034652282570153986.json, 视频生成/图生视频/2031229701166993409.json, 视频生成/图生视频/2036741088412700673.json, 视频生成/图生视频/2075032295114895362.json, 视频生成/图生视频/2032494068420317186.json, 视频生成/图生视频/2030439938361135105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_378

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2034652282570153986.json、视频生成/图生视频/2031229701166993409.json、视频生成/图生视频/2036741088412700673.json、视频生成/图生视频/2075032295114895362.json、视频生成/图生视频/2032494068420317186.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `Seed (rgthree)` —— 4/6 个有
- `DapaoImageAspectRatioResizeNode` —— 3/6 个有
- `RH_LLMAPI_Pro_Node` —— 3/6 个有
- `easy int` —— 3/6 个有
- `JWInteger` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `Int` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LatentUpscaleModelLoader` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `ResizeImageMaskNode` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `ShowText` —— 1/6 个有
- `TextBox` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
