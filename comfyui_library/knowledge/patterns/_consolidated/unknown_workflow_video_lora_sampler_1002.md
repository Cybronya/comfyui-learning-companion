---
name: unknown_workflow_video_lora_sampler_1002
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5155
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, FL_Audio_BPM_Analyzer, FL_Audio_Drum_Detector, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, JWFloatToString, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadAudioUI, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PT_H3ConcatAVLatent, PreviewAny, PreviewImage, PrimitiveFloat, Qwen3ASRLoader_DFT, Qwen3ASRTranscribe_DFT, RHLLMChatNode, RandomNoise, ResolutionSelector, RunningHub Deepcleaner, SamplerCustomAdvanced, SetNode, Text, TextCombinerSix, TextCombinerTwo, UNETLoader, VAEDecode, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [视频生成/文生视频/Fenglairh-MiniMax H3完整工作流集合最新加速-官方版_2087770654929145857.json, 视频生成/文生视频/Fenglairh-MiniMax H3完整工作流集合最新加速-官方版_2089022849863471105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1002

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Fenglairh-MiniMax H3完整工作流集合最新加速-官方版_2087770654929145857.json、视频生成/文生视频/Fenglairh-MiniMax H3完整工作流集合最新加速-官方版_2089022849863471105.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `FL_Audio_BPM_Analyzer`
- `FL_Audio_Drum_Detector`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `JWFloatToString`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadAudioUI`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PT_H3ConcatAVLatent`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3ASRLoader_DFT`
- `Qwen3ASRTranscribe_DFT`
- `RHLLMChatNode`
- `RandomNoise`
- `ResolutionSelector`
- `RunningHub Deepcleaner`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text`
- `TextCombinerSix`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `HAIGC_VideoLastFrame` —— 1/2 个有
- `PixaromaGroupSwitch` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
