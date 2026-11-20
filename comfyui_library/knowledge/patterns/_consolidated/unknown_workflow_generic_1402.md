---
name: unknown_workflow_generic_1402
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7595
common_nodes: [CR Text, ImpactSwitch, Int, LoadImage, Note Plus (mtb), SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Step1X-Edit图像编辑-全能图片G4o平替版-StarAI_1916790021335224322.json, 图片生成/图生图/全能图片V1最强图像编辑模型，单双图模型随意切换，提示词润色+格式自动整理-StarAI_1960779393322946561.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1402

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Step1X-Edit图像编辑-全能图片G4o平替版-StarAI_1916790021335224322.json、图片生成/图生图/全能图片V1最强图像编辑模型，单双图模型随意切换，提示词润色+格式自动整理-StarAI_1960779393322946561.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `ImpactSwitch`
- `Int`
- `LoadImage`
- `Note Plus (mtb)`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有
- `RunningHub_Step1XEdit` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
