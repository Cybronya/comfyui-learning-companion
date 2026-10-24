---
name: unknown_workflow_lora_unet_vae_8
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.874667
common_nodes: [BasicScheduler, CLIPLoader, CreateVideo, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, PreviewAny, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/（加速）MiniMax H3 导演台全能工作流_2090880598213750786.json, 视频生成/文生视频/H3导演台_2103122205092700161.json, 视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/（加速）MiniMax H3 导演台全能工作流_2090880598213750786.json、视频生成/文生视频/H3导演台_2103122205092700161.json、视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 2/3 个有
- `SolAttnMiniMax` —— 2/3 个有
- `EasyCache` —— 1/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有
- `MiniMaxH3BlockCacheT8` —— 1/3 个有
- `MiniMaxH3HybridLoader` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
