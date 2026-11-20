---
name: unknown_workflow_unet_vae
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.774154
common_nodes: [CLIPLoader, CreateVideo, MiniMaxH3Director, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [平台全量/minimax_h3_director_rv2v_2094601858668122113.json, 平台全量/minimax_h3_director_v2v 视频编辑_2084824665377300481.json, 平台全量/minimax_h3_director_v2v_2094599667274309633.json, 平台全量/视频人物替换工作流Minimax H3_2108726039680733186.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流_2086836832465149953.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流_2090255476226351106.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流_2091830064806719490.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流_2095764158875791361.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流_2095813700035891201.json, 视频生成/图生视频/MiniMax H3 导演台双采样全能工作流_2091717015529672706.json, 视频生成/图生视频/MiniMax H3开源版 导演台全能工作流加速优化_2086023470298779649.json, 视频生成/图生视频/MiniMax-H3 Director 导演台（多参模式）_2099349402946195457.json, 视频生成/图生视频/MiniMax-H3 Director 导演台（多参模式）_2099820499600764930.json, 视频生成/图生视频/MiniMaxH3导演台_2098299681519529986.json, 视频生成/图生视频/MinimaxH3导演台优化二采_2108815050982125569.json, 视频生成/图生视频/Minimax_H3_导演台多合一工作流_2099776978822975489.json, 视频生成/图生视频/Minimax_H3_导演台多合一工作流_2100036933652148226.json, 视频生成/图生视频/minimax_h3_二采_加速_2113314419370455041.json, 视频生成/图生视频/超强电影感+MiniMax H3导演台（适合叙事短片）_2097295043429224450.json, 视频生成/图生视频/（自用）MiniMax H3 导演台工作流（原作者：AI搅拌手）_2095426676049145857.json, 视频生成/图生视频/（自用）二次采样加速MiniMax H3 导演台工作流（原作者：AI搅拌手）_2090361827803877377.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2090104417038196737.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2094624733835907074.json, 视频生成/文生视频/MiniMax H3 电影级运镜全能导演台｜二采精修｜分镜合成｜加速版_2096009884130177025.json, 视频生成/文生视频/MiniMax H3 电影质感全能导演台｜二采放大｜分镜合成｜8步加速版_2100406933353226242.json, 视频生成/文生视频/minimaxH3 全模态导演台-多参考图 x 多视频  x  多音频_2091642744618967042.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（平台全量/minimax_h3_director_rv2v_2094601858668122113.json、平台全量/minimax_h3_director_v2v 视频编辑_2084824665377300481.json、平台全量/minimax_h3_director_v2v_2094599667274309633.json、平台全量/视频人物替换工作流Minimax H3_2108726039680733186.json、视频生成/图生视频/MiniMax H3 导演台全能工作流_2086836832465149953.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `MiniMaxH3Director`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 24/26 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 22/26 个有
- `PathchSageAttentionKJ` —— 22/26 个有
- `MiniMaxH3DirectorRefine` —— 19/26 个有
- `LoraLoaderModelOnly` —— 16/26 个有
- `UpscaleModelLoader` —— 16/26 个有
- `BasicScheduler` —— 13/26 个有
- `Fast Groups Bypasser (rgthree)` —— 5/26 个有
- `GetNode` —— 2/26 个有
- `SetNode` —— 2/26 个有
- `StringToInt` —— 2/26 个有
- `LoadImage` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
