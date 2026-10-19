---
name: unknown_workflow_video_lora_sampler_744
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.412
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Anim换脸_2046577984135503874.json, 视频生成/图生视频/2001302724798971906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_744

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Anim换脸_2046577984135503874.json、视频生成/图生视频/2001302724798971906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FlashVSRNode` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `Mask Invert` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SAM3_TrackToMask` —— 1/2 个有
- `SAM3_VideoTrack` —— 1/2 个有
- `SeCModelLoader` —— 1/2 个有
- `SeCVideoSegmentation` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
