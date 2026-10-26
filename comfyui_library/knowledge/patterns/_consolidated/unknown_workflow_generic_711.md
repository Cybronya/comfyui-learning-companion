---
name: unknown_workflow_generic_711
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9055
common_nodes: [InsertAnythingImageProcessor, InsertAnythingInferencer, InsertAnythingLoader, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LoadImage, MaskOption, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Nunchaku_InsertAnything电商产品展示_1922466510332428290.json, 图片生成/图生图/Nunchaku版本InsertAnything_1921815681019363330.json, 图片生成/图生图/万物迁移 insertAnything 蒙层_1922606419437129729.json, 图片生成/图生图/万物迁移新技术-insertAnything_1922639665013166081.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_711

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Nunchaku_InsertAnything电商产品展示_1922466510332428290.json、图片生成/图生图/Nunchaku版本InsertAnything_1921815681019363330.json、图片生成/图生图/万物迁移 insertAnything 蒙层_1922606419437129729.json、图片生成/图生图/万物迁移新技术-insertAnything_1922639665013166081.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `InsertAnythingImageProcessor`
- `InsertAnythingInferencer`
- `InsertAnythingLoader`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LoadImage`
- `MaskOption`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LayerMask: MaskGrow` —— 2/4 个有
- `MaskPreview+` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
