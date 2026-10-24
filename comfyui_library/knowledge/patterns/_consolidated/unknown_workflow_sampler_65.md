---
name: unknown_workflow_sampler_65
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.914
common_nodes: [ImageToMask, LoadImage, RunningHub OneReward Eraser, RunningHub OneReward Loader, RunningHub OneReward Sampler, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/AI绘画_OneReward多功能测试_局部重绘、图像外扩工作流V1_1965606591733055490.json, 图片生成/图生图/OneReward多功能测试工作流V1_1965465889753714689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_65

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/AI绘画_OneReward多功能测试_局部重绘、图像外扩工作流V1_1965606591733055490.json、图片生成/图生图/OneReward多功能测试工作流V1_1965465889753714689.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageToMask`
- `LoadImage`
- `RunningHub OneReward Eraser`
- `RunningHub OneReward Loader`
- `RunningHub OneReward Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
