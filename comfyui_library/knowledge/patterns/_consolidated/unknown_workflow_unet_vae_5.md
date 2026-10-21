---
name: unknown_workflow_unet_vae_5
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.716857
common_nodes: [CLIPLoader, CreateVideo, MiniMaxH3Director, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3_director_fl2v 参考生视频_2084823508688920578.json, 视频生成/图生视频/minimax_h3_director_fl2v_2094619431400988673.json, 视频生成/图生视频/minimax_h3_director_r2v 参考生视频_2084824118477811713.json, 视频生成/图生视频/minimax_h3_director_rv2v 参考改视频_2084824457453072386.json, 视频生成/文生视频/MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313.json, 视频生成/文生视频/MiniMax H3 Director 全能导演台_2093465779391000578.json, 视频生成/文生视频/MiniMax H3 导演台-文生视频 图生视频 首尾帧生视频 视频转视频 参考素材转视频_2088428364578250753.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/minimax_h3_director_fl2v 参考生视频_2084823508688920578.json、视频生成/图生视频/minimax_h3_director_fl2v_2094619431400988673.json、视频生成/图生视频/minimax_h3_director_r2v 参考生视频_2084824118477811713.json、视频生成/图生视频/minimax_h3_director_rv2v 参考改视频_2084824457453072386.json、视频生成/文生视频/MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `MiniMaxH3Director`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 6/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `CR Model Input Switch` —— 1/7 个有
- `EasyCache` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
