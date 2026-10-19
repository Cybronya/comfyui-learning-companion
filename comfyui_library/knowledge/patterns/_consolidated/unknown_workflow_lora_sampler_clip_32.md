---
name: unknown_workflow_lora_sampler_clip_32
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.671857
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXSequencer, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LazySwitchKJ, LoraLoaderModelOnly, MultiImageLoader, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2059948094514618369.json, 视频生成/图生视频/2059920310899662850.json, 视频生成/图生视频/2059193500587094017.json, 视频生成/图生视频/2063202881095954433.json, 视频生成/图生视频/2059401786028544001.json, 视频生成/图生视频/2075878057012977666.json, 视频生成/文生视频/LTX I2V 多图生视频_2059954460599865345.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2059948094514618369.json、视频生成/图生视频/2059920310899662850.json、视频生成/图生视频/2059193500587094017.json、视频生成/图生视频/2063202881095954433.json、视频生成/图生视频/2059401786028544001.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXSequencer`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LazySwitchKJ`
- `LoraLoaderModelOnly`
- `MultiImageLoader`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `Int` —— 6/7 个有
- `LTXVLatentUpsampler` —— 6/7 个有
- `LatentUpscaleModelLoader` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `PrimitiveInt` —— 5/7 个有
- `CM_IntToFloat` —— 4/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `LTXVAudioVAEEncode` —— 4/7 个有
- `LoadAudioUI` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `SetLatentNoiseMask` —— 4/7 个有
- `SolidMask` —— 4/7 个有
- `easy mathInt` —— 4/7 个有
- `MathExpression|pysssss` —— 3/7 个有
- `Text` —— 3/7 个有
- `Float to Int` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `DF_Int_to_Float` —— 1/7 个有
- `LTXVChunkFeedForward` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy imageInsetCrop` —— 1/7 个有
- `easy setNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1 | 1 - 1 | 7 | 100% |
| 高度 | 24 | 24 - 24 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，7 个样本，取值集中（一致性 100%）
