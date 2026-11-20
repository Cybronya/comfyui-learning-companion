---
name: unknown_workflow_generic_675
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8484
common_nodes: [ImageFromBatch+, SaveImage, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/图生图/SeeDance 2.0 首帧及尾帧获取V1_2020832969061048322.json, 图片生成/图生图/从视频中提取最后一帧图_2011716521806012417.json, 图片生成/图生图/从视频中提取第一帧图_2011714335785099266.json, 平台全量/SeeDance 2.0 【视频】首帧及尾帧获取_2021064227607289857.json, 平台全量/视频首尾帧图提取_1974445605617537026.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_675

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/SeeDance 2.0 首帧及尾帧获取V1_2020832969061048322.json、图片生成/图生图/从视频中提取最后一帧图_2011716521806012417.json、图片生成/图生图/从视频中提取第一帧图_2011714335785099266.json、平台全量/SeeDance 2.0 【视频】首帧及尾帧获取_2021064227607289857.json、平台全量/视频首尾帧图提取_1974445605617537026.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageFromBatch+`
- `SaveImage`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoInfo` —— 4/5 个有
- `PreviewImage` —— 3/5 个有
- `SimpleMath+` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
