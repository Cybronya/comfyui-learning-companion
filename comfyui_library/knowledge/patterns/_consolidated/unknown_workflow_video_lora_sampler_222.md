---
name: unknown_workflow_video_lora_sampler_222
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6411
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, ImageResizeKJv2, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json, 视频生成/图生视频/Wan2.2Animate姿态+声音+精准替换_2002155248145842178.json, 视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json, 视频生成/图生视频/全能图片V12 + WanAnimate，让你穿着勇士队球衣开跳库里之歌_1992409563280330754.json, 视频生成/图生视频/视频角色替换工作流_2010634733373366273.json, 视频生成/图生视频/（自用）Wan Animate KJ V2版Move模式视频V2（换装前置）_1977660761738739714.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Mix主体混合版V2_1974413564041670657.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移Uni3c运镜版V1_1974430400560893954.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移V1_1974423112462766082.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_222

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Wan2.2+Animate+V2模运动迁移Uni3c运镜_1976670695512068097.json、视频生成/图生视频/Wan2.2Animate姿态+声音+精准替换_2002155248145842178.json、视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json、视频生成/图生视频/全能图片V12 + WanAnimate，让你穿着勇士队球衣开跳库里之歌_1992409563280330754.json、视频生成/图生视频/视频角色替换工作流_2010634733373366273.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 10 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `WanVideoLoraSelectMulti` —— 9/10 个有
- `GetNode` —— 8/10 个有
- `WanVideoContextOptions` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `GrowMask` —— 7/10 个有
- `ImageConcatMulti` —— 7/10 个有
- `CR Prompt Text` —— 6/10 个有
- `PointsEditor` —— 6/10 个有
- `WanVideoEncode` —— 6/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/10 个有
- `WanVideoUni3C_embeds` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `ACE_ImageFaceCrop` —— 5/10 个有
- `JWInteger` —— 5/10 个有
- `PoseRetargetPromptHelper` —— 5/10 个有
- `INTConstant` —— 4/10 个有
- `GrowMaskWithBlur` —— 3/10 个有
- `Label (rgthree)` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `GetImageSize+` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `Bookmark (rgthree)` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `RH_Captioner` —— 1/10 个有
- `RH_Nano_Banana2_Image2Image` —— 1/10 个有
- `ShowText` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有
- `VHS_VideoInfoLoaded` —— 1/10 个有
- `WanVideoLoraSelect` —— 1/10 个有
- `easy promptConcat` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
