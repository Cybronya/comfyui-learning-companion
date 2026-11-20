---
name: unknown_workflow_controlnet_video_lora_35
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.704667
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/SCAIL-Pose动作迁移-支持真人_动漫_卡通_拟人 IP_动物 等风格化角色的动作生成_2051695050878406657.json, 平台全量/动作迁移合集（吐血整理）人类（动物）单人（多人）_2027637518782439426.json, 平台全量/极强姿态识别SDPose+Wan2.2 Animate动作迁移方案_2052501347337023490.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/SCAIL-Pose动作迁移-支持真人_动漫_卡通_拟人 IP_动物 等风格化角色的动作生成_2051695050878406657.json、平台全量/动作迁移合集（吐血整理）人类（动物）单人（多人）_2027637518782439426.json、平台全量/极强姿态识别SDPose+Wan2.2 Animate动作迁移方案_2052501347337023490.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Display Any (rgthree)` —— 2/3 个有
- `DownloadAndLoadNLFModel` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `NLFPredict` —— 2/3 个有
- `PoseDetectionVitPoseToDWPose` —— 2/3 个有
- `RenderNLFPoses` —— 2/3 个有
- `SDPoseOODLoader` —— 2/3 个有
- `SDPoseOODProcessor` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Float` —— 1/3 个有
- `Int` —— 1/3 个有
- `PixelPerfectResolution` —— 1/3 个有
- `PoseDetectionOneToAllAnimation` —— 1/3 个有
- `YOLOModelLoader` —— 1/3 个有
- `easy getNode` —— 1/3 个有
- `easy setNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
