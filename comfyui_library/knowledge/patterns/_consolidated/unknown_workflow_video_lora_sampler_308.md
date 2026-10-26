---
name: unknown_workflow_video_lora_sampler_308
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.555125
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Animate ——飞翔荷兰人_1971146513277689858.json, 视频生成/图生视频/Wan2.2 Animate 人物替换_1969930159883231234.json, 视频生成/图生视频/Wan2.2 Animate 视频换人 视频人物替换_2037140996198240257.json, 视频生成/图生视频/Wan2.2 Animate 角色替换+背景动作迁移 KJ加速版-StarAI_1969240711893839873.json, 视频生成/图生视频/Wan2.2 Animate 角色替换视频动作迁移 KJ加速版-StarAI_1969526770116554754.json, 视频生成/图生视频/Wan2.2 Animate人物迁移 单_多人舞蹈影视替换 （点编辑器遮罩）_1971057186338152449.json, 视频生成/图生视频/多人镜头替换工具-MM_1970004050341208065.json, 视频生成/图生视频/超精准多人视频替换(支持3DCG和真人)_20251014_1976173547762647041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_308

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Animate ——飞翔荷兰人_1971146513277689858.json、视频生成/图生视频/Wan2.2 Animate 人物替换_1969930159883231234.json、视频生成/图生视频/Wan2.2 Animate 视频换人 视频人物替换_2037140996198240257.json、视频生成/图生视频/Wan2.2 Animate 角色替换+背景动作迁移 KJ加速版-StarAI_1969240711893839873.json、视频生成/图生视频/Wan2.2 Animate 角色替换视频动作迁移 KJ加速版-StarAI_1969526770116554754.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `SetNode`
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
- `ImageConcatMulti` —— 7/8 个有
- `BlockifyMask` —— 5/8 个有
- `DrawMaskOnImage` —— 5/8 个有
- `GetImageSizeAndCount` —— 5/8 个有
- `Int` —— 5/8 个有
- `JWInteger` —— 5/8 个有
- `GrowMask` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `DownloadAndLoadSAM2Model` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 3/8 个有
- `PointsEditor` —— 3/8 个有
- `Sam2Segmentation` —— 3/8 个有
- `VHS_VideoInfo` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `INTConstant` —— 2/8 个有
- `Text` —— 2/8 个有
- `WanVideoContextOptions` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `AILab_MiniCPM_4_V` —— 1/8 个有
- `DilateErodeMask` —— 1/8 个有
- `Float` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `LayerMask: LoadFlorence2Model` —— 1/8 个有
- `LayerMask: ObjectDetectorFL2` —— 1/8 个有
- `LayerMask: SAM2VideoUltra` —— 1/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/8 个有
- `Mask Invert` —— 1/8 个有
- `MaskSmooth+` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `OpenDWPose_JK` —— 1/8 个有
- `OpenposePreprocessor` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `Seed_` —— 1/8 个有
- `ToFloat` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
