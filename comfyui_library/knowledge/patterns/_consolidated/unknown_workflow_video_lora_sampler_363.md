---
name: unknown_workflow_video_lora_sampler_363
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.463833
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SDPoseOODLoader, SDPoseOODProcessor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/sdpose 动作迁移_2071622435325177857.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064688046506856449.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064701232807239682.json, 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064716165561282562.json, 视频生成/图生视频/自动P图，对齐模板视频，动作迁移，表情迁移_2000015490712039426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_363

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/sdpose 动作迁移_2071622435325177857.json、视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json、视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064688046506856449.json、视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064701232807239682.json、视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2064716165561282562.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Text` —— 5/6 个有
- `WanVideoContextOptions` —— 2/6 个有
- `BlockifyMask` —— 1/6 个有
- `ClothesSegment` —— 1/6 个有
- `CompressImages` —— 1/6 个有
- `DrawMaskOnImage` —— 1/6 个有
- `Evaluate Integers` —— 1/6 个有
- `GrowMask` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `ReActorFaceBoost` —— 1/6 个有
- `ReActorFaceSwap` —— 1/6 个有
- `SaveMP4` —— 1/6 个有
- `SeCModelLoader` —— 1/6 个有
- `SeCVideoSegmentation` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `WanVideoTorchCompileSettings` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
