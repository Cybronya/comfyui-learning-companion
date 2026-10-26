---
name: unknown_workflow_generic_1410
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7635
common_nodes: [ImageScale, ImageStitch, JjkText, LoadImage, PreviewImage, RH_ComfyFluxKontext, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/kontext 一键双人合影生成_1938146335730372610.json, 图片生成/图生图/kontext 万物迁移 （优化版）_1938089963911319554.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1410

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/kontext 一键双人合影生成_1938146335730372610.json、图片生成/图生图/kontext 万物迁移 （优化版）_1938089963911319554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageScale`
- `ImageStitch`
- `JjkText`
- `LoadImage`
- `PreviewImage`
- `RH_ComfyFluxKontext`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `InspyrenetRembg` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_Translator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
