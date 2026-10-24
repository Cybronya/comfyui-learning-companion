---
name: unknown_workflow_sampler_74
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8375
common_nodes: [EmptyImage, GetImageSizeAndCount, ImageResize+, LoadImage, PreviewImage, RH_Prompter, RunningHub USO Loader, RunningHub USO Sampler, SaveImage, StringFunction|pysssss, easy anythingIndexSwitch, easy imageConcat, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/生图-参考风格生图-USO-RunningHub_1980185702988156929.json, 图片生成/图生图/生图-图转任意风格-USO-RunningHub_1980163230716825602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_74

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/生图-参考风格生图-USO-RunningHub_1980185702988156929.json、图片生成/图生图/生图-图转任意风格-USO-RunningHub_1980163230716825602.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageResize+`
- `LoadImage`
- `PreviewImage`
- `RH_Prompter`
- `RunningHub USO Loader`
- `RunningHub USO Sampler`
- `SaveImage`
- `StringFunction|pysssss`
- `easy anythingIndexSwitch`
- `easy imageConcat`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
