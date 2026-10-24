---
name: unknown_workflow_controlnet_video_lora_6
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8073
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/SCALL动作迁移 【最新最强】_2001279614733385729.json, 视频生成/图生视频/(卡通-脸部识别)Scail双人动作迁移(720P高质量版)V2_2001008301930315778.json, 视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001007812647976961.json, 视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001114999428968450.json, 视频生成/图生视频/(（自用）-脸部识别版)Scail双人动作迁移(720P高质量版)V3_2000985576838922241.json, 视频生成/图生视频/02.16gSCAIL多人_2002262972904947714.json, 视频生成/图生视频/044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json, 视频生成/图生视频/ScaiL单_双人动作迁移-舞蹈、口播、带货-数字人_2003735062367641602.json, 视频生成/图生视频/ScaiL单_双人动作迁移-舞蹈、口播、带货-数字人_2004016053883682817.json, 视频生成/图生视频/Scail动作迁移_2001603322555559938.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/SCALL动作迁移 【最新最强】_2001279614733385729.json、视频生成/图生视频/(卡通-脸部识别)Scail双人动作迁移(720P高质量版)V2_2001008301930315778.json、视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001007812647976961.json、视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001114999428968450.json、视频生成/图生视频/(（自用）-脸部识别版)Scail双人动作迁移(720P高质量版)V3_2000985576838922241.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
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
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 9/10 个有
- `ImageConcatMulti` —— 8/10 个有
- `CR Prompt Text` —— 7/10 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 7/10 个有
- `DWPreprocessor` —— 7/10 个有
- `JWInteger` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `MathExpression|pysssss` —— 7/10 个有
- `RunningHub Deepcleaner` —— 7/10 个有
- `PDIMAGE_LongerSize` —— 5/10 个有
- `GetNode` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `SimpleMath+` —— 4/10 个有
- `FloatConstant` —— 2/10 个有
- `Int` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `WanVideoTorchCompileSettings` —— 2/10 个有
- `CM_IntToFloat` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `DF_Int_to_Float` —— 1/10 个有
- `DuckHideNode` —— 1/10 个有
- `Fast Bypasser (rgthree)` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageScaleDownBy` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `Inversed Switch` —— 1/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有
- `easy imageSize` —— 1/10 个有
- `easy int` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
