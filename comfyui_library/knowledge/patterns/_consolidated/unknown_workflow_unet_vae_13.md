---
name: unknown_workflow_unet_vae_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6515
common_nodes: [CLIPLoader, CreateVideo, MiniMaxH3Director, PreviewAny, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/夜樱馆_导演台6合1_加速版_2099536983994486785.json, 视频生成/文生视频/方格智联-MINIH3-工作台_2086704664422207489.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/夜樱馆_导演台6合1_加速版_2099536983994486785.json、视频生成/文生视频/方格智联-MINIH3-工作台_2086704664422207489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

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
- `MiniMaxH3SLADynamicLoRABypassV2T8Advanced` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
