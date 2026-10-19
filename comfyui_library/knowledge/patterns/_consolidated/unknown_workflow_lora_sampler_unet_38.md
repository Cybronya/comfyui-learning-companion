---
name: unknown_workflow_lora_sampler_unet_38
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95075
common_nodes: [AudioConcat, BasicScheduler, BatchImagesNode, CLIPLoader, ComfyMathExpression, ComfySwitchNode, ConditioningZeroOut, CreateVideo, Float, GetImageRangeFromBatch, Int, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, ResolutionSelector, SaveVideo, SetLatentNoiseMask, SolidMask, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3无限时长极速音频驱动数字人1013_2109675064579936258.json, 视频生成/图生视频/MiniMax_H3无限时长极速音频驱动数字人1015_2110201843593867266.json, 视频生成/图生视频/MiniMax_H3无限时长极速音频驱动数字人_2101231106522697729.json, 视频生成/数字人/MiniMax_H3无限时长极速音频驱动数字人_2101231106522697729.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_38

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3无限时长极速音频驱动数字人1013_2109675064579936258.json、视频生成/图生视频/MiniMax_H3无限时长极速音频驱动数字人1015_2110201843593867266.json、视频生成/图生视频/MiniMax_H3无限时长极速音频驱动数字人_2101231106522697729.json、视频生成/数字人/MiniMax_H3无限时长极速音频驱动数字人_2101231106522697729.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioConcat`
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `CreateVideo`
- `Float`
- `GetImageRangeFromBatch`
- `Int`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3BlockCacheT8` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `RIFE VFI` —— 3/4 个有
- `BasicGuider` —— 2/4 个有
- `BlockSparseAttention` —— 2/4 个有
- `ExtendIntermediateSigmas` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `RandomNoise` —— 2/4 个有
- `SamplerCustomAdvanced` —— 2/4 个有
- `SelfLiftAvatarH3Sampler` —— 2/4 个有
- `AudioCrop` —— 1/4 个有
- `MiniMaxH3Unified` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `SaveAudioAdvanced` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
