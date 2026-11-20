---
name: unknown_workflow_video_lora_sampler_1051
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6135
common_nodes: [AudioCrop, BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetNode, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SetNode, SolidMask, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 sigma强化+Selflift双采去油小脸不崩口型同步数字人MV无限分段加速_1953029627158720514.json, 视频生成/图生视频/【阿良绘】H3数字人（语音克隆+自动提词+自动时长）_2100796156698775554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1051

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 sigma强化+Selflift双采去油小脸不崩口型同步数字人MV无限分段加速_1953029627158720514.json、视频生成/图生视频/【阿良绘】H3数字人（语音克隆+自动提词+自动时长）_2100796156698775554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ComfyNumberConvert` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/2 个有
- `RunningHub_VoxCPM_MultiSpeaker` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `YUAN_TXTConvertAny` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
