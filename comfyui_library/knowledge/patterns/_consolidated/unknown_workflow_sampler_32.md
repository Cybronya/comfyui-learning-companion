---
name: unknown_workflow_sampler_32
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.864
common_nodes: [DF_Get_image_size, ImageRemoveBackground+, ImageResizeKJv2, LBMSampler, LoadImage, LoadLBMModel, PreviewImage, SaveImage, TransparentBGSession+]
problems: []
missing: []
members: [图片生成/图生图/LBM-商品人物重打光换背景_1924654145469673473.json, 图片生成/图生图/LBM打光及背景融合工作流V1_1922669595415691266.json, 图片生成/图生图/[众馨]人物背景融合_1993246795654430722.json, 图片生成/图生图/人物换背景，调整位置，打光_1923965694881558530.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_32

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/LBM-商品人物重打光换背景_1924654145469673473.json、图片生成/图生图/LBM打光及背景融合工作流V1_1922669595415691266.json、图片生成/图生图/[众馨]人物背景融合_1993246795654430722.json、图片生成/图生图/人物换背景，调整位置，打光_1923965694881558530.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `DF_Get_image_size`
- `ImageRemoveBackground+`
- `ImageResizeKJv2`
- `LBMSampler`
- `LoadImage`
- `LoadLBMModel`
- `PreviewImage`
- `SaveImage`
- `TransparentBGSession+`

**可变部分**（部分 workflow 才有）：
- `ImageCompositeMasked` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `LayerUtility: ImageAutoCrop V3` —— 3/4 个有
- `PDIMAGE_LongerSize` —— 3/4 个有
- `Compositor3` —— 1/4 个有
- `CompositorConfig3` —— 1/4 个有
- `ImageScaleDownToSize` —— 1/4 个有
- `preview_mask` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
