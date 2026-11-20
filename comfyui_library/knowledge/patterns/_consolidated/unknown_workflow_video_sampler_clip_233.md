---
name: unknown_workflow_video_sampler_clip_233
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7575
common_nodes: [1hew_AudioDuration, CFGGuider, CLIPTextEncode, CR Prompt Text, CustomSigmas, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, Float, GetNode, JWInteger, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MathExpression|pysssss, PathchSageAttentionKJ, PreviewAudio, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3 AI2V数字人工作流(双人_多人支持)_2031018087641784321.json, 视频生成/图生视频/LTX-2.3 AI2V数字人工作流_2030889202761601025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_233

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3 AI2V数字人工作流(双人_多人支持)_2031018087641784321.json、视频生成/图生视频/LTX-2.3 AI2V数字人工作流_2030889202761601025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `1hew_AudioDuration`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CustomSigmas`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Float`
- `GetNode`
- `JWInteger`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTX2SamplingPreviewOverride` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
