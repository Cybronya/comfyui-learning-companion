---
name: unknown_workflow_video_lora_sampler_746
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.816
common_nodes: [AudioConcat, AudioEncoderEncode, AudioEncoderLoader, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetAudioDurationFromAudio, HeartMuLa_Transcribe, ImageBatch, ImageResizeKJv2, JWStringGetLine, JWStringSplit, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MaskToImage, MathExpression|pysssss, ModelPatchLoader, PreviewImage, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, RandomNoise, SAM3Segment, SamplerCustomAdvanced, TextBox, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRAM_Debug, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Infinite Talk双人数字人+Qwen3 TTS语音克隆_2039012816979496962.json, 音频生成/音频生成/Infinite Talk双人数字人+Qwen3 TTS语音设计_2035955658540978178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_746

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Infinite Talk双人数字人+Qwen3 TTS语音克隆_2039012816979496962.json、音频生成/音频生成/Infinite Talk双人数字人+Qwen3 TTS语音设计_2035955658540978178.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetAudioDurationFromAudio`
- `HeartMuLa_Transcribe`
- `ImageBatch`
- `ImageResizeKJv2`
- `JWStringGetLine`
- `JWStringSplit`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PreviewImage`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `RandomNoise`
- `SAM3Segment`
- `SamplerCustomAdvanced`
- `TextBox`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 1/2 个有
- `TDQwen3TTSVoiceDesign` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
