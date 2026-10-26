---
name: unknown_workflow_video_lora_sampler_71
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.524316
common_nodes: [BatchCount+, CLIPVisionLoader, DownloadAndLoadNLFModel, DrawViTPose, ImageBatch, ImageFromBatch, ImageResizeKJv2, LazySwitch1way, NLFPredict, OnnxDetectionModelLoader, PoseAndFaceDetection, PoseDetectionVitPoseToDWPose, PreviewImage, RenderNLFPoses, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, YOLOModelLoader, easy anythingIndexSwitch, easy boolean, easy int, easy mathInt]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898.json, 图片生成/文生图/Wan2.2 Animate copy2 1-1_2038940728784592898.json, 图片生成/文生图/Wan2.2 Animate copy2 1-3_2043561252823244802.json, 数字人/数字人/Wan2.2 Animate动作迁移-AIGCTV_2043534137943920642.json, 数字人/数字人/wan2.2服装+视频自动化_2041447047198412802.json, 数字人/数字人/wan2.2服装+视频自动化_2041482422352617474.json, 数字人/数字人/完美一致的视频动作迁移_2038453735529127937.json, 视频生成/图生视频/11122_2052262207102177281.json, 视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部+抖动+舞蹈动作模仿一致性_2052900551507103745.json, 视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部+抖动+舞蹈动作模仿一致性_2058733620000550914.json, 视频生成/图生视频/Wan2.2 Animate动作迁移+表情+手部一致性_2059989559043248130.json, 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1-小珠光-显存优化_2041363947378450433.json, 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1-自适应调整 显存优化_2038787173708734465.json, 视频生成/图生视频/Wan2.2 Animate动作迁移V6.1（自动尺寸）30S_2060333059626586114.json, 视频生成/图生视频/Wan2.2 Animate动作迁移（4月自动尺寸版本）_2041791361074073602.json, 视频生成/图生视频/Wan2.2 Animate动作迁移（姿势面部胸部幅度大小可调节）（自动尺寸）_2039936284520615937.json, 视频生成/图生视频/Wan2.2 动作迁移V6.1+抖动（动作表情一致性强）_2041459050583433217.json, 视频生成/图生视频/Wan2.2-Animate-Move&Mix-V1_2101929816374206466.json, 视频生成/图生视频/Wan2.2AnimateV2 视频角色动作迁移与角色注入_ 视频重绘 _ 动作克隆 _ 角色一致性_2054844641391980546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate动作迁移V6（自动尺寸）_2038850866869968898.json、图片生成/文生图/Wan2.2 Animate copy2 1-1_2038940728784592898.json、图片生成/文生图/Wan2.2 Animate copy2 1-3_2043561252823244802.json、数字人/数字人/Wan2.2 Animate动作迁移-AIGCTV_2043534137943920642.json、数字人/数字人/wan2.2服装+视频自动化_2041447047198412802.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 19 个 workflow 都包含：
- `BatchCount+`
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `DrawViTPose`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LazySwitch1way`
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
- `LoadImage` —— 18/19 个有
- `WanVideoLoraSelectMulti` —— 18/19 个有
- `easy float` —— 18/19 个有
- `GetNode` —— 17/19 个有
- `MemoryCleaner` —— 17/19 个有
- `RHHiddenNodes` —— 17/19 个有
- `SetNode` —— 17/19 个有
- `CR Text` —— 15/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/19 个有
- `easy compare` —— 15/19 个有
- `easy imageSize` —— 15/19 个有
- `ImpactSwitch` —— 14/19 个有
- `LazySwitch2way` —— 13/19 个有
- `BBoxYOLO` —— 12/19 个有
- `CheckpointLoaderSimple` —— 12/19 个有
- `SDPoseDrawKeypoints` —— 12/19 个有
- `SDPoseKeypointExtractor` —— 12/19 个有
- `SDPoseOODLoader` —— 7/19 个有
- `SDPoseOODProcessor` —— 7/19 个有
- `VRAMReserver` —— 6/19 个有
- `SimpleMath+` —— 4/19 个有
- `Any Switch (rgthree)` —— 3/19 个有
- `BlockifyMask` —— 3/19 个有
- `DownloadAndLoadSAM2Model` —— 3/19 个有
- `DrawMaskOnImage` —— 3/19 个有
- `Fast Groups Bypasser (rgthree)` —— 3/19 个有
- `GrowMaskWithBlur` —— 3/19 个有
- `Sam2Segmentation` —— 3/19 个有
- `WanVideoEncode` —— 2/19 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/19 个有
- `WanVideoUni3C_embeds` —— 2/19 个有
- `easy cleanGpuUsed` —— 2/19 个有
- `孤海注释` —— 2/19 个有
- `CM_FloatToInt` —— 1/19 个有
- `Int` —— 1/19 个有
- `Label (rgthree)` —— 1/19 个有
- `PreviewAny` —— 1/19 个有
- `Primitive integer [Crystools]` —— 1/19 个有
- `PrimitiveFloat` —— 1/19 个有
- `RunningHub Deepcleaner` —— 1/19 个有
- `easy sam3ModelLoader` —— 1/19 个有
- `easy sam3VideoSegmentation` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
