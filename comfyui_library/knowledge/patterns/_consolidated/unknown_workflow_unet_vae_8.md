---
name: unknown_workflow_unet_vae_8
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.730364
common_nodes: [CLIPLoader, CreateVideo, MiniMaxH3Director, PreviewAny, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3_director_fl2v 参考生视频_2084823508688920578.json, 视频生成/图生视频/minimax_h3_director_fl2v_2094619431400988673.json, 视频生成/图生视频/minimax_h3_director_r2v 参考生视频_2084824118477811713.json, 视频生成/图生视频/minimax_h3_director_rv2v 参考改视频_2084824457453072386.json, 视频生成/图生视频/视频人物替换｜参考图换脸改衣_2089916752309350401.json, 视频生成/图生视频/（自用）MiniMax H3 导演台工作流（原作者：AI搅拌手）_2088301831494660097.json, 视频生成/文生视频/FZ-MinimaxH3-视频导演台（加速版）_2096847459136917505.json, 视频生成/文生视频/H3 全能导演台-T2V文生视频_2088249873417195521.json, 视频生成/文生视频/H3导演台_2103122205092700161.json, 视频生成/文生视频/MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313.json, 视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/minimax_h3_director_fl2v 参考生视频_2084823508688920578.json、视频生成/图生视频/minimax_h3_director_fl2v_2094619431400988673.json、视频生成/图生视频/minimax_h3_director_r2v 参考生视频_2084824118477811713.json、视频生成/图生视频/minimax_h3_director_rv2v 参考改视频_2084824457453072386.json、视频生成/图生视频/视频人物替换｜参考图换脸改衣_2089916752309350401.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `MiniMaxH3Director`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `BasicScheduler` —— 2/11 个有
- `MiniMaxH3DirectorRefine` —— 2/11 个有
- `BasicGuider` —— 1/11 个有
- `EasyCache` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `ModelAttentionBackend` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
