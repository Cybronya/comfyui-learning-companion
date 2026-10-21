---
name: unknown_workflow_lora_sampler_unet_98
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.549
common_nodes: [AudioCrop, BasicScheduler, CFGGuider, CR Prompt Text, CR Text, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), GetNode, KSamplerSelect, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoadAudio, LoadImage, LongCatVoiceCloneTTS, LoraLoaderModelOnly, NormalizeAudioLoudness, PreviewAny, PreviewAudio, Qwen3ASRLoader, Qwen3ASRTranscribe, RH_LLMAPI_Pro_Node, RH_RhartImageG2ImageToImage, RH_RhartImageG2TextToImage, RandomNoise, SamplerCustomAdvanced, SaveAudioMP3, SaveImage, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2062416629836894209.json, 视频生成/图生视频/2062170832935411714.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_98

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2062416629836894209.json、视频生成/图生视频/2062170832935411714.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `BasicScheduler`
- `CFGGuider`
- `CR Prompt Text`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LongCatVoiceCloneTTS`
- `LoraLoaderModelOnly`
- `NormalizeAudioLoudness`
- `PreviewAny`
- `PreviewAudio`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2TextToImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveAudioMP3`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CS-LTXGridDirector` —— 1/2 个有
- `CS-LTXSixGridDirector` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `LTX2SamplingPreviewOverride` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `TTResolutionSelector` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
