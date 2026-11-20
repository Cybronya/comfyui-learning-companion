---
name: unknown_workflow_controlnet_video_lora_57
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.602
common_nodes: [BlockifyMask, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, JWInteger, LoadImage, PointsEditor, RH_Captioner, Sam2Segmentation, SetNode, ShowText, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy promptConcat, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_57

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json、视频生成/文生视频/Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `PointsEditor`
- `RH_Captioner`
- `Sam2Segmentation`
- `SetNode`
- `ShowText`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ACE_ImageFaceCrop` —— 1/2 个有
- `AnimalPosePreprocessor` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `OnnxDetectionModelLoader` —— 1/2 个有
- `PDIMAGE_LongerSize` —— 1/2 个有
- `PoseAndFaceDetection` —— 1/2 个有
- `PoseRetargetPromptHelper` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
