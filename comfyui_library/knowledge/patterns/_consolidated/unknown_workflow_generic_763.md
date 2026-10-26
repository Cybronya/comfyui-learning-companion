---
name: unknown_workflow_generic_763
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.84475
common_nodes: [CR Overlay Text, Compare, Image Blank, ImageConcanate, ImpactSwitch, Int, InversionDemoLazySwitch, JjkText, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Multi Text Merge, RHHiddenNodes, SaveImage, TextInput_, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/内衣随意上身，情趣内衣搭配秀，内衣情趣装换装，换头，换姿态背景_2018712966417358849.json, 图片生成/图生图/换头，换装，换背景，电商穿搭工具，姿势控制 （快速出图版）_2017685684592578561.json, 图片生成/图生图/百搭秀Pro OOTD 平替全能图片V1 Pro_2003978910310277122.json, 图片生成/图生图/百搭秀换装——平替全能图片V1 Pro+姿态控制_2001643694421864450.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_763

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/内衣随意上身，情趣内衣搭配秀，内衣情趣装换装，换头，换姿态背景_2018712966417358849.json、图片生成/图生图/换头，换装，换背景，电商穿搭工具，姿势控制 （快速出图版）_2017685684592578561.json、图片生成/图生图/百搭秀Pro OOTD 平替全能图片V1 Pro_2003978910310277122.json、图片生成/图生图/百搭秀换装——平替全能图片V1 Pro+姿态控制_2001643694421864450.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Overlay Text`
- `Compare`
- `Image Blank`
- `ImageConcanate`
- `ImpactSwitch`
- `Int`
- `InversionDemoLazySwitch`
- `JjkText`
- `LayerUtility: ImageBlendAdvance V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Multi Text Merge`
- `RHHiddenNodes`
- `SaveImage`
- `TextInput_`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `ConvertRGBNode` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `MaxNode` —— 3/4 个有
- `Resolution` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `LayerMask: SegformerB2ClothesUltra` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1440 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1440，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
