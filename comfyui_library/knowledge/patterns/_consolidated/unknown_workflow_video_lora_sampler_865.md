---
name: unknown_workflow_video_lora_sampler_865
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CRTFirstLastFrameSelector, ConditioningZeroOut, Float, Getter, Int, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PreviewAudio, PreviewImage, Qwen3TTSModelLoader, RandomNoise, SamplerCustomAdvanced, Setter, SimpleMath+, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2040280794584846338.json, 视频生成/图生视频/2041800197050732545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_865

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2040280794584846338.json、视频生成/图生视频/2041800197050732545.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CRTFirstLastFrameSelector`
- `ConditioningZeroOut`
- `Float`
- `Getter`
- `Int`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewAudio`
- `PreviewImage`
- `Qwen3TTSModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Setter`
- `SimpleMath+`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `1hew_AnySwitchBool` —— 1/2 个有
- `ASRMW` —— 1/2 个有
- `AudioConcat` —— 1/2 个有
- `AudioEvenSplitNode` —— 1/2 个有
- `AudioMerge` —— 1/2 个有
- `AudioSelectNode` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `EmptyAudio` —— 1/2 个有
- `GetAudioDurationFromAudio` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PainterVRAM` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `Qwen3TTSVoiceClone` —— 1/2 个有
- `Qwen3TTSVoiceDesign` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `VRAMReserver` —— 1/2 个有
- `easy promptLine` —— 1/2 个有
- `图像缩放V2_孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
