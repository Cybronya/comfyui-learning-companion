---
name: unknown_workflow_controlnet_video_lora_16
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.552429
common_nodes: [BlockifyMask, CLIPVisionLoader, CR Prompt Text, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, LoadImage, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/03-11-01-WAN2.2_Animate-主体混合或动作迁移_1989934295831769090.json, 平台全量/03-11-02-WAN2.2_Animate-网红舞蹈视频转绘_1989934349317492738.json, 视频生成/图生视频/(Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json, 视频生成/图生视频/Wan Animate KJ V2版+Sec稳定自动遮罩视频换装_1977311321710567425.json, 视频生成/图生视频/视频换装稳定版，可切镜头V3_1990353025669754881.json, 视频生成/图生视频/（自用）Wan Animate KJ V2版+Sec稳定遮罩Mix视频V3（换装前置）_1977639019339239426.json, 视频生成/文生视频/Wan Animate KJ V2版+Sec稳定遮罩视频换装V3_1976929662687420417.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_16

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/03-11-01-WAN2.2_Animate-主体混合或动作迁移_1989934295831769090.json、平台全量/03-11-02-WAN2.2_Animate-网红舞蹈视频转绘_1989934349317492738.json、视频生成/图生视频/(Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json、视频生成/图生视频/Wan Animate KJ V2版+Sec稳定自动遮罩视频换装_1977311321710567425.json、视频生成/图生视频/视频换装稳定版，可切镜头V3_1990353025669754881.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 7 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
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
- `ACE_ImageFaceCrop` —— 6/7 个有
- `ClothesSegment` —— 6/7 个有
- `DownloadAndLoadSAM2Model` —— 6/7 个有
- `DrawViTPose` —— 6/7 个有
- `ImageFromBatch` —— 6/7 个有
- `OnnxDetectionModelLoader` —— 6/7 个有
- `PointsEditor` —— 6/7 个有
- `PoseAndFaceDetection` —— 6/7 个有
- `PoseRetargetPromptHelper` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `Sam2Segmentation` —— 6/7 个有
- `SeCModelLoader` —— 6/7 个有
- `SeCVideoSegmentation` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `EmptyImage` —— 5/7 个有
- `ImageConcanate` —— 5/7 个有
- `JWInteger` —— 5/7 个有
- `VHS_VideoInfo` —— 5/7 个有
- `WanVideoContextOptions` —— 5/7 个有
- `PDIMAGE_LongerSize` —— 4/7 个有
- `segformer_b2_clothes` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `DWPreprocessor` —— 2/7 个有
- `FaceMaskFromPoseKeypoints` —— 2/7 个有
- `INTConstant` —— 2/7 个有
- `ImageCropByMaskAndResize` —— 2/7 个有
- `PixelPerfectResolution` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/7 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `TT_img_enc_v2` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
