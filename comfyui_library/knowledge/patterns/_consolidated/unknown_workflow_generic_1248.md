---
name: unknown_workflow_generic_1248
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8345
common_nodes: [Image Stitch, LoadImage, PreviewImage, RH_ComfyFluxKontext, RH_Translator, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Kontext 双图风格参考迁移_1938806256159412225.json, 图片生成/文生图/Kontext（2图版）言出法随-电商-换背景-换物-换装-图生图-文生图_1934106102831173633.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1248

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Kontext 双图风格参考迁移_1938806256159412225.json、图片生成/文生图/Kontext（2图版）言出法随-电商-换背景-换物-换装-图生图-文生图_1934106102831173633.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Stitch`
- `LoadImage`
- `PreviewImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 1/2 个有
- `ImageCrop+` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
