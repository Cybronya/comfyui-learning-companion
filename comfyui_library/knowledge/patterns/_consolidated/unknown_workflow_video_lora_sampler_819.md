---
name: unknown_workflow_video_lora_sampler_819
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.599
common_nodes: [BlockifyMask, CLIPVisionLoader, CR Clamp Value, CR SDXL Aspect Ratio, CR Text Concatenate, CropFace, CropFaces, DetectFaces, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, FlashVSRNode, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, INTConstant, Image Crop Face, ImageResizeKJv2, LoadImage, NumberClamp, OnnxDetectionModelLoader, PoseAndFaceDetection, PrimitiveBoolean, PrimitiveInt, PrimitiveString, Sam2Segmentation, SaveImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy ifElse]
problems: []
missing: []
members: [视频生成/图生视频/WanAnimate_V9动作迁移人物替换_2100754716815880193.json, 视频生成/图生视频/WanAnimate_V9高质量动作迁移High‑quality motion transfer_2100757667223523330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_819

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WanAnimate_V9动作迁移人物替换_2100754716815880193.json、视频生成/图生视频/WanAnimate_V9高质量动作迁移High‑quality motion transfer_2100757667223523330.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Clamp Value`
- `CR SDXL Aspect Ratio`
- `CR Text Concatenate`
- `CropFace`
- `CropFaces`
- `DetectFaces`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `FlashVSRNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `Image Crop Face`
- `ImageResizeKJv2`
- `LoadImage`
- `NumberClamp`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveString`
- `Sam2Segmentation`
- `SaveImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
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
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 1/2 个有
- `SAM3Segmentation` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
