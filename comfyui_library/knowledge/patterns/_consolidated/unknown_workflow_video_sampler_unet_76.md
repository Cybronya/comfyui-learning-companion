---
name: unknown_workflow_video_sampler_unet_76
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.817
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 文生视频  提示词自动优化版_2084674314833580034.json, 视频生成/文生视频/MiniMaxH3图生视频工作流 By 像素幻想Lab_2093254151970058242.json, 视频生成/文生视频/MiniMaxH3文生视频工作流 By 像素幻想Lab_2087128147237105666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_76

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 文生视频  提示词自动优化版_2084674314833580034.json、视频生成/文生视频/MiniMaxH3图生视频工作流 By 像素幻想Lab_2093254151970058242.json、视频生成/文生视频/MiniMaxH3文生视频工作流 By 像素幻想Lab_2087128147237105666.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `JWFloatToString` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
