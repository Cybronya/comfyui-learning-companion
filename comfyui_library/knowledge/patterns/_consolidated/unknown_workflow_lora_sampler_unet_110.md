---
name: unknown_workflow_lora_sampler_unet_110
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.891
common_nodes: [CFGGuider, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAddGuidesFromBatchIndexes, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, PromptRelaySmartEncode, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SimpleMath+, SolidMask, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, easy ifElse, easy saveVideo, easy timelineEditor, easy timelineInfoOutput]
problems: []
missing: []
members: [视频生成/图生视频/(智能多参) Ltx2.3 Singularity+Licon-MSR+EasyMedia导演台V3_2063189005126168577.json, 视频生成/图生视频/(智能多参-正式版）- Ltx2.3 Licon-MSR+EasyMedia导演台V1_2063442671171104770.json, 视频生成/图生视频/(智能多帧) Ltx2.3 Singularity+EasyMedia导演工作台v3_2063140910652813313.json, 视频生成/图生视频/(首尾帧) Ltx2.3 Singularity+EasyMedia导演工作台V3_2063140222006808577.json, 视频生成/图生视频/LTX 2.3 + Licon-MSR：多参考图时间线导演_2066752524996136961.json, 视频生成/图生视频/Ltx2.3 Singularity+EasyMedia导演工作台(乱神版)V3_2063129511406952450.json, 视频生成/图生视频/开源版seedance2.0(智能多参)+Ltx2.3+Singularity+Licon-MSR_2063514127636717569.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_110

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/(智能多参) Ltx2.3 Singularity+Licon-MSR+EasyMedia导演台V3_2063189005126168577.json、视频生成/图生视频/(智能多参-正式版）- Ltx2.3 Licon-MSR+EasyMedia导演台V1_2063442671171104770.json、视频生成/图生视频/(智能多帧) Ltx2.3 Singularity+EasyMedia导演工作台v3_2063140910652813313.json、视频生成/图生视频/(首尾帧) Ltx2.3 Singularity+EasyMedia导演工作台V3_2063140222006808577.json、视频生成/图生视频/LTX 2.3 + Licon-MSR：多参考图时间线导演_2066752524996136961.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAddGuidesFromBatchIndexes`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PromptRelaySmartEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `easy ifElse`
- `easy saveVideo`
- `easy timelineEditor`
- `easy timelineInfoOutput`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/7 个有
- `LTXVMakeRefVideo` —— 4/7 个有
- `easy timelineSegmentOutput` —— 4/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `LTXVImgToVideoInplace` —— 3/7 个有
- `LTXVLatentUpsampler` —— 3/7 个有
- `LatentUpscaleModelLoader` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `SimpleMathDual+` —— 3/7 个有
- `easy indexAnything` —— 3/7 个有
- `PreviewImage` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 24 | 24 - 24 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，7 个样本，取值集中（一致性 100%）
