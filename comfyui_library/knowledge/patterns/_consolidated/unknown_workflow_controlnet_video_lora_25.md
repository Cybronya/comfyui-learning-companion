---
name: unknown_workflow_controlnet_video_lora_25
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.458
common_nodes: [Any Switch (rgthree), CLIPVisionLoader, CR Text, DWPreprocessor, Fast Groups Bypasser (rgthree), FastUnsharpSharpen, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SDPoseOODLoader, SDPoseOODProcessor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [图片生成/图生图/【法外狂徒】动作迁移长视频，适合真人、CG、人物替换_2015383660786094082.json, 图片生成/图生图/动作迁移二次元优化版_2022588261209743361.json, 数字人/数字人/动作迁移长视频，适合真人、CG_2022584907335213057.json, 视频生成/图生视频/动作迁移长视频_2031341857254416385.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_25

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【法外狂徒】动作迁移长视频，适合真人、CG、人物替换_2015383660786094082.json、图片生成/图生图/动作迁移二次元优化版_2022588261209743361.json、数字人/数字人/动作迁移长视频，适合真人、CG_2022584907335213057.json、视频生成/图生视频/动作迁移长视频_2031341857254416385.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPVisionLoader`
- `CR Text`
- `DWPreprocessor`
- `Fast Groups Bypasser (rgthree)`
- `FastUnsharpSharpen`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 1/4 个有
- `BlockifyMask` —— 1/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `GrowMask` —— 1/4 个有
- `ImageCombine` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LoadNLFModel` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `NLFPredict` —— 1/4 个有
- `PoseDetectionVitPoseToDWPose` —— 1/4 个有
- `RenderNLFPoses` —— 1/4 个有
- `RepeatImageBatch` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `easy framesEditor` —— 1/4 个有
- `easy mathInt` —— 1/4 个有
- `easy sam3ModelLoader` —— 1/4 个有
- `easy sam3VideoModelExtraConfig` —— 1/4 个有
- `easy sam3VideoSegmentation` —— 1/4 个有
- `easy sam3Visualization` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
