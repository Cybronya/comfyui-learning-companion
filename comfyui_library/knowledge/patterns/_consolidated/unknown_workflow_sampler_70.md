---
name: unknown_workflow_sampler_70
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_Translator, RunningHubUniWorldSampler, RunningUniworldModelLoader, SaveImage, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/30秒Uniworld图片转绘_1931862507332239362.json, 图片生成/图生图/Uniworld去除对象_1933005400730112001.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_70

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/30秒Uniworld图片转绘_1931862507332239362.json、图片生成/图生图/Uniworld去除对象_1933005400730112001.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `RunningHubUniWorldSampler`
- `RunningUniworldModelLoader`
- `SaveImage`
- `easy imageConcat`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
