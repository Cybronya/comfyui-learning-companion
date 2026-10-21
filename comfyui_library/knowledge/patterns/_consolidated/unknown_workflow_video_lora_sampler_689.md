---
name: unknown_workflow_video_lora_sampler_689
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.401333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, DapaoH3LocalPromptNode, Fast Groups Bypasser (rgthree), GetNode, Int, Int2String, JjkShowText, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveString, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, Text, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, 孤海注释]
problems: []
missing: []
members: [视频生成/文生视频/10Eros Max BETA5 workflow_2097951550932082690.json, 视频生成/文生视频/MiniMax H3多参全能整合工作流V2_2090358738145333250.json, 视频生成/文生视频/MiniMax+H3多参全能整合工作流_2090073717442441217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_689

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/10Eros Max BETA5 workflow_2097951550932082690.json、视频生成/文生视频/MiniMax H3多参全能整合工作流V2_2090358738145333250.json、视频生成/文生视频/MiniMax+H3多参全能整合工作流_2090073717442441217.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：40%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `DapaoH3LocalPromptNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
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
- `PrimitiveString`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/3 个有
- `H3SigmaRefiner` —— 2/3 个有
- `MiniMaxH3SigmaShift` —— 2/3 个有
- `MiniMaxLowVRAMAttention` —— 2/3 个有
- `ModelPreviewOverrideKJ` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LTXVConcatAVLatent` —— 1/3 个有
- `LTXVSeparateAVLatent` —— 1/3 个有
- `MinimaxH3LatentUpscaler3D` —— 1/3 个有
- `PT_H3ConcatAVLatent` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `VAEDecodeAudio` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VAEEncodeAudio` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
