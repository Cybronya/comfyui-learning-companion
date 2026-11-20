---
name: unknown_workflow_video_lora_sampler_220
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.716455
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GrowMask, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PointsEditor, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate角色替换与修改_1932812610956136450.json, 图片生成/图生图/Wan2.2 animate 视频人物替换_1976938900721672193.json, 图片生成/图生图/万物动作迁移One2All_1998760592200585217.json, 平台全量/03-11-03-WAN2.2_Animate_角色替换_1989934447699128322.json, 平台全量/46a.tonnie-Wan2.2 Animate替换视频中的人物及姿态_2005696631309828097.json, 平台全量/Wan2.2 Animate 多人视频人物精准替换_1977741311920984065.json, 平台全量/Wan2.2 Animate 视频换脸_1977731915312758785.json, 平台全量/Wan2.2 Animate 视频物品替换_1978055441882173442.json, 平台全量/Wan2.2 Animate 视频物品替换_2026111994465624066.json, 数字人/数字人/WanAnimate（视频角色替换_姿势迁移）_1969678871396315137.json, 视频生成/图生视频/动漫跳舞SDPOSE+Wan Animate_1973029204331728897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_220

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate角色替换与修改_1932812610956136450.json、图片生成/图生图/Wan2.2 animate 视频人物替换_1976938900721672193.json、图片生成/图生图/万物动作迁移One2All_1998760592200585217.json、平台全量/03-11-03-WAN2.2_Animate_角色替换_1989934447699128322.json、平台全量/46a.tonnie-Wan2.2 Animate替换视频中的人物及姿态_2005696631309828097.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 11 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PointsEditor`
- `Sam2Segmentation`
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 10/11 个有
- `WanVideoTorchCompileSettings` —— 10/11 个有
- `DWPreprocessor` —— 9/11 个有
- `PixelPerfectResolution` —— 8/11 个有
- `Fast Groups Muter (rgthree)` —— 6/11 个有
- `SimpleMath+` —— 6/11 个有
- `GetNode` —— 5/11 个有
- `SetNode` —— 5/11 个有
- `WanVideoSetLoRAs` —— 5/11 个有
- `GetImageSizeAndCount` —— 4/11 个有
- `ImageConcatMulti` —— 4/11 个有
- `MathExpression|pysssss` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `easy int` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `GroundingDinoModelLoader_SDPose` —— 2/11 个有
- `InspyrenetRembg` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `SDPoseOODLoader` —— 2/11 个有
- `SDPoseOODProcessor` —— 2/11 个有
- `YOLOModelLoader` —— 2/11 个有
- `CR Upscale Image` —— 1/11 个有
- `ImageFromBatch` —— 1/11 个有
- `ImpactInt` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `OnnxDetectionModelLoader` —— 1/11 个有
- `PoseDetectionOneToAllAnimation` —— 1/11 个有
- `WanVideoContextOptions` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
