---
name: unknown_workflow_controlnet_video_lora_7
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.4542
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, Fast Groups Bypasser (rgthree), FastUnsharpSharpen, GetNode, GrowMaskWithBlur, INTConstant, ImageBlend, ImageConcatMulti, ImageFlip, ImageResizeKJv2, LoadImage, MaskToImage, OnnxDetectionModelLoader, PlaySound|pysssss, PoseAndFaceDetection, PreviewAny, PreviewImage, SDPoseOODLoader, SDPoseOODProcessor, Seed (rgthree), SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader, easy framesEditor, easy sam3GetObjectIds, easy sam3GetObjectMask, easy sam3ModelLoader, easy sam3VideoModelExtraConfig, easy sam3VideoSegmentation, easy sam3Visualization]
problems: []
missing: []
members: [图片生成/图生图/人物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2012171919730151426.json, 视频生成/图生视频/0219人物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2024420468635209729.json, 视频生成/图生视频/GS-人物替换姿态迁移_2058803362686136321.json, 视频生成/图生视频/WanAnimate Sam3+SD-Pose  人物替换+姿态迁移_2078667744270180354.json, 视频生成/图生视频/WanAnimate+Sam3+SD-Pose+物替换&姿态迁移+最强工作流!!+_2064168504852566018.json, 视频生成/图生视频/人物替换&姿态迁移 WanAnimate Sam3+SD-Pose_2015028362657406978.json, 视频生成/图生视频/人物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2064313461764612097.json, 视频生成/图生视频/人物替换&姿态迁移_2044048131473547266.json, 视频生成/图生视频/自用 人物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2026672367019237377.json, 视频生成/图生视频/舞蹈迁移-自用_2062211912280137730.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/人物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2012171919730151426.json、视频生成/图生视频/0219人物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2024420468635209729.json、视频生成/图生视频/GS-人物替换姿态迁移_2058803362686136321.json、视频生成/图生视频/WanAnimate Sam3+SD-Pose  人物替换+姿态迁移_2078667744270180354.json、视频生成/图生视频/WanAnimate+Sam3+SD-Pose+物替换&姿态迁移+最强工作流!!+_2064168504852566018.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 10 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `FastUnsharpSharpen`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageBlend`
- `ImageConcatMulti`
- `ImageFlip`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskToImage`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PoseAndFaceDetection`
- `PreviewAny`
- `PreviewImage`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `Seed (rgthree)`
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
- `easy framesEditor`
- `easy sam3GetObjectIds`
- `easy sam3GetObjectMask`
- `easy sam3ModelLoader`
- `easy sam3VideoModelExtraConfig`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 9/10 个有
- `WanVideoContextOptions` —— 8/10 个有
- `Label (rgthree)` —— 3/10 个有
- `LamCommonPrint` —— 3/10 个有
- `孤海注释` —— 2/10 个有
- `DF_Int_to_Float` —— 1/10 个有
- `ImageResizeKJ` —— 1/10 个有
- `ImageUpscaleWithModel` —— 1/10 个有
- `ImpactConditionalBranch` —— 1/10 个有
- `Int` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `RH_Captioner` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `UpscaleModelLoader` —— 1/10 个有
- `easy compare` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
