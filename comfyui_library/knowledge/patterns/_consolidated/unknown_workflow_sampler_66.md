---
name: unknown_workflow_sampler_66
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8465
common_nodes: [ImageConcanate, JjkText, LoadImage, RH_Translator, RunningHub OneReward Loader, RunningHub OneReward Sampler, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Flux Fill OneReward 外扩 RH_1969451804171923458.json, 图片生成/图生图/Flux Fill OneReward 重绘 RH版_1969402547008118786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_66

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux Fill OneReward 外扩 RH_1969451804171923458.json、图片生成/图生图/Flux Fill OneReward 重绘 RH版_1969402547008118786.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcanate`
- `JjkText`
- `LoadImage`
- `RH_Translator`
- `RunningHub OneReward Loader`
- `RunningHub OneReward Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImagePadForOutpaintMasked` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
