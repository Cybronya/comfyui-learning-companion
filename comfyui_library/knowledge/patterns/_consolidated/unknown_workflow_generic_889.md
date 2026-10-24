---
name: unknown_workflow_generic_889
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.969667
common_nodes: [JoinImageWithAlpha, LayerMask: SegmentAnythingUltra V2, LoadImage, MaskPreview+, SDMatteApply, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/SDMatte高精度半透明图像抠图V2_1956216471452045313.json, 图片生成/图生图/SDmatte高精度抠图，毛发、玻璃、水珠、婚纱等等完美抠出_1956524137772711938.json, 图片生成/图生图/最强抠图神器SDMatte_1955981530273337346.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_889

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SDMatte高精度半透明图像抠图V2_1956216471452045313.json、图片生成/图生图/SDmatte高精度抠图，毛发、玻璃、水珠、婚纱等等完美抠出_1956524137772711938.json、图片生成/图生图/最强抠图神器SDMatte_1955981530273337346.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `JoinImageWithAlpha`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `MaskPreview+`
- `SDMatteApply`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Mask Invert` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `LayerUtility: ImageCombineAlpha` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
