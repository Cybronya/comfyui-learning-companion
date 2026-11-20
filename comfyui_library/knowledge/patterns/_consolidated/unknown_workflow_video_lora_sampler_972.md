---
name: unknown_workflow_video_lora_sampler_972
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.848
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLTXVLatentVideo, GetImageRangeFromBatch, ImageResizeKJv2, KSamplerSelect, LTXICLoRALoaderModelOnly, LTXVAddGuideMulti, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, ManualSigmas, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, SimpleMath+, StringConcatenate, TextGenerate, VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/LTX2.3-edit anything-视频编辑替换、移除、添加及风格转绘_2054591636344197121.json, 平台全量/LTX2.3-edit+anything-视频编辑替换、移除、添加及风格转绘_2061465033829339138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_972

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX2.3-edit anything-视频编辑替换、移除、添加及风格转绘_2054591636344197121.json、平台全量/LTX2.3-edit+anything-视频编辑替换、移除、添加及风格转绘_2061465033829339138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXICLoRALoaderModelOnly`
- `LTXVAddGuideMulti`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `SimpleMath+`
- `StringConcatenate`
- `TextGenerate`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有
- `LTXVAudioVAELoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoaderKJ` —— 1/2 个有

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
