---
name: unknown_workflow_lora_sampler_clip_322
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.823
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, CreateVideo, ImageBatch, ImageFromBatch, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, WanInfiniteTalkToVideo]
problems: []
missing: []
members: [音频生成/音频生成/用InfiniteTalk + Qwen3-TTS 对口型，一键生成MOSS给刘培强庆生视频！_2018671065148432385.json, 音频生成/音频生成/🐸InfiniteTalk单人对口型 官方版🐸_2019601283992264705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_322

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/用InfiniteTalk + Qwen3-TTS 对口型，一键生成MOSS给刘培强庆生视频！_2018671065148432385.json、音频生成/音频生成/🐸InfiniteTalk单人对口型 官方版🐸_2019601283992264705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `CreateVideo`
- `ImageBatch`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanInfiniteTalkToVideo`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `DapaoImageAspectRatioResizeNode` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `Qwen3TTSModelLoader` —— 1/2 个有
- `Qwen3TTSVoiceClone` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
