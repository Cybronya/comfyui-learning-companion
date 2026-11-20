---
name: unknown_workflow_video_100
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7445
common_nodes: [AddLabel, CoordinatePlotter, ImageConcanate, ImageConcatMulti, ImageFromBatch, PointsEditor, PreviewImage, PrimitiveInt, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/SecNode_动态遮罩_1978516734611181570.json, 平台全量/SecNodes+Sam2丝滑稳定视频遮罩V2_1976911209616347138.json, 平台全量/comfyUI-sec-workflow_1977998184624652289.json, 视频生成/文生视频/SecNodes视频遮罩提取_1977650345428045825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_100

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/SecNode_动态遮罩_1978516734611181570.json、平台全量/SecNodes+Sam2丝滑稳定视频遮罩V2_1976911209616347138.json、平台全量/comfyUI-sec-workflow_1977998184624652289.json、视频生成/文生视频/SecNodes视频遮罩提取_1977650345428045825.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `CoordinatePlotter`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageFromBatch`
- `PointsEditor`
- `PreviewImage`
- `PrimitiveInt`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `DownloadAndLoadSAM2Model` —— 1/4 个有
- `ImageAndMaskPreview_UTK` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Sam2Segmentation` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
