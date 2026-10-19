---
name: unknown_workflow_video_upscale_latent_upscale_116
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.746667
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RegexExtract, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy positive, easy promptLine]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3全栈式短剧生成V10（lora版）_2043329392163688450.json, 视频生成/文生视频/LTX2.3全栈式短视频生成V9（ID-lora单人版）_2044031772660342786.json, 视频生成/文生视频/LTX2.3全栈式短视频生成V9（单人Lora版）_2041880704421732354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_116

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/LTX2.3全栈式短剧生成V10（lora版）_2043329392163688450.json、视频生成/文生视频/LTX2.3全栈式短视频生成V9（ID-lora单人版）_2044031772660342786.json、视频生成/文生视频/LTX2.3全栈式短视频生成V9（单人Lora版）_2041880704421732354.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RegexExtract`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy positive`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `LongTextToList` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `TrimVideoLatent` —— 2/3 个有
- `easy indexAnything` —— 2/3 个有
- `LTXVReferenceAudio` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `easy ifElse` —— 1/3 个有
- `easy mathString` —— 1/3 个有
- `easy promptList` —— 1/3 个有
- `easy promptReplace` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
