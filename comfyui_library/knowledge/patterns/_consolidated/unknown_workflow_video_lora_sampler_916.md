---
name: unknown_workflow_video_lora_sampler_916
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.41
common_nodes: [AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, DapaoH3LocalPromptNode, Fast Groups Bypasser (rgthree), GetNode, H3SigmaRefiner, Int, Int2String, JjkShowText, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, PrimitiveString, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, Text, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, 孤海注释]
problems: []
missing: []
members: [视频生成/文生视频/10Eros Max BETA5 workflow_2097951550932082690.json, 视频生成/文生视频/MiniMax H3多参全能整合工作流V2_2090358738145333250.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_916

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/10Eros Max BETA5 workflow_2097951550932082690.json、视频生成/文生视频/MiniMax H3多参全能整合工作流V2_2090358738145333250.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `DapaoH3LocalPromptNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `H3SigmaRefiner`
- `Int`
- `Int2String`
- `JjkShowText`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `PrimitiveString`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
