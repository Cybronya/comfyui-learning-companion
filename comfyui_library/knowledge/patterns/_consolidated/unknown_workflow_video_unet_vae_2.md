---
name: unknown_workflow_video_unet_vae_2
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.754625
common_nodes: [CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa-MiniMax H3 导演台全能工作流-图生视频-人物去油_2110344332875231233.json, 视频生成/图生视频/H3图生视频-高清版_2100035695510376450.json, 视频生成/图生视频/MiniMax H3 导演台工作流-ref2va_2091323053144887297.json, 视频生成/图生视频/minimax_h3_短剧动漫分镜_2095347998501986306.json, 视频生成/文生视频/Dasiwa-MiniMax H3 导演台全能工作流-文生视频_2095312937933164545.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流-fl2v-文生视频_2092254280576225281.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流-人物去油_2096232593627897857.json, 视频生成/文生视频/MiniMax H3 漫剧导演台_2097478155698262018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Dasiwa-MiniMax H3 导演台全能工作流-图生视频-人物去油_2110344332875231233.json、视频生成/图生视频/H3图生视频-高清版_2100035695510376450.json、视频生成/图生视频/MiniMax H3 导演台工作流-ref2va_2091323053144887297.json、视频生成/图生视频/minimax_h3_短剧动漫分镜_2095347998501986306.json、视频生成/文生视频/Dasiwa-MiniMax H3 导演台全能工作流-文生视频_2095312937933164545.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `MiniMaxH3DirectorRefine` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `UpscaleModelLoader` —— 7/8 个有
- `MiniMaxH3Director` —— 6/8 个有
- `CreateVideo` —— 4/8 个有
- `LoraLoaderBypassModelOnly` —— 4/8 个有
- `ModelAttentionBackend` —— 4/8 个有
- `孤海注释` —— 4/8 个有
- `SaveVideo` —— 3/8 个有
- `ComfyMiniMaxH3Director` —— 2/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
