---
name: unknown_workflow_video_sampler_51
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.749333
common_nodes: [Any Switch (rgthree), DiffuEraserLoader, DiffuEraserSampler, Fast Groups Muter (rgthree), FlashVSRNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, MathExpression|pysssss, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy compare, easy ifElse]
problems: []
missing: []
members: [平台全量/各种视频水印去除，含seedance2.0即梦水印去除（支持自动遮罩，手动遮罩）_2020682584543469569.json, 平台全量/超能视频2.0水印去除（自动适配横屏竖屏9_16-16_9）_2020470530733776898.json, 数字人/数字人/即梦视频去水印 seedance2.0 去水印 自动版_2020494888961314818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_51

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/各种视频水印去除，含seedance2.0即梦水印去除（支持自动遮罩，手动遮罩）_2020682584543469569.json、平台全量/超能视频2.0水印去除（自动适配横屏竖屏9_16-16_9）_2020470530733776898.json、数字人/数字人/即梦视频去水印 seedance2.0 去水印 自动版_2020494888961314818.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `Fast Groups Muter (rgthree)`
- `FlashVSRNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy compare`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `WatermarkDetector` —— 2/3 个有
- `WatermarkDetectorLoader` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `GetImagesFromBatchIndexed` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
