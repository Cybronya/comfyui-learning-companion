---
name: unknown_workflow_video_sampler_clip_221
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8445
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3_图生视频_2030308264814059522.json, 视频生成/文生视频/LTX2.5- 图生+文生视频_2034499552383868929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_221

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3_图生视频_2030308264814059522.json、视频生成/文生视频/LTX2.5- 图生+文生视频_2034499552383868929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `Int` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
