---
name: unknown_workflow_lora_sampler_checkpoint_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.983
common_nodes: [CFGGuider, CheckpointLoaderSimple, ConditioningZeroOut, CreateVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled, VAELoaderKJ, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2064954613949886465.json, 视频生成/图生视频/2056272610891227137.json, 视频生成/图生视频/2057746305258188801.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2064954613949886465.json、视频生成/图生视频/2056272610891227137.json、视频生成/图生视频/2057746305258188801.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `CreateVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `FB_Qwen3TTSCustomVoice` —— 2/3 个有
- `FB_Qwen3TTSVoiceClone` —— 2/3 个有
- `FB_Qwen3TTSVoiceDesign` —— 2/3 个有
- `LTXAVTextEncoderLoader` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `Qwen3ASRLoader_DFT` —— 2/3 个有
- `Qwen3ASRTranscribe_DFT` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `ReservedVRAMSetter` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
