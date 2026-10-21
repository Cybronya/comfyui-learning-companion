---
name: unknown_workflow_video_lora_sampler_468
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85925
common_nodes: [BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAudio, ResolutionSelector, SelfLiftAvatarH3Sampler, SelfLiftAvatarH3TST, SetLatentNoiseMask, SolidMask, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/Minimax H3  音频驱动数字人-神态口型自然-双采加速_2111647737732231170.json, 视频生成/图生视频/高阶双采加速不降质音频驱动数字人-视频工作流 MiniMax H3新技术_2101122144590712834.json, 视频生成/图生视频/高阶双采加速不降质音频驱动数字人-视频工作流+MiniMax+H3新技术_2111456170199310337.json, 视频生成/图生视频/高阶双采音色克隆台词驱动数字人- MiniMax H3视频工作流_2110580224256724993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_468

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/Minimax H3  音频驱动数字人-神态口型自然-双采加速_2111647737732231170.json、视频生成/图生视频/高阶双采加速不降质音频驱动数字人-视频工作流 MiniMax H3新技术_2101122144590712834.json、视频生成/图生视频/高阶双采加速不降质音频驱动数字人-视频工作流+MiniMax+H3新技术_2111456170199310337.json、视频生成/图生视频/高阶双采音色克隆台词驱动数字人- MiniMax H3视频工作流_2110580224256724993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `ConditioningZeroOut`
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
- `PreviewAudio`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SelfLiftAvatarH3TST`
- `SetLatentNoiseMask`
- `SolidMask`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `Int` —— 3/4 个有
- `MelBandRoFormerModelLoader` —— 3/4 个有
- `MelBandRoFormerSampler` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `TrimAudioDuration` —— 3/4 个有
- `Label (rgthree)` —— 2/4 个有
- `Qwen3ASRLoader` —— 2/4 个有
- `Qwen3ASRTranscribe` —— 2/4 个有
- `RunningHub_VoxCPM_Generate` —— 2/4 个有
- `RunningHub_VoxCPM_LoadModel` —— 2/4 个有
- `SaveAudioMP3` —— 1/4 个有
- `Seed` —— 1/4 个有
- `XB_CanvasLabel` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
