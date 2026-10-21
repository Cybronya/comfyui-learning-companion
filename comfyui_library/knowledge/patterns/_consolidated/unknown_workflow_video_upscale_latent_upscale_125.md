---
name: unknown_workflow_video_upscale_latent_upscale_125
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8655
common_nodes: [Anything Everywhere, Audio Duration (mtb), AudioSeparation, CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptyLTXVLatentVideo, Float, GetNode, KSampler, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: BooleanOperatorV2, LayerUtility: If , LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, SetLatentNoiseMask, SetNode, SolidMask, Text Multiline, TrimAudioDuration, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [数字人/数字人/LTX2.3数字人_2085739699964039169.json, 数字人/数字人/数字人LTX-2.3_2090689345052299266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_125

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/LTX2.3数字人_2085739699964039169.json、数字人/数字人/数字人LTX-2.3_2090689345052299266.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Audio Duration (mtb)`
- `AudioSeparation`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Float`
- `GetNode`
- `KSampler`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: If `
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `Text Multiline`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Audio Resample (mtb)` —— 1/2 个有
- `AudioCombine` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LTXVAudioVAEDecode` —— 1/2 个有
- `NormalizeAudioLoudness` —— 1/2 个有
- `TTResolutionSelector` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | heun | - | 2 | 100% |
| 调度器 | linear_quadratic | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，2 个样本，一致性 100%
- 调度器 最常用 linear_quadratic，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
