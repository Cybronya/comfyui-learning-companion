---
name: unknown_workflow_controlnet_video_lora_29
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.383
common_nodes: [Any Switch (rgthree), BlockifyMask, CLIPVisionLoader, CR Text, DownloadAndLoadNLFModel, DrawMaskOnImage, DrawViTPose, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, GetNode, GroundingDinoModelLoader_SDPose, GrowMask, ImageFromBatch, ImageResizeKJv2, Int, LoadImage, NLFPredict, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, PoseDetectionOneToAllAnimation, PoseDetectionVitPoseToDWPose, PreviewImage, RenderNLFPoses, RepeatImageBatch, SDPoseOODLoader, SDPoseOODProcessor, SeCModelLoader, SeCVideoSegmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader, easy anythingIndexSwitch, easy framesEditor, easy sam3ImageSegmentation, easy sam3ModelLoader]
problems: []
missing: []
members: [平台全量/WAN ANIMATE商用级开源 万能视频生成_2042941701400043522.json, 平台全量/animate终点-V2.0_2036253016612937730.json, 平台全量/舞蹈动作迁移_2043998473153941505.json, 视频生成/图生视频/全能替换_2046490938419187713.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_29

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/WAN ANIMATE商用级开源 万能视频生成_2042941701400043522.json、平台全量/animate终点-V2.0_2036253016612937730.json、平台全量/舞蹈动作迁移_2043998473153941505.json、视频生成/图生视频/全能替换_2046490938419187713.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：38%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadNLFModel`
- `DrawMaskOnImage`
- `DrawViTPose`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `GroundingDinoModelLoader_SDPose`
- `GrowMask`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PoseDetectionOneToAllAnimation`
- `PoseDetectionVitPoseToDWPose`
- `PreviewImage`
- `RenderNLFPoses`
- `RepeatImageBatch`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy anythingIndexSwitch`
- `easy framesEditor`
- `easy sam3ImageSegmentation`
- `easy sam3ModelLoader`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 3/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/4 个有
- `GIMMVFI_interpolate` —— 3/4 个有
- `ImageBatch` —— 3/4 个有
- `ImpactConditionalBranch` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `VHS_GetImageCount` —— 3/4 个有
- `WanVideoBlockSwap` —— 3/4 个有
- `WanVideoSetBlockSwap` —— 3/4 个有
- `WanVideoSetLoRAs` —— 3/4 个有
- `easy compare` —— 3/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
