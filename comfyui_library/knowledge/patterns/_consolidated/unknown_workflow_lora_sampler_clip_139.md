---
name: unknown_workflow_lora_sampler_clip_139
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.646667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSize, LTXAVTextEncoderLoader, LTXVAddGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SamplerEulerAncestral, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2064603463413223426.json, 视频生成/文生视频/四步引导+首尾帧ltx2_3_style_transition+全节点注释_2057837235214577666.json, 视频生成/文生视频/首尾帧ltx2_3_style_transition+全节点注释_2055806950063001602.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_139

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2064603463413223426.json、视频生成/文生视频/四步引导+首尾帧ltx2_3_style_transition+全节点注释_2057837235214577666.json、视频生成/文生视频/首尾帧ltx2_3_style_transition+全节点注释_2055806950063001602.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 2/3 个有
- `CreateVideo` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 201 | 3 | 63% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 201，3 个样本
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
