---
name: unknown_workflow_video_lora_sampler_814
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5785
common_nodes: [BatchCount+, DWPreprocessor, DrawViTPose, GetNode, ImageFromBatch, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PixelPerfectResolution, PoseAndFaceDetection, PreviewImage, RepeatImageBatch, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy anythingIndexSwitch, easy cleanGpuUsed, easy showAnything, math_calculate]
problems: []
missing: []
members: [视频生成/图生视频/Wan22Animate人物替换_循环_2032090534226960386.json, 视频生成/图生视频/Wan22Animate动作迁移_2029464241350119426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_814

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan22Animate人物替换_循环_2032090534226960386.json、视频生成/图生视频/Wan22Animate动作迁移_2029464241350119426.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
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
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy showAnything`
- `math_calculate`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `Combine Video` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `Florence2toCoordinates` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageBatchMultiple+` —— 1/2 个有
- `LazySwitch1way` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PoseDetectionOneToAllAnimation` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy mathInt` —— 1/2 个有
- `easy sam3ModelLoader` —— 1/2 个有
- `easy sam3VideoSegmentation` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
