---
name: unknown_workflow_video_lora_sampler_814
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.585
common_nodes: [BatchCount+, DWPreprocessor, DrawViTPose, GetNode, ImageFromBatch, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PixelPerfectResolution, PoseAndFaceDetection, PreviewImage, RepeatImageBatch, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything, math_calculate]
problems: []
missing: []
members: [平台全量/Wan22Animate人物替换_2030205739989475329.json, 视频生成/图生视频/Wan22Animate人物替换_循环_2032090534226960386.json, 视频生成/图生视频/Wan22Animate动作迁移_2029464241350119426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_814

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Wan22Animate人物替换_2030205739989475329.json、视频生成/图生视频/Wan22Animate人物替换_循环_2032090534226960386.json、视频生成/图生视频/Wan22Animate动作迁移_2029464241350119426.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `BatchCount+`
- `DWPreprocessor`
- `DrawViTPose`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PixelPerfectResolution`
- `PoseAndFaceDetection`
- `PreviewImage`
- `RepeatImageBatch`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `math_calculate`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 2/3 个有
- `Combine Video` —— 2/3 个有
- `DownloadAndLoadSAM2Model` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `Florence2ModelLoader` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `Florence2toCoordinates` —— 2/3 个有
- `GrowMask` —— 2/3 个有
- `ImageBatchMultiple+` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `Sam2Segmentation` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `LazySwitch1way` —— 1/3 个有
- `PoseDetectionOneToAllAnimation` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy compare` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy mathInt` —— 1/3 个有
- `easy sam3ModelLoader` —— 1/3 个有
- `easy sam3VideoSegmentation` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
