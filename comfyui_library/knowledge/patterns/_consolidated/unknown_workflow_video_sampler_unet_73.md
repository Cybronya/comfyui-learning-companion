---
name: unknown_workflow_video_sampler_unet_73
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6575
common_nodes: [AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/MiniMax h3音频驱动数字人对口型-自动写提示词+全节点注释_2089689798725423105.json, 数字人/数字人/MinimaxH3音频驱动+语音克隆_2086995655117070338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_73

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/MiniMax h3音频驱动数字人对口型-自动写提示词+全节点注释_2089689798725423105.json、数字人/数字人/MinimaxH3音频驱动+语音克隆_2086995655117070338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `AudioBeforeAfterSilence` —— 1/2 个有
- `AudioConcat` —— 1/2 个有
- `EmptyAudio` —— 1/2 个有
- `HeartMuLa_Transcribe` —— 1/2 个有
- `JoinStringMulti` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `Qwen3TTSModelLoader` —— 1/2 个有
- `Qwen3TTSVoiceClone` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `ToString` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
