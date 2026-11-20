---
name: unknown_workflow_video_upscale_lora_3
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7491
common_nodes: [CLIPLoader, LoraLoaderModelOnly, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, UpscaleModelLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/H3图生视频-高清版_2099775777192636418.json, 图片生成/文生图/Dasiwa-MiniMax H3 导演台全能工作流-文生视频-人物去油_2110210924484325378.json, 平台全量/MiniMax H3 漫剧导演台 3_2119736014557237250.json, 视频生成/图生视频/Dasiwa-MiniMax H3 导演台全能工作流-参考生视频_2095363717016932353.json, 视频生成/图生视频/Dasiwa-MiniMax H3 导演台全能工作流-图生视频-人物去油_2110344332875231233.json, 视频生成/图生视频/Dasiwa-MiniMax H3 导演台全能工作流-图生视频_2095485189106528257.json, 视频生成/文生视频/Dasiwa-MiniMax H3 导演台全能工作流-文生视频_2095312937933164545.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流-fl2v-文生视频_2092254280576225281.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流-人物去油_2096232593627897857.json, 视频生成/文生视频/MiniMax H3 漫剧导演台_2097478155698262018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/H3图生视频-高清版_2099775777192636418.json、图片生成/文生图/Dasiwa-MiniMax H3 导演台全能工作流-文生视频-人物去油_2110210924484325378.json、平台全量/MiniMax H3 漫剧导演台 3_2119736014557237250.json、视频生成/图生视频/Dasiwa-MiniMax H3 导演台全能工作流-参考生视频_2095363717016932353.json、视频生成/图生视频/Dasiwa-MiniMax H3 导演台全能工作流-图生视频-人物去油_2110344332875231233.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 9/10 个有
- `MiniMaxH3Director` —— 8/10 个有
- `CreateVideo` —— 7/10 个有
- `LoraLoaderBypassModelOnly` —— 7/10 个有
- `ModelAttentionBackend` —— 7/10 个有
- `孤海注释` —— 7/10 个有
- `SaveVideo` —— 6/10 个有
- `ComfyMiniMaxH3Director` —— 2/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
