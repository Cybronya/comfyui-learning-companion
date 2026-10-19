---
name: unknown_workflow_sampler_14
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.667
common_nodes: [GetImageSizeAndCount, ImageScaleDownToSize, ImageStitch, LoadImage, PreviewImage, RunningHub USO Loader, RunningHub USO Sampler, SaveImage]
problems: []
missing: [RunningHub USO Loader, RunningHub USO Sampler, Text Multiline]
members: [图片生成/文生图/1962876203176800258.json, 图片生成/文生图/1962897927087828994.json, 图片生成/文生图/1986739065456422913.json, 图片生成/文生图/1986739671420104706.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1962876203176800258.json、图片生成/文生图/1962897927087828994.json、图片生成/文生图/1986739065456422913.json、图片生成/文生图/1986739671420104706.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageScaleDownToSize`
- `ImageStitch`
- `LoadImage`
- `PreviewImage`
- `RunningHub USO Loader`
- `RunningHub USO Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 2/4 个有
- `Text Multiline` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：RunningHub USO Loader、RunningHub USO Sampler、Text Multiline
