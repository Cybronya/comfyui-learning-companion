---
name: unknown_workflow_video_lora_sampler_146
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.5635
common_nodes: [BatchCount+, CLIPVisionLoader, DownloadAndLoadNLFModel, DrawViTPose, ImageBatch, ImageFromBatch, ImageResizeKJv2, LazySwitch1way, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseAndFaceDetection, PoseDetectionVitPoseToDWPose, PreviewImage, RenderNLFPoses, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, YOLOModelLoader, easy anythingIndexSwitch, easy boolean, easy int, easy mathInt]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898.json, 图片生成/图生图/Wan2.2_Animate动作迁移+表情+手部一致性_2115618607257444353.json, 图片生成/图生图/Wan2.2_Animate动作迁移+表情+手部一致性_2115666496704835585.json, 图片生成/文生图/Wan2.2 Animate copy2 1-1_2038940728784592898.json, 图片生成/文生图/Wan2.2 Animate copy2 1-3_2043561252823244802.json, 平台全量/004.Wan视频之源007.图+视频跳舞-图片背景_2035564111743950850.json, 平台全量/Wan2.2 Animate动作迁移_2041836655023230977.json, 平台全量/Wan2.2 Animate角色替换+动作迁移_2043756994556858369.json, 平台全量/Wan2.2 Animate角色替换+动作迁移_2045176899768422402.json, 平台全量/Wan2.2-Animate-Move&Mix-V1_2105118615497433089.json, 平台全量/Wan2.2-Animate-Move&Mix-V1_2105495366593503233.json, 平台全量/animate 2129988469_2036254057895038977.json, 数字人/数字人/Wan2.2 Animate动作迁移-AIGCTV_2043534137943920642.json, 视频生成/图生视频/11122_2052262207102177281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_146

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898.json、图片生成/图生图/Wan2.2_Animate动作迁移+表情+手部一致性_2115618607257444353.json、图片生成/图生图/Wan2.2_Animate动作迁移+表情+手部一致性_2115666496704835585.json、图片生成/文生图/Wan2.2 Animate copy2 1-1_2038940728784592898.json、图片生成/文生图/Wan2.2 Animate copy2 1-3_2043561252823244802.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 14 个 workflow 都包含：
- `BatchCount+`
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `DrawViTPose`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LazySwitch1way`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PoseDetectionVitPoseToDWPose`
- `PreviewImage`
- `RenderNLFPoses`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy anythingIndexSwitch`
- `easy boolean`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `easy float` —— 13/14 个有
- `MemoryCleaner` —— 12/14 个有
- `GetNode` —— 11/14 个有
- `RHHiddenNodes` —— 11/14 个有
- `SetNode` —— 11/14 个有
- `CR Text` —— 10/14 个有
- `ImpactSwitch` —— 10/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/14 个有
- `easy compare` —— 10/14 个有
- `easy imageSize` —— 10/14 个有
- `BBoxYOLO` —— 9/14 个有
- `CheckpointLoaderSimple` —— 9/14 个有
- `LazySwitch2way` —— 9/14 个有
- `SDPoseDrawKeypoints` —— 9/14 个有
- `SDPoseKeypointExtractor` —— 9/14 个有
- `BlockifyMask` —— 7/14 个有
- `DrawMaskOnImage` —— 7/14 个有
- `GrowMaskWithBlur` —— 7/14 个有
- `Fast Groups Bypasser (rgthree)` —— 6/14 个有
- `SDPoseOODLoader` —— 5/14 个有
- `SDPoseOODProcessor` —— 5/14 个有
- `Any Switch (rgthree)` —— 4/14 个有
- `DownloadAndLoadSAM2Model` —— 4/14 个有
- `Sam2Segmentation` —— 4/14 个有
- `VRAMReserver` —— 4/14 个有
- `easy sam3ModelLoader` —— 4/14 个有
- `easy sam3VideoSegmentation` —— 4/14 个有
- `ImageBlend` —— 3/14 个有
- `LayerUtility: PurgeVRAM` —— 3/14 个有
- `MaskToImage` —— 3/14 个有
- `PreviewAny` —— 3/14 个有
- `easy framesEditor` —— 3/14 个有
- `easy sam3GetObjectIds` —— 3/14 个有
- `easy sam3GetObjectMask` —— 3/14 个有
- `easy sam3VideoModelExtraConfig` —— 3/14 个有
- `easy sam3Visualization` —— 3/14 个有
- `SimpleMath+` —— 2/14 个有
- `孤海注释` —— 2/14 个有
- `CM_FloatToInt` —— 1/14 个有
- `CM_IntBinaryOperation` —— 1/14 个有
- `Display Any (rgthree)` —— 1/14 个有
- `FloatConstant` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `MaskPreview+` —— 1/14 个有
- `Preview from image [Crystools]` —— 1/14 个有
- `ReservedVRAMSetter` —— 1/14 个有
- `VHS_LoadVideoFFmpeg` —— 1/14 个有
- `VHS_VideoInfoLoaded` —— 1/14 个有
- `VRAMCleanup` —— 1/14 个有
- `WanVideoEncode` —— 1/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/14 个有
- `WanVideoUni3C_embeds` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
