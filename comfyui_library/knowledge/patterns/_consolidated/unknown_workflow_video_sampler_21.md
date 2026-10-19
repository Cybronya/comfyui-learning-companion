---
name: unknown_workflow_video_sampler_21
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6665
common_nodes: [BlockifyMask, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, INTConstant, ImageResizeKJv2, LoadImage, MaskToImage, OnnxDetectionModelLoader, PointsEditor, RHHiddenNodes, Sam2Segmentation, SeCModelLoader, SeCVideoSegmentation, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached]
problems: []
missing: []
members: [视频生成/图生视频/2004896290372808705.json, 视频生成/图生视频/2011052589265195009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2004896290372808705.json、视频生成/图生视频/2011052589265195009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskToImage`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `RHHiddenNodes`
- `Sam2Segmentation`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`

**可变部分**（部分 workflow 才有）：
- `ConvertOpenPoseKeypointsToDWPose` —— 1/2 个有
- `DownloadAndLoadNLFModel` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `FaceMaskFromPoseKeypoints` —— 1/2 个有
- `ImageCropByMaskAndResize` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `NLFPredict` —— 1/2 个有
- `PixelPerfectResolution` —— 1/2 个有
- `PoseAndFaceDetection` —— 1/2 个有
- `PoseDetectionVitPoseToDWPose` —— 1/2 个有
- `RenderNLFPoses` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy framesEditor` —— 1/2 个有
- `easy sam3ModelLoader` —— 1/2 个有
- `easy sam3VideoSegmentation` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
