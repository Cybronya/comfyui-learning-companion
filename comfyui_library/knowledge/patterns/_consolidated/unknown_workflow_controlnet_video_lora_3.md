---
name: unknown_workflow_controlnet_video_lora_3
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.586429
common_nodes: [BlockifyMask, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, JWInteger, LoadImage, PointsEditor, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy showAnything]
problems: []
missing: [AnimalPosePreprocessor, LayerUtility: PurgeVRAM, CR Prompt Text, easy promptConcat, segformer_b2_clothes]
members: [视频生成/图生视频/1978363035192549378.json, 视频生成/图生视频/1998610915446677506.json, 视频生成/图生视频/1974413564041670657.json, 视频生成/图生视频/1974415771805855745.json, 视频生成/图生视频/1974423112462766082.json, 视频生成/图生视频/1974430400560893954.json, 视频生成/图生视频/1974432637244805122.json, 视频生成/图生视频/1976929662687420417.json, 视频生成/图生视频/1977311321710567425.json, 视频生成/图生视频/1990353025669754881.json, 视频生成/图生视频/1977639019339239426.json, 视频生成/图生视频/1977660761738739714.json, 视频生成/文生视频/1974432637244805122.json, 视频生成/文生视频/1976929662687420417.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1978363035192549378.json、视频生成/图生视频/1998610915446677506.json、视频生成/图生视频/1974413564041670657.json、视频生成/图生视频/1974415771805855745.json、视频生成/图生视频/1974423112462766082.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 14 个 workflow 都包含：
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
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanVideoContextOptions` —— 13/14 个有
- `WanVideoTorchCompileSettings` —— 13/14 个有
- `ACE_ImageFaceCrop` —— 12/14 个有
- `DrawViTPose` —— 12/14 个有
- `OnnxDetectionModelLoader` —— 12/14 个有
- `PoseAndFaceDetection` —— 12/14 个有
- `PoseRetargetPromptHelper` —— 12/14 个有
- `EmptyImage` —— 9/14 个有
- `ImageConcanate` —— 8/14 个有
- `PDIMAGE_LongerSize` —— 7/14 个有
- `VHS_VideoInfo` —— 7/14 个有
- `ClothesSegment` —— 6/14 个有
- `ImageFromBatch` —— 6/14 个有
- `PreviewImage` —— 6/14 个有
- `PrimitiveInt` —— 6/14 个有
- `SeCModelLoader` —— 6/14 个有
- `SeCVideoSegmentation` —— 6/14 个有
- `segformer_b2_clothes` —— 4/14 个有
- `RH_Captioner` —— 3/14 个有
- `SaveImage` —— 3/14 个有
- `ShowText` —— 3/14 个有
- `easy promptConcat` —— 3/14 个有
- `AnimalPosePreprocessor` —— 2/14 个有
- `LayerUtility: PurgeVRAM` —— 2/14 个有
- `TT_img_enc_v2` —— 2/14 个有
- `ImageUpscaleWithModel` —— 1/14 个有
- `PoseDetectionOneToAllAnimation` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `UpscaleModelLoader` —— 1/14 个有
- `easy anythingIndexSwitch` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：AnimalPosePreprocessor、LayerUtility: PurgeVRAM、CR Prompt Text、easy promptConcat、segformer_b2_clothes
