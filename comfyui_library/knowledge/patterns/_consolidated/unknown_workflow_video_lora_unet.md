---
name: unknown_workflow_video_lora_unet
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.72725
common_nodes: [CLIPLoader, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3图生视频-高清版_2100035695510376450.json, 视频生成/图生视频/H3导演台长视频生成_段间引导_turbo_2087464309365493761.json, 视频生成/图生视频/H3导演台长视频生成_段间引导_turbo_2087586429961596929.json, 视频生成/图生视频/MiniMax H3 AIMixer 导演台4step_2090306246338506754.json, 视频生成/图生视频/MiniMax H3 max 转场爆款导演台_全能参考+首尾帧+全节点注释_2107720944176418818.json, 视频生成/图生视频/MiniMax_H3_max_转场爆款导演台_全能参考+首尾帧_2110653959206694914.json, 视频生成/文生视频/MiniMax H3 max 转场爆款导演台全能 全能参考 首尾帧+全节点注释_2101582619145232385.json, 视频生成/文生视频/MiniMax H3 max 转场爆款导演台全能 全能参考 首尾帧+全节点注释_2101636357511798785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_unet

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3图生视频-高清版_2100035695510376450.json、视频生成/图生视频/H3导演台长视频生成_段间引导_turbo_2087464309365493761.json、视频生成/图生视频/H3导演台长视频生成_段间引导_turbo_2087586429961596929.json、视频生成/图生视频/MiniMax H3 AIMixer 导演台4step_2090306246338506754.json、视频生成/图生视频/MiniMax H3 max 转场爆款导演台_全能参考+首尾帧+全节点注释_2107720944176418818.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DirectorRefine` —— 5/8 个有
- `UpscaleModelLoader` —— 5/8 个有
- `CR Text` —— 4/8 个有
- `Switch` —— 4/8 个有
- `孤海注释` —— 4/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoadImage` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
