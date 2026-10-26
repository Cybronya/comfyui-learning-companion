---
name: unknown_workflow_video_lora_sampler_29
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.570296
common_nodes: [CLIPVisionLoader, DWPreprocessor, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/43.tonnie-Wan2.2 Animate视频动作迁移_2004764267972882433.json, 视频生成/图生视频/46c.tonnie-Wan2.2+Animate替换视频中的人物的服装_2006611649658101762.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移_2050805055514791937.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096554698164752386.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096575707920027649.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2050834000423473154.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2069022324761907201.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2082813929578909697.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2104161486053662722.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2104198098951168001.json, 视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流_2110913885871099905.json, 视频生成/图生视频/Wan Animate2.2 替身出演，形神境随_1969559616474542081.json, 视频生成/图生视频/Wan Animate2.2主体混合mix加速版V1_1969219198985662465.json, 视频生成/图生视频/Wan Animate2.2主体迁移（自动裁剪脸部，增强主体一致性）v3_1972998201764655106.json, 视频生成/图生视频/Wan-Animate-动作参考-KJ_1969398350657318913.json, 视频生成/图生视频/Wan-Animate-角色替换-KJ_1962703044544737281.json, 视频生成/图生视频/Wan-Animate-角色替换-人物唱歌-KJ_1969620771280744450.json, 视频生成/图生视频/Wan-Animate-角色替换-小鸟摇-KJ_1969608004544983041.json, 视频生成/图生视频/WanAnimate真人舞蹈-视频动作和表情迁移_1968952890041778177.json, 视频生成/图生视频/WanAnimate角色替换+动作参考- FXAI_1970797508848984065.json, 视频生成/图生视频/WanAnimate角色替换+动作参考-By Aiwood_1969039434375176194.json, 视频生成/图生视频/动作迁移_2017571137424723969.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042478976223940610.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042488839909937154.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2044301999423889409.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2047561888975822849.json, 视频生成/图生视频/角色替换+动作参考_2000210160024944641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/43.tonnie-Wan2.2 Animate视频动作迁移_2004764267972882433.json、视频生成/图生视频/46c.tonnie-Wan2.2+Animate替换视频中的人物的服装_2006611649658101762.json、视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移_2050805055514791937.json、视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096554698164752386.json、视频生成/图生视频/Wan Animate  视频换脸 _ 动作迁移工作流 唱歌跳舞视频动作迁移_2096575707920027649.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 27 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 26/27 个有
- `DownloadAndLoadSAM2Model` —— 26/27 个有
- `DrawMaskOnImage` —— 26/27 个有
- `GrowMask` —— 26/27 个有
- `PointsEditor` —— 26/27 个有
- `Sam2Segmentation` —— 26/27 个有
- `FaceMaskFromPoseKeypoints` —— 25/27 个有
- `GetImageSizeAndCount` —— 25/27 个有
- `ImageConcatMulti` —— 25/27 个有
- `ImageCropByMaskAndResize` —— 25/27 个有
- `WanVideoSetLoRAs` —— 25/27 个有
- `GetNode` —— 21/27 个有
- `INTConstant` —— 21/27 个有
- `SetNode` —— 21/27 个有
- `WanVideoContextOptions` —— 19/27 个有
- `GetImageRangeFromBatch` —— 14/27 个有
- `PreviewImage` —— 14/27 个有
- `AudioCropProcessUTK` —— 12/27 个有
- `SimpleMath+` —— 5/27 个有
- `Int` —— 4/27 个有
- `easy showAnything` —— 3/27 个有
- `ColorMatch` —— 2/27 个有
- `JWInteger` —— 2/27 个有
- `MathExpression|pysssss` —— 2/27 个有
- `Text Multiline` —— 2/27 个有
- `WanVideoLoraSelect` —— 2/27 个有
- `ACE_ImageFaceCrop` —— 1/27 个有
- `CR Prompt Text` —— 1/27 个有
- `Fast Groups Muter (rgthree)` —— 1/27 个有
- `OnnxDetectionModelLoader` —— 1/27 个有
- `PoseAndFaceDetection` —— 1/27 个有
- `PoseRetargetPromptHelper` —— 1/27 个有
- `easy cleanGpuUsed` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
