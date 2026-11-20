---
name: unknown_workflow_upscale_74
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.773
common_nodes: [ImageUpscaleWithModel, ImpactSwitch, LoadImage, RHHiddenNodes, ReActorRestoreFace, SaveImagePlus, UpscaleModelLoader, easy boolean, easy ifElse, easy int, easy string]
problems: []
missing: []
members: [图片生成/图生图/换脸-图片换脸-单人_多人-支持指定人物换脸_2004865742099152898.json, 平台全量/换脸-图片换脸-单人_多人-支持指定人物换脸_2047286997915541506.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_74

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换脸-图片换脸-单人_多人-支持指定人物换脸_2004865742099152898.json、平台全量/换脸-图片换脸-单人_多人-支持指定人物换脸_2047286997915541506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `ImpactSwitch`
- `LoadImage`
- `RHHiddenNodes`
- `ReActorRestoreFace`
- `SaveImagePlus`
- `UpscaleModelLoader`
- `easy boolean`
- `easy ifElse`
- `easy int`
- `easy string`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
