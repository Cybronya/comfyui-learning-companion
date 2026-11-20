---
name: unknown_workflow_generic_979
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.821333
common_nodes: [ImageFromBatch+, SaveImage, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/图生图/SeeDance 2.0 首帧及尾帧获取V1_2020832969061048322.json, 图片生成/图生图/从视频中提取最后一帧图_2011716521806012417.json, 图片生成/图生图/从视频中提取第一帧图_2011714335785099266.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_979

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SeeDance 2.0 首帧及尾帧获取V1_2020832969061048322.json、图片生成/图生图/从视频中提取最后一帧图_2011716521806012417.json、图片生成/图生图/从视频中提取第一帧图_2011714335785099266.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageFromBatch+`
- `SaveImage`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
