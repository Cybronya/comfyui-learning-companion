---
name: unknown_workflow_sampler_13
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6875
common_nodes: [CR Prompt Text, ImageConcanate, LoadImage, PDIMAGE_LongerSize, RunningHub USO Loader, RunningHub USO Sampler, SaveImage]
problems: []
missing: [RunningHub USO Loader, RunningHub USO Sampler, CR Prompt Text]
members: [图片生成/文生图/1962486590113202178.json, 图片生成/文生图/1962487178385338370.json, 图片生成/文生图/1962782611250757633.json, 图片生成/文生图/1962802231387009026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_13

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1962486590113202178.json、图片生成/文生图/1962487178385338370.json、图片生成/文生图/1962782611250757633.json、图片生成/文生图/1962802231387009026.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Prompt Text`
- `ImageConcanate`
- `LoadImage`
- `PDIMAGE_LongerSize`
- `RunningHub USO Loader`
- `RunningHub USO Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ImageGetSize` —— 1/4 个有
- `ResizeLongestToNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：RunningHub USO Loader、RunningHub USO Sampler、CR Prompt Text
