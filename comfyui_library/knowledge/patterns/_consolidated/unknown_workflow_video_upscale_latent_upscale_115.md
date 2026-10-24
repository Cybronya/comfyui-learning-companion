---
name: unknown_workflow_video_upscale_latent_upscale_115
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.477
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PreviewImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 单图单音频动画工作流_2094569760485892098.json, 视频生成/图生视频/minimax 影视剧 多参工作流 高清 运动不模糊_2088628741688877058.json, 视频生成/图生视频/兼具质量和速度的数字人_2089306091665580034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_115

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/minimax H3 单图单音频动画工作流_2094569760485892098.json、视频生成/图生视频/minimax 影视剧 多参工作流 高清 运动不模糊_2088628741688877058.json、视频生成/图生视频/兼具质量和速度的数字人_2089306091665580034.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/3 个有
- `LoraLoaderBypassModelOnly` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `VAEDecodeAudio` —— 2/3 个有
- `easy ab` —— 2/3 个有
- `HeartMuLa_Transcribe` —— 1/3 个有
- `MelBandRoFormerModelLoader` —— 1/3 个有
- `MelBandRoFormerSampler` —— 1/3 个有
- `MiniMaxH3HybridLoader` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `SoundFlow_GetLength` —— 1/3 个有
- `TTP_text_mix` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VRGDG_AudioCrop` —— 1/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
