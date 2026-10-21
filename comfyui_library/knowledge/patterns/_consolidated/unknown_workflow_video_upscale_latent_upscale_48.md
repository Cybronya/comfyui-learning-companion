---
name: unknown_workflow_video_upscale_latent_upscale_48
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.921375
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2035704140126494721.json, 视频生成/图生视频/LTX2.3 图生视频_2085391376946122754.json, 视频生成/图生视频/2036666522667589634.json, 视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146.json, 视频生成/图生视频/2030519163785060353.json, 视频生成/图生视频/2030546098619682817.json, 视频生成/图生视频/2030921554300768258.json, 视频生成/图生视频/2030280752230830082.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_48

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2035704140126494721.json、视频生成/图生视频/LTX2.3 图生视频_2085391376946122754.json、视频生成/图生视频/2036666522667589634.json、视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146.json、视频生成/图生视频/2030519163785060353.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 7/8 个有
- `LTXVAudioVAELoader` —— 7/8 个有
- `LTXVChunkFeedForward` —— 7/8 个有
- `LTXVImgToVideoConditionOnly` —— 7/8 个有
- `LTXVPreprocess` —— 7/8 个有
- `ModelPatchTorchSettings` —— 7/8 个有
- `PathchSageAttentionKJ` —— 7/8 个有
- `PrimitiveBoolean` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `PrimitiveFloat` —— 5/8 个有
- `LTXVFirstLastFrameControl_TTP` —— 4/8 个有
- `RH_LLMAPI_Pro_Node` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `SimpleMath+` —— 2/8 个有
- `CM_IntToFloat` —— 1/8 个有
- `DualCLIPLoader` —— 1/8 个有
- `GetImageSize+` —— 1/8 个有
- `LTXVImgToVideoInplaceKJ` —— 1/8 个有
- `LTXVReferenceAudio` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `MelBandRoFormerModelLoader` —— 1/8 个有
- `MelBandRoFormerSampler` —— 1/8 个有
- `PromptRelayEncode` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `SaveAudio` —— 1/8 个有
- `UNETLoader` —— 1/8 个有
- `VAELoaderKJ` —— 1/8 个有
- `easy float` —— 1/8 个有
- `easy getNode` —— 1/8 个有
- `easy mathInt` —— 1/8 个有
- `easy setNode` —— 1/8 个有
- `孤海注释` —— 1/8 个有

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
