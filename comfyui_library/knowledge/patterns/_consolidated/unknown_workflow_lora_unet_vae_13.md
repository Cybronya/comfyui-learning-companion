---
name: unknown_workflow_lora_unet_vae_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.912
common_nodes: [CLIPLoader, CreateVideo, LoraLoaderModelOnly, MiniMaxH3Director, PathchSageAttentionKJ, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 导演台-文生视频 图生视频 首尾帧生视频 视频转视频 参考素材转视频_2088428364578250753.json, 视频生成/文生视频/【开源】Minimax_H3 导演台参考生长视频_2089264892179206146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 导演台-文生视频 图生视频 首尾帧生视频 视频转视频 参考素材转视频_2088428364578250753.json、视频生成/文生视频/【开源】Minimax_H3 导演台参考生长视频_2089264892179206146.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Model Input Switch` —— 1/2 个有
- `EasyCache` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `SolAttnPatch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
