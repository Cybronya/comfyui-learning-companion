---
name: unknown_workflow_upscale_50
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.8
common_nodes: [Image Comparer (rgthree), LoadImage, SUPIR_Upscale, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/水彩放大_2062547319521898497.json, 图片生成/图生图/矢量级放大 无损_1950225257456164865.json, 平台全量/SUPIR放大_2038451394016976898.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_50

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/水彩放大_2062547319521898497.json、图片生成/图生图/矢量级放大 无损_1950225257456164865.json、平台全量/SUPIR放大_2038451394016976898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SUPIR_Upscale`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
