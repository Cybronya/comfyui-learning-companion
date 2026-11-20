---
name: unknown_workflow_video_lora_sampler_367
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.637625
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/视频单人姿势匹配_WanAnimate2.2_1990625748220350465.json, 平台全量/角色动作互换工作流_1990974899604889601.json, 数字人/数字人/AI在学抛媚眼？眼神训练挑战！Wan2.2 Animate数字人教程_1969659436019163137.json, 数字人/数字人/Wan Animate 2.2：角色动作迁移_1969987148046868481.json, 数字人/数字人/视频-动作表情口型-wan2.2-animate-KJ_1973995545582768129.json, 视频生成/图生视频/Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json, 视频生成/图生视频/Wan Animate2.2动作迁移_1969366584278085634.json, 视频生成/图生视频/表哥超级画质动作复刻V2.1_2002002967475699713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_367

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/视频单人姿势匹配_WanAnimate2.2_1990625748220350465.json、平台全量/角色动作互换工作流_1990974899604889601.json、数字人/数字人/AI在学抛媚眼？眼神训练挑战！Wan2.2 Animate数字人教程_1969659436019163137.json、数字人/数字人/Wan Animate 2.2：角色动作迁移_1969987148046868481.json、数字人/数字人/视频-动作表情口型-wan2.2-animate-KJ_1973995545582768129.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `JWInteger` —— 7/8 个有
- `GetImageSizeAndCount` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `WanVideoAnimateEmbeds` —— 6/8 个有
- `CR Prompt Text` —— 3/8 个有
- `Text` —— 3/8 个有
- `WanVideoTorchCompileSettings` —— 3/8 个有
- `GetImageRangeFromBatch` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `RHHiddenNodes` —— 2/8 个有
- `VHS_VideoInfo` —— 2/8 个有
- `VHS_VideoInfoLoaded` —— 2/8 个有
- `easy seed` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `Bjornulf_ShowInt` —— 1/8 个有
- `DrawViTPose` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `OnnxDetectionModelLoader` —— 1/8 个有
- `PoseAndFaceDetection` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
