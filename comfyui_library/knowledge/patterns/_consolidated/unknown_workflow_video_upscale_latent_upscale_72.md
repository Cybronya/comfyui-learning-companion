---
name: unknown_workflow_video_upscale_latent_upscale_72
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8602
common_nodes: [Anything Everywhere, Audio Duration (mtb), CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSampler, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, SetLatentNoiseMask, SetNode, SolidMask, Text Multiline, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [数字人/数字人/LTX2.3数字人_2085739699964039169.json, 数字人/数字人/双人数字人LTX2.3(效果很ok)_2062103431044751362.json, 数字人/数字人/数字人LTX-2.3_2062111475262640130.json, 数字人/数字人/数字人LTX-2.3_2079746159542882305.json, 数字人/数字人/数字人LTX-2.3_2090689345052299266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_72

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/LTX2.3数字人_2085739699964039169.json、数字人/数字人/双人数字人LTX2.3(效果很ok)_2062103431044751362.json、数字人/数字人/数字人LTX-2.3_2062111475262640130.json、数字人/数字人/数字人LTX-2.3_2079746159542882305.json、数字人/数字人/数字人LTX-2.3_2090689345052299266.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `Audio Duration (mtb)`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
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
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 4/5 个有
- `Float` —— 4/5 个有
- `LTXVAudioVAEDecode` —— 4/5 个有
- `LayerUtility: BooleanOperatorV2` —— 4/5 个有
- `LayerUtility: If ` —— 4/5 个有
- `NormalizeAudioLoudness` —— 4/5 个有
- `TrimAudioDuration` —— 4/5 个有
- `Audio Resample (mtb)` —— 3/5 个有
- `AudioCombine` —— 3/5 个有
- `AudioConcat` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | heun | - | 5 | 80% |
| 调度器 | linear_quadratic | - | 5 | 80% |
| 重绘幅度 | 1 | 0.4 - 1 | 5 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，5 个样本，一致性 80%
- 调度器 最常用 linear_quadratic，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，5 个样本
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
