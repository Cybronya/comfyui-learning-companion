---
name: unknown_workflow_video_lora_sampler_646
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.506667
common_nodes: [CLIPVisionLoader, DF_Int_to_Float, GetNode, ImageFromBatch, ImageResizeKJv2, LoadImage, MemoryCleaner, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, SimpleMath+, Text, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy boolean, easy float, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2044639396833529858.json, 视频生成/图生视频/2052769134831779841.json, 视频生成/图生视频/2044639687251337217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_646

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2044639396833529858.json、视频生成/图生视频/2052769134831779841.json、视频生成/图生视频/2044639687251337217.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DF_Int_to_Float`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `MemoryCleaner`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `SimpleMath+`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy boolean`
- `easy float`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `BBoxYOLO` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `SDPoseDrawKeypoints` —— 2/3 个有
- `SDPoseKeypointExtractor` —— 2/3 个有
- `YOLOModelLoader` —— 2/3 个有
- `BlockifyMask` —— 1/3 个有
- `DownloadAndLoadNLFModel` —— 1/3 个有
- `DrawMaskOnImage` —— 1/3 个有
- `LayerMask: MaskGrow` —— 1/3 个有
- `NLFPredict` —— 1/3 个有
- `PoseDetectionVitPoseToDWPose` —— 1/3 个有
- `RenderNLFPoses` —— 1/3 个有
- `VHS_VideoInfoLoaded` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy sam3ModelLoader` —— 1/3 个有
- `easy sam3VideoSegmentation` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
