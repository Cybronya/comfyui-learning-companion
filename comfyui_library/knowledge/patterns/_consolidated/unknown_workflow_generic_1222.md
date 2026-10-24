---
name: unknown_workflow_generic_1222
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.618
common_nodes: [CR Prompt Text, Comfly_api_set, ImageConcanate, LoadImage, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Max图像编辑（贞贞的AI工坊API）_2011374508204105729.json, 图片生成/图生图/全能图片G image 1.5图像编辑v1（贞贞的ai工坊版）_2001715416554717186.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1222

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux2 Max图像编辑（贞贞的AI工坊API）_2011374508204105729.json、图片生成/图生图/全能图片G image 1.5图像编辑v1（贞贞的ai工坊版）_2001715416554717186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Comfly_api_set`
- `ImageConcanate`
- `LoadImage`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Comfly_Flux_2_Max` —— 1/2 个有
- `Comfly_gpt_image_1_edit` —— 1/2 个有
- `JWInteger` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
