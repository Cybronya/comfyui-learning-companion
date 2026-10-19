---
name: unknown_workflow_unet_vae_4
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9406
common_nodes: [CLIPLoader, CreateVideo, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SaveImage, SaveVideo, SolAttnMiniMax, UNETLoader, VAELoader, easy imageChooser, kkVideoFirstLastFrames]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 导演台全能+二采样工作流_2091194471978463234.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流_2090482445757014017.json, 视频生成/图生视频/Reminx+Fast Minmax H3导演台-变身904_2095546990494044162.json, 视频生成/图生视频/导演台Sigmas设置-901_2094793386204160002.json, 视频生成/图生视频/导演台高质量产出903-40s 1200RH币_2094957121136840706.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 导演台全能+二采样工作流_2091194471978463234.json、视频生成/图生视频/MiniMax H3 导演台全能工作流_2090482445757014017.json、视频生成/图生视频/Reminx+Fast Minmax H3导演台-变身904_2095546990494044162.json、视频生成/图生视频/导演台Sigmas设置-901_2094793386204160002.json、视频生成/图生视频/导演台高质量产出903-40s 1200RH币_2094957121136840706.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SaveImage`
- `SaveVideo`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `easy imageChooser`
- `kkVideoFirstLastFrames`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 4/5 个有
- `MiniMaxH3Director` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PlaySound|pysssss` —— 3/5 个有
- `H3SigmaRefiner` —— 2/5 个有
- `Lora Loader Stack (rgthree)` —— 2/5 个有
- `SplitSigmas` —— 2/5 个有
- `ComfyMiniMaxH3Director` —— 1/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
