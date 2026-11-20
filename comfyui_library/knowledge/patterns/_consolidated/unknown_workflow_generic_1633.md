---
name: unknown_workflow_generic_1633
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8235
common_nodes: [Fast Groups Muter (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, RH_Nano_Banana_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/rh_gemini2.5(-全能图片V1)单双图切换驱动_1960684227488546817.json, 平台全量/Banan谷歌香蕉图像编辑_1962020923492777985.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1633

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/rh_gemini2.5(-全能图片V1)单双图切换驱动_1960684227488546817.json、平台全量/Banan谷歌香蕉图像编辑_1962020923492777985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Muter (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
