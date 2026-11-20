---
name: unknown_workflow_lora_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [EasyControlGenerate, EasyControlLoadFlux, EasyControlLoadLora, ImageConcanate, ImageResizeKJ, LoadImage, Note Plus (mtb), SaveImageAndMetadata_]
problems: []
missing: []
members: [图片生成/图生图/EasyCN-地面最强吉卜力图生图反推_1909927009089454082.json, 图片生成/图生图/EasyControl新版Subject物品改建工作流_1912195766746607618.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/EasyCN-地面最强吉卜力图生图反推_1909927009089454082.json、图片生成/图生图/EasyControl新版Subject物品改建工作流_1912195766746607618.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `EasyControlGenerate`
- `EasyControlLoadFlux`
- `EasyControlLoadLora`
- `ImageConcanate`
- `ImageResizeKJ`
- `LoadImage`
- `Note Plus (mtb)`
- `SaveImageAndMetadata_`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
