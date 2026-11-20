---
name: unknown_workflow_unet_vae_2
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.758833
common_nodes: [CLIPLoader, CreateVideo, MiniMaxH3Director, PreviewAny, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3_director_fl2v 参考生视频_2084823508688920578.json, 视频生成/图生视频/minimax_h3_director_fl2v_2094619431400988673.json, 视频生成/图生视频/minimax_h3_director_r2v 参考生视频_2084824118477811713.json, 视频生成/图生视频/minimax_h3_director_rv2v 参考改视频_2084824457453072386.json, 视频生成/图生视频/视频人物替换｜参考图换脸改衣_2089916752309350401.json, 视频生成/图生视频/（自用）MiniMax H3 导演台工作流（原作者：AI搅拌手）_2088301831494660097.json, 视频生成/文生视频/FZ-MinimaxH3-视频导演台（加速版）_2096847459136917505.json, 视频生成/文生视频/H3 全能导演台-T2V文生视频_2088249873417195521.json, 视频生成/文生视频/H3导演台_2103122205092700161.json, 视频生成/文生视频/MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2090104417038196737.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2094624733835907074.json, 视频生成/文生视频/MiniMax H3 电影级运镜全能导演台｜二采精修｜分镜合成｜加速版_2096009884130177025.json, 视频生成/文生视频/MiniMax H3 电影质感全能导演台｜二采放大｜分镜合成｜8步加速版_2100406933353226242.json, 视频生成/文生视频/MiniMax-H3_Director_导演台多参模式_2101083112175394817.json, 视频生成/文生视频/minimaxH3 全模态导演台-多参考图 x 多视频  x  多音频_2091642744618967042.json, 视频生成/文生视频/minimax_h3_director_二采+导演台_2089917916656525313.json, 视频生成/文生视频/让灵感，直接开拍｜MiniMax H3 导演台全能工作流_2099151043417432066.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/minimax_h3_director_fl2v 参考生视频_2084823508688920578.json、视频生成/图生视频/minimax_h3_director_fl2v_2094619431400988673.json、视频生成/图生视频/minimax_h3_director_r2v 参考生视频_2084824118477811713.json、视频生成/图生视频/minimax_h3_director_rv2v 参考改视频_2084824457453072386.json、视频生成/图生视频/视频人物替换｜参考图换脸改衣_2089916752309350401.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `MiniMaxH3Director`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/18 个有
- `PathchSageAttentionKJ` —— 14/18 个有
- `LoraLoaderModelOnly` —— 10/18 个有
- `MiniMaxH3DirectorRefine` —— 9/18 个有
- `UpscaleModelLoader` —— 7/18 个有
- `BasicScheduler` —— 4/18 个有
- `PreviewImage` —— 2/18 个有
- `BasicGuider` —— 1/18 个有
- `EmptyImage` —— 1/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `LoadImage` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
