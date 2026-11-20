---
name: unknown_workflow_controlnet_video_lora_5
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.880636
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/SCALL动作迁移 【最新最强】_2001279614733385729.json, 数字人/数字人/SCAIL+SDPose+Uni3C动作、运镜最强迁移，宠物跳舞视频_2011427859486744578.json, 视频生成/图生视频/(卡通-脸部识别)Scail双人动作迁移(720P高质量版)V2_2001008301930315778.json, 视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001007812647976961.json, 视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001114999428968450.json, 视频生成/图生视频/(（自用）-脸部识别版)Scail双人动作迁移(720P高质量版)V3_2000985576838922241.json, 视频生成/图生视频/SCAIL+SDPose+Uni3C动作、运镜最强迁移_2028347107450560514.json, 视频生成/图生视频/ScaiL单_双人动作迁移-舞蹈、口播、带货-数字人_2003735062367641602.json, 视频生成/图生视频/ScaiL单_双人动作迁移-舞蹈、口播、带货-数字人_2004016053883682817.json, 视频生成/图生视频/最强多人角色替换工作流-口型动作都能对上_2027264869686317057.json, 视频生成/图生视频/自动骨骼匹配动作迁移_2014181903984762881.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_5

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/SCALL动作迁移 【最新最强】_2001279614733385729.json、数字人/数字人/SCAIL+SDPose+Uni3C动作、运镜最强迁移，宠物跳舞视频_2011427859486744578.json、视频生成/图生视频/(卡通-脸部识别)Scail双人动作迁移(720P高质量版)V2_2001008301930315778.json、视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001007812647976961.json、视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001114999428968450.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ConvertOpenPoseKeypointsToDWPose` —— 10/11 个有
- `DWPreprocessor` —— 10/11 个有
- `GetImageSizeAndCount` —— 10/11 个有
- `ImageConcatMulti` —— 8/11 个有
- `WanVideoSetBlockSwap` —— 7/11 个有
- `WanVideoSetLoRAs` —— 7/11 个有
- `CR Prompt Text` —— 6/11 个有
- `JWInteger` —— 6/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/11 个有
- `MathExpression|pysssss` —— 6/11 个有
- `RunningHub Deepcleaner` —— 6/11 个有
- `SimpleMath+` —— 6/11 个有
- `Int` —— 5/11 个有
- `PDIMAGE_LongerSize` —— 5/11 个有
- `WanVideoTorchCompileSettings` —— 5/11 个有
- `Any Switch (rgthree)` —— 4/11 个有
- `CR Text` —— 4/11 个有
- `Fast Groups Muter (rgthree)` —— 4/11 个有
- `GroundingDinoModelLoader_SDPose` —— 4/11 个有
- `LayerUtility: PurgeVRAM V2` —— 4/11 个有
- `SDPoseOODLoader` —— 4/11 个有
- `SDPoseOODProcessor` —— 4/11 个有
- `YOLOModelLoader` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `GetNode` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `SaveImage` —— 2/11 个有
- `VHS_VideoInfo` —— 2/11 个有
- `BatchThief` —— 1/11 个有
- `CM_IntToFloat` —— 1/11 个有
- `DuckHideNode` —— 1/11 个有
- `ImageScaleDownBy` —— 1/11 个有
- `RH_Nano_Banana2_Image2Image` —— 1/11 个有
- `TT_img_enc` —— 1/11 个有
- `TT_img_enc_v2` —— 1/11 个有
- `easy imageSize` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
