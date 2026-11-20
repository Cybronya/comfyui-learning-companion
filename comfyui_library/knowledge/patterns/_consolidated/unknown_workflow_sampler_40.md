---
name: unknown_workflow_sampler_40
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94375
common_nodes: [DF_Get_image_size, ImageStitch, LoadImage, RunningHub USO Loader, RunningHub USO Sampler, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/USO单图多风格一致性反推图生图_1963137798670880769.json, 图片生成/图生图/USO单图风格一致性图生图_1963122858853642242.json, 图片生成/图生图/USO单图风格一致性图生图_1963133920571273217.json, 图片生成/文生图/USO单图风格一致性文生图_1963108546273579010.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_40

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/USO单图多风格一致性反推图生图_1963137798670880769.json、图片生成/图生图/USO单图风格一致性图生图_1963122858853642242.json、图片生成/图生图/USO单图风格一致性图生图_1963133920571273217.json、图片生成/文生图/USO单图风格一致性文生图_1963108546273579010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `DF_Get_image_size`
- `ImageStitch`
- `LoadImage`
- `RunningHub USO Loader`
- `RunningHub USO Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
