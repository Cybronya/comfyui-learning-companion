---
name: unknown_workflow_video_upscale_latent_upscale_123
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.934
common_nodes: [AudioCrop, BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, CreateVideo, Float, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, ManualSigmas, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LatentUpscaleBy32T8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3PromptEnhancerT8, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SolAttnMiniMax, SoundFlow_GetLength, StringConcatenate, T8PerformanceDirectorConfig, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_Generate, T8_IndexTTS25_ModelLoader, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/1013-2MiniMax H3数字人加速版V1_2109806190858424321.json, 视频生成/图生视频/MiniMax H3数字人加速版V1_2109292172842455042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_123

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/1013-2MiniMax H3数字人加速版V1_2109806190858424321.json、视频生成/图生视频/MiniMax H3数字人加速版V1_2109292172842455042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `Float`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `ManualSigmas`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LatentUpscaleBy32T8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3PromptEnhancerT8`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SolAttnMiniMax`
- `SoundFlow_GetLength`
- `StringConcatenate`
- `T8PerformanceDirectorConfig`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_ModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 1/2 个有
- `T8_BreezeTTS_CloneRequest` —— 1/2 个有
- `T8_BreezeTTS_Generate` —— 1/2 个有
- `T8_BreezeTTS_GenerationSettings` —— 1/2 个有
- `T8_BreezeTTS_ModelLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
