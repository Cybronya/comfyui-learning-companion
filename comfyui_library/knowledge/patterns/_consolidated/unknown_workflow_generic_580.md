---
name: unknown_workflow_generic_580
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.877333
common_nodes: [Fast Groups Muter (rgthree), Image Comparer (rgthree), InspyrenetRembg, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageCombineAlpha, LayerUtility: ImageRemoveAlpha, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/抠图_一键抠图王_1982503060440260610.json, 图片生成/图生图/最强抠图_指定物品抠图_移除背景_2066793905529638913.json, 平台全量/双抠图版本-可单图_批量_1951305753791508481.json, 平台全量/抠图丨当前最强抠图_1876479952211107842.json, 平台全量/最强抠图 指定物品抠图 移除背景_2066383567063699458.json, 平台全量/最强抠图丨导入图片一键抠图封装版本_1937709722461978625.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_580

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/抠图_一键抠图王_1982503060440260610.json、图片生成/图生图/最强抠图_指定物品抠图_移除背景_2066793905529638913.json、平台全量/双抠图版本-可单图_批量_1951305753791508481.json、平台全量/抠图丨当前最强抠图_1876479952211107842.json、平台全量/最强抠图 指定物品抠图 移除背景_2066383567063699458.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `InspyrenetRembg`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageCombineAlpha`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ColorPicker` —— 4/6 个有
- `BiRefNet_ModelLoader_Zho` —— 3/6 个有
- `BiRefNet_Zho` —— 3/6 个有
- `ArgosTranslateTextNode` —— 2/6 个有
- `BaiduTranslateNode` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `Int2Any_AS` —— 1/6 个有
- `LoadImagesFromPath` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
