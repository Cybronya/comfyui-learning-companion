---
name: unknown_workflow_video_lora_sampler_113
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.641
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, ImageConcatMulti, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json, 图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json, 视频生成/图生视频/(Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json, 视频生成/图生视频/(骨骼自适应)Wan2.2 Animate V2模型Move模式运动迁移V1_1998610915446677506.json, 视频生成/图生视频/Wan Animate KJ V2版+Sec稳定自动遮罩视频换装_1977311321710567425.json, 视频生成/图生视频/视频换装稳定版，可切镜头V3_1990353025669754881.json, 视频生成/图生视频/（自用）Wan Animate KJ V2版+Sec稳定遮罩Mix视频V3（换装前置）_1977639019339239426.json, 视频生成/图生视频/（自用）Wan Animate KJ V2版Move模式视频V2（换装前置）_1977660761738739714.json, 视频生成/文生视频/Wan Animate KJ V2版+Sec稳定遮罩视频换装V3_1976929662687420417.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Mix主体混合版V2_1974413564041670657.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移Uni3c运镜版V1_1974430400560893954.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移V1_1974423112462766082.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json、图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json、视频生成/图生视频/(Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json、视频生成/图生视频/(骨骼自适应)Wan2.2 Animate V2模型Move模式运动迁移V1_1998610915446677506.json、视频生成/图生视频/Wan Animate KJ V2版+Sec稳定自动遮罩视频换装_1977311321710567425.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 13 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ACE_ImageFaceCrop` —— 12/13 个有
- `GetImageSizeAndCount` —— 12/13 个有
- `GrowMask` —— 12/13 个有
- `JWInteger` —— 12/13 个有
- `PointsEditor` —— 12/13 个有
- `CR Prompt Text` —— 11/13 个有
- `DownloadAndLoadSAM2Model` —— 11/13 个有
- `GetNode` —— 11/13 个有
- `PoseRetargetPromptHelper` —— 11/13 个有
- `Sam2Segmentation` —— 11/13 个有
- `SetNode` —— 11/13 个有
- `WanVideoEncode` —— 11/13 个有
- `WanVideoUni3C_ControlnetLoader` —— 11/13 个有
- `WanVideoUni3C_embeds` —— 11/13 个有
- `easy showAnything` —— 11/13 个有
- `WanVideoContextOptions` —— 10/13 个有
- `WanVideoTorchCompileSettings` —— 10/13 个有
- `EmptyImage` —— 7/13 个有
- `ImageFromBatch` —— 7/13 个有
- `PreviewImage` —— 7/13 个有
- `PrimitiveInt` —— 7/13 个有
- `SeCModelLoader` —— 7/13 个有
- `SeCVideoSegmentation` —— 7/13 个有
- `ClothesSegment` —— 6/13 个有
- `PDIMAGE_LongerSize` —— 6/13 个有
- `VHS_VideoInfo` —— 6/13 个有
- `ImageConcanate` —— 5/13 个有
- `SaveImage` —— 3/13 个有
- `segformer_b2_clothes` —— 3/13 个有
- `TT_img_enc_v2` —— 2/13 个有
- `CoordinatePlotter` —— 1/13 个有
- `GrowMaskWithBlur` —— 1/13 个有
- `INTConstant` —— 1/13 个有
- `ImageUpscaleWithModel` —— 1/13 个有
- `LayerMask: MaskPreview` —— 1/13 个有
- `PoseDetectionOneToAllAnimation` —— 1/13 个有
- `RH_Captioner` —— 1/13 个有
- `ShowText` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有
- `UpscaleModelLoader` —— 1/13 个有
- `easy anythingIndexSwitch` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy promptConcat` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
