---
name: unknown_workflow_generic_1861
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6515
common_nodes: [Any Switch (rgthree), DeepTranslatorTextNode, Fast Groups Bypasser (rgthree), Int, InvertMask, JoinImageWithAlpha, LayerMask: SegformerB2ClothesUltra, LayerMask: SegmentAnythingUltra V2, Load Image Batch, LoadImage, MaskBlur+, Masks Add, PlaySound|pysssss, SDMatteApply, SaveImage, TextInput_]
problems: []
missing: []
members: [图片生成/文生图/抠图_1989160854727831554.json, 平台全量/QT102-智能抠图 支持语抠图，选择服装抠图，批量抠图_1946847960661680130.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1861

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/抠图_1989160854727831554.json、平台全量/QT102-智能抠图 支持语抠图，选择服装抠图，批量抠图_1946847960661680130.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `DeepTranslatorTextNode`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `InvertMask`
- `JoinImageWithAlpha`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `Load Image Batch`
- `LoadImage`
- `MaskBlur+`
- `Masks Add`
- `PlaySound|pysssss`
- `SDMatteApply`
- `SaveImage`
- `TextInput_`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
