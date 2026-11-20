---
name: unknown_workflow_video_lora_vae_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.423
common_nodes: [AILab_MaskPreview, BlockifyMask, CLIPVisionLoader, CoordinatePlotter, DrawMaskOnImage, GetNode, GrowMaskWithBlur, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, PreviewImage, SDPoseOODLoader, SDPoseOODProcessor, Sa2VANodeTpl, SeCModelLoader, SeCVideoSegmentation, SetNode, Text, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, YOLOModelLoader, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097.json, 视频生成/图生视频/人物替换+动作迁移：Wan2.2AnimateV2+Sa2VA+SeC最强遮罩_1992222168801144834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097.json、视频生成/图生视频/人物替换+动作迁移：Wan2.2AnimateV2+Sa2VA+SeC最强遮罩_1992222168801144834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：42%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_MaskPreview`
- `BlockifyMask`
- `CLIPVisionLoader`
- `CoordinatePlotter`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `Sa2VANodeTpl`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AdaptiveWanVideoAnimateEmbeds` —— 1/2 个有
- `Evaluate Integers` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoAnimateEmbeds` —— 1/2 个有
- `WanVideoSampler` —— 1/2 个有
- `WanVideoSamplerExtraArgs` —— 1/2 个有
- `WanVideoSamplerv2` —— 1/2 个有
- `WanVideoSchedulerv2` —— 1/2 个有
- `WanVideoSetBlockSwap` —— 1/2 个有
- `easy convertAnything` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `workflow>Frame Padder-1` —— 1/2 个有
- `workflow>Frame Padder-2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
