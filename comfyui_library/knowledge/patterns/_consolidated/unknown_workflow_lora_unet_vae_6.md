---
name: unknown_workflow_lora_unet_vae_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8835
common_nodes: [BasicScheduler, CLIPLoader, CreateVideo, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PathchSageAttentionKJ, PreviewAny, SaveVideo, SolAttnMiniMax, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/（加速）MiniMax H3 导演台全能工作流_2090880598213750786.json, 视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/（加速）MiniMax H3 导演台全能工作流_2090880598213750786.json、视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SaveVideo`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 1/2 个有
- `LoraLoaderBypassModelOnly` —— 1/2 个有
- `MiniMaxH3BlockCacheT8` —— 1/2 个有
- `MiniMaxH3HybridLoader` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
