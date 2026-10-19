---
name: unknown_workflow_controlnet_video_lora_19
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93725
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, FloatConstant, GetImageSizeAndCount, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/SCAIL+ 全能图片V1 Pro伪背景替换_2001645245022498817.json, 视频生成/文生视频/SCAIL单人三维姿态驱动+图像参考的长时序稳定生成_2000259341699739649.json, 视频生成/文生视频/SCAIL双人三维姿态驱动+图像参考的长时序稳定生成_2000476624699224066.json, 视频生成/文生视频/SCAIL多人三维姿态驱动+图像参考的长时序稳定生成_2001536477941121026.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/SCAIL+ 全能图片V1 Pro伪背景替换_2001645245022498817.json、视频生成/文生视频/SCAIL单人三维姿态驱动+图像参考的长时序稳定生成_2000259341699739649.json、视频生成/文生视频/SCAIL双人三维姿态驱动+图像参考的长时序稳定生成_2000476624699224066.json、视频生成/文生视频/SCAIL多人三维姿态驱动+图像参考的长时序稳定生成_2001536477941121026.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `FloatConstant`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWImageExtractFromBatch` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_Nano_Banana2_Image2Image` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
