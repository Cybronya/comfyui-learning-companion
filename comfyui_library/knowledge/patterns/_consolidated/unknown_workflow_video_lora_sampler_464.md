---
name: unknown_workflow_video_lora_sampler_464
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.428143
common_nodes: [CLIPVisionLoader, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064688046506856449.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064701232807239682.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064716165561282562.json, 视频生成/图生视频/影视二创_2022695116523180034.json, 视频生成/图生视频/视频二创角色替换Wan2.2 Animate KJ_2003413399671377922.json, 视频生成/图生视频/首帧二创人物替换优化_2042773742413156353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_464

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json、视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064688046506856449.json、视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064701232807239682.json、视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064716165561282562.json、视频生成/图生视频/影视二创_2022695116523180034.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PreviewImage`
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
- `PoseAndFaceDetection` —— 6/7 个有
- `SDPoseOODLoader` —— 6/7 个有
- `SDPoseOODProcessor` —— 6/7 个有
- `YOLOModelLoader` —— 6/7 个有
- `VHS_VideoInfo` —— 5/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `Int` —— 4/7 个有
- `Text` —— 4/7 个有
- `INTConstant` —— 3/7 个有
- `PlaySound|pysssss` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `BBoxYOLO` —— 1/7 个有
- `CheckpointLoaderSimple` —— 1/7 个有
- `DWPreprocessor` —— 1/7 个有
- `DrawViTPose` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `NumberComparison` —— 1/7 个有
- `PixelPerfectResolution` —— 1/7 个有
- `SDPoseDrawKeypoints` —— 1/7 个有
- `SDPoseKeypointExtractor` —— 1/7 个有
- `easy ifElse` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
