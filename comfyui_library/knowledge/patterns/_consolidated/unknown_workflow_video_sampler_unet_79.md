---
name: unknown_workflow_video_sampler_unet_79
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8205
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 文生视频  提示词自动优化版_2084674314833580034.json, 视频生成/文生视频/MiniMaxH3图生视频工作流 By 像素幻想Lab_2093254151970058242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_79

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 文生视频  提示词自动优化版_2084674314833580034.json、视频生成/文生视频/MiniMaxH3图生视频工作流 By 像素幻想Lab_2093254151970058242.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JWFloatToString` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
