---
name: unknown_workflow_generic_1654
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [GetImageRangeFromBatch, SaveImage, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/图生图/一键提取视频首尾帧_2041793153333731330.json, 平台全量/视频去水印并高清放大到1080P（第一步：获取视频中的首帧静态图）_2028096131338604546.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1654

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键提取视频首尾帧_2041793153333731330.json、平台全量/视频去水印并高清放大到1080P（第一步：获取视频中的首帧静态图）_2028096131338604546.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `SaveImage`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewAny` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
