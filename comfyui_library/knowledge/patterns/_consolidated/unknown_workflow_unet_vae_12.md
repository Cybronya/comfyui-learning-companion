---
name: unknown_workflow_unet_vae_12
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7555
common_nodes: [CLIPLoader, CreateVideo, MiniMaxH3Director, PreviewAny, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-H3 文本生视频turbo加速_2086689208969818114.json, 视频生成/文生视频/MiniMax导演台全能工作流_2098064353835700225.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax-H3 文本生视频turbo加速_2086689208969818114.json、视频生成/文生视频/MiniMax导演台全能工作流_2098064353835700225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `MiniMaxH3Director`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MiniMaxH3BlockCacheT8` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
