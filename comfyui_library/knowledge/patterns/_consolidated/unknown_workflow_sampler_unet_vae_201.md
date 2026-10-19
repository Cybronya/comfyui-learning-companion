---
name: unknown_workflow_sampler_unet_vae_201
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8305
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, MiniMaxChunkFeedForward, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, ShowText|pysssss, UNETLoader, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 开源版 文生视频 首尾帧视频 多模态视频生成 3合1集合工作流_2084939564103331841.json, 视频生成/文生视频/MiniMax H3 海螺模型 9种SKILL视频生成工作流_2087576840822157313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_201

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 开源版 文生视频 首尾帧视频 多模态视频生成 3合1集合工作流_2084939564103331841.json、视频生成/文生视频/MiniMax H3 海螺模型 9种SKILL视频生成工作流_2087576840822157313.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `UNETLoader`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `Fast Muter (rgthree)` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `PixaromaLabel` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
