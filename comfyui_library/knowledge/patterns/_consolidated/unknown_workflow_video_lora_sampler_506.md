---
name: unknown_workflow_video_lora_sampler_506
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.543
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, EmptyImage, FloatConstant, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, INTConstant, ImageConcatMulti, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, PreviewImage, SetNode, TextBox1, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy anythingIndexSwitch, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/1979072764936097793.json, 视频生成/图生视频/1976916291078524930.json, 视频生成/图生视频/2016418267958616065.json, 视频生成/图生视频/1976905425356525570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_506

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1979072764936097793.json、视频生成/图生视频/1976916291078524930.json、视频生成/图生视频/2016418267958616065.json、视频生成/图生视频/1976905425356525570.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 4 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `EmptyImage`
- `FloatConstant`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `TextBox1`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `Sam2Segmentation` —— 3/4 个有
- `AnimalPosePreprocessor` —— 2/4 个有
- `DWPreprocessor` —— 2/4 个有
- `DrawViTPose` —— 2/4 个有
- `FaceMaskFromPoseKeypoints` —— 2/4 个有
- `ImageCropByMaskAndResize` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `PixelPerfectResolution` —— 2/4 个有
- `DownloadAndLoadQwenModel` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `QwenVLDetection` —— 1/4 个有
- `SeCModelLoader` —— 1/4 个有
- `SeCVideoSegmentation` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
