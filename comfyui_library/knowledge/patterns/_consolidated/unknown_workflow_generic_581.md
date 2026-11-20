---
name: unknown_workflow_generic_581
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.831167
common_nodes: [CR Text, ChinesePrompt_Mix, GrowMaskWithBlur, JoinImageWithAlpha, LayerMask: SegmentAnythingUltra V2, LoadImage, Mask Invert, MaskPreview+, PreviewImage, SDMatteApply, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/抠图最强模型透明材质完美扣除_2097134466434162690.json, 图片生成/图生图/抠图最强模型透明材质完美扣除_2097231577305669633.json, 图片生成/图生图/抠图最强模型（透明材质完美扣除）_1957784334042329089.json, 图片生成/图生图/抠图最强模型（透明材质完美扣除）_2076128864685875201.json, 图片生成/图生图/抠图最强模型（透明材质完美扣除）_2078460342971224065.json, 平台全量/透明材质抠图_1966823048215191554.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_581

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/抠图最强模型透明材质完美扣除_2097134466434162690.json、图片生成/图生图/抠图最强模型透明材质完美扣除_2097231577305669633.json、图片生成/图生图/抠图最强模型（透明材质完美扣除）_1957784334042329089.json、图片生成/图生图/抠图最强模型（透明材质完美扣除）_2076128864685875201.json、图片生成/图生图/抠图最强模型（透明材质完美扣除）_2078460342971224065.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CR Text`
- `ChinesePrompt_Mix`
- `GrowMaskWithBlur`
- `JoinImageWithAlpha`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `Mask Invert`
- `MaskPreview+`
- `PreviewImage`
- `SDMatteApply`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AddMask` —— 5/6 个有
- `LayerMask: BiRefNetUltraV2` —— 5/6 个有
- `LayerMask: LoadBiRefNetModelV2` —— 5/6 个有
- `LayerMask: MaskPreview` —— 5/6 个有
- `RMBG` —— 5/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
