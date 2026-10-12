---
key: 视频生成/图生视频/Minimax H3 sigma强化+Selflift双采去油小脸不崩口型同步数字人MV无限分段加速_1953029627158720514.json
name: Minimax H3 sigma强化+Selflift双采去油小脸不崩口型同步数字人MV无限分段加速_1953029627158720514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3 sigma强化+Selflift双采去油小脸不崩口型同步数字人MV无限分段加速_1953029627158720514.json
hash: ddb2cafd0afe751a
coverage: 0.411111
learned_at: 2026-10-12 21:05:48
nodes: [MiniMaxChunkFeedForward, LTXVConcatAVLatent, LTXVSeparateAVLatent, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelAttentionBackend, SetNode, GetNode, SetNode, CLIPLoader, SetNode, GetNode, VAELoader, GetNode, SetNode, MiniMaxLowVRAMAttention, GetNode, UNETLoader, VAELoader, SetLatentNoiseMask, SetNode, SetNode, ModelPreviewOverrideKJ, LoadImage, GetNode, GetNode, easy showAnything, SolidMask, ComfyMathExpression, ComfyNumberConvert, GetNode, GetNode, SoundFlow_GetLength, GetNode, LTXVSeparateAVLatent, VAEDecode, ComfyMathExpression, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, SetNode, LoadImage, GetNode, SetNode, LoadImage, LoadImage, SetNode, MarkdownNote, KSamplerSelect, BasicScheduler, H3SigmaRefiner, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, Text Concatenate, GetNode, SetNode, GetNode, GetNode, LTXVAudioVAEEncode, GetNode, SetNode, MarkdownNote, MarkdownNote, GetNode, SelfLiftAvatarH3Sampler, SetNode, JjkText, SetNode, GetNode, easy cleanGpuUsed, MiniMaxH3ReferenceToVideo, GetImageRangeFromBatch, LayerUtility: PurgeVRAM V2, LoadAudio, ResolutionSelector, GetNode, easy seed, VHS_VideoCombine, JjkText, JjkText, AudioCrop]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, Text Concatenate, easy cleanGpuUsed, easy seed]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/图生视频/Minimax H3 sigma强化+Selflift双采去油小脸不崩口型同步数字人MV无限分段加速_1953029627158720514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3 sigma强化+Selflift双采去油小脸不崩口型同步数字人MV无限分段加速_1953029627158720514.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（90 个）：
- `MiniMaxChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `VAELoader`
- `GetNode`
- `SetNode`
- `MiniMaxLowVRAMAttention`
- `GetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `SetLatentNoiseMask`
- `SetNode`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `LoadImage`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `SolidMask`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `GetNode`
- `GetNode`
- `SoundFlow_GetLength`
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `H3SigmaRefiner`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Text Concatenate`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `GetNode`
- `SelfLiftAvatarH3Sampler` ★核心
- `SetNode`
- `JjkText`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `MiniMaxH3ReferenceToVideo`
- `GetImageRangeFromBatch`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `ResolutionSelector`
- `GetNode`
- `easy seed`
- `VHS_VideoCombine`
- `JjkText`
- `JjkText`
- `AudioCrop`

## 知识

覆盖率 **41%**（37/90）

**有卡**：`MiniMaxChunkFeedForward`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`CLIPLoader`、`VAELoader`、`MiniMaxLowVRAMAttention`、`UNETLoader`、`SetLatentNoiseMask`、`ModelPreviewOverrideKJ`、`LoadImage`、`SolidMask`、`ComfyMathExpression`、`ComfyNumberConvert`、`SoundFlow_GetLength`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`H3SigmaRefiner`、`LTXVAudioVAEEncode`、`SelfLiftAvatarH3Sampler`、`MiniMaxH3ReferenceToVideo`、`GetImageRangeFromBatch`、`LoadAudio`、`ResolutionSelector`、`VHS_VideoCombine`、`AudioCrop`

**缺卡**（8）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`Text Concatenate`、`easy cleanGpuUsed`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
