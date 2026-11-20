---
name: unknown_workflow_video_47
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.989667
common_nodes: [ImageResizeKJv2, Images to RGB, MaskPreview+, MaskToImage, RH_Translator, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/Sam3语义分割遮罩模型-Sam3 Segmentation_1991908961492291586.json, 平台全量/Sam3精准语义分割遮罩模型-Sam3 Segmentation-视频遮罩获取_2018851292554207234.json, 平台全量/Sam3语义分割遮罩_1992848049842049025.json, 平台全量/Sam3语义分割遮罩模型-Sam3 Segmentation_1991610436030308353.json, 平台全量/Sam3语义分割遮罩模型-Sam3 Segmentation_1991926394104115201.json, 平台全量/Sam3语义分割遮罩模型-Sam3 Segmentation_2007087851925671937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_47

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Sam3语义分割遮罩模型-Sam3 Segmentation_1991908961492291586.json、平台全量/Sam3精准语义分割遮罩模型-Sam3 Segmentation-视频遮罩获取_2018851292554207234.json、平台全量/Sam3语义分割遮罩_1992848049842049025.json、平台全量/Sam3语义分割遮罩模型-Sam3 Segmentation_1991610436030308353.json、平台全量/Sam3语义分割遮罩模型-Sam3 Segmentation_1991926394104115201.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageResizeKJv2`
- `Images to RGB`
- `MaskPreview+`
- `MaskToImage`
- `RH_Translator`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 5/6 个有
- `LoadSAM3Model` —— 5/6 个有
- `SAM3Segmentation` —— 5/6 个有
- `CR SDXL Aspect Ratio` —— 1/6 个有
- `CustomAddLabel` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `easy sam3ModelLoader` —— 1/6 个有
- `easy sam3VideoSegmentation` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
