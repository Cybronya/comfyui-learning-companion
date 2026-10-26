---
name: unknown_workflow_video_lora_sampler_213
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.478
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/动作迁移+表情迁移 升级版本_1996485212181766146.json, 数字人/数字人/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922.json, 视频生成/图生视频/Wan-Animate_V2-动作迁移自动版_1975030930718986242.json, 视频生成/图生视频/wanvideo_WanAnimate_v2-kj-小鸟摇_1977738504492961794.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064688046506856449.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064701232807239682.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064716165561282562.json, 视频生成/图生视频/白用更新动作迁移_2051920241860591618.json, 视频生成/图生视频/自动P图，对齐模板视频，动作迁移，表情迁移_2000015490712039426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_213

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/动作迁移+表情迁移 升级版本_1996485212181766146.json、数字人/数字人/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922.json、视频生成/图生视频/Wan-Animate_V2-动作迁移自动版_1975030930718986242.json、视频生成/图生视频/wanvideo_WanAnimate_v2-kj-小鸟摇_1977738504492961794.json、视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `ImageConcatMulti` —— 9/10 个有
- `Int` —— 8/10 个有
- `PreviewImage` —— 8/10 个有
- `SDPoseOODLoader` —— 8/10 个有
- `SDPoseOODProcessor` —— 8/10 个有
- `VHS_VideoInfo` —— 8/10 个有
- `Text` —— 7/10 个有
- `YOLOModelLoader` —— 7/10 个有
- `BlockifyMask` —— 4/10 个有
- `DrawMaskOnImage` —— 4/10 个有
- `WanVideoContextOptions` —— 4/10 个有
- `DownloadAndLoadSAM2Model` —— 3/10 个有
- `DrawViTPose` —— 3/10 个有
- `GrowMaskWithBlur` —— 3/10 个有
- `Sam2Segmentation` —— 3/10 个有
- `Evaluate Integers` —— 2/10 个有
- `WanVideoTorchCompileSettings` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `ClothesSegment` —— 1/10 个有
- `GrowMask` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageFromBatch` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `JWStringMultiline` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `ReActorFaceBoost` —— 1/10 个有
- `ReActorFaceSwap` —— 1/10 个有
- `SeCModelLoader` —— 1/10 个有
- `SeCVideoSegmentation` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
