---
name: unknown_workflow_video_lora_sampler_106
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.7345
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_2003025271127175169.json, 视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_uni3c_2003035793427972097.json, 视频生成/图生视频/【遇见AI】SCAIL-Pose姿势迁移，支持丝滑转身，支持双人对打_2000492359223832578.json, 视频生成/图生视频/一键SCAIL多只宠物跳舞_2014755319490023425.json, 视频生成/图生视频/丝滑动作迁移-SCAIL无限人数版_2001543214261780482.json, 视频生成/图生视频/动作迁移-丝滑转身-SCAIL_2001524857722531841.json, 视频生成/图生视频/动作迁移SCAIL-48G_2004839644334354433.json, 视频生成/图生视频/动作迁移支持手部细节（单人）SCAIL支持丝滑转身_2000804833005367297.json, 视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）2.0_2001144706195222530.json, 视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）_2001092437491712001.json, 视频生成/图生视频/动作迁移（双人）SCAIL支持丝滑转身支持双人对打_2000796264725872641.json, 视频生成/图生视频/动作迁移（双人）SCAIL（支持丝滑转身、双人对打）2.0_2001142236438032385.json, 视频生成/图生视频/动作迁移（双人）SCAIL（支持丝滑转身、双人对打）_2001090043416543233.json, 视频生成/图生视频/支持丝滑转身_2003660932444266497.json, 视频生成/图生视频/最新SCAIL动作迁移美女跳舞，支持双人对战_2000446117890359297.json, 视频生成/文生视频/SCAIL 动物多人跳舞小猫小狗人物跳舞视频工作流 scaila 多人跳舞跨物种舞蹈模仿单人跳舞_2015990564986036225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_2003025271127175169.json、视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_uni3c_2003035793427972097.json、视频生成/图生视频/【遇见AI】SCAIL-Pose姿势迁移，支持丝滑转身，支持双人对打_2000492359223832578.json、视频生成/图生视频/一键SCAIL多只宠物跳舞_2014755319490023425.json、视频生成/图生视频/丝滑动作迁移-SCAIL无限人数版_2001543214261780482.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 15/16 个有
- `WanVideoEncode` —— 15/16 个有
- `WanVideoUni3C_ControlnetLoader` —— 15/16 个有
- `WanVideoUni3C_embeds` —— 15/16 个有
- `NLFPredict` —— 14/16 个有
- `OnnxDetectionModelLoader` —— 14/16 个有
- `PoseDetectionVitPoseToDWPose` —— 14/16 个有
- `RenderNLFPoses` —— 14/16 个有
- `DownloadAndLoadNLFModel` —— 13/16 个有
- `FloatConstant` —— 13/16 个有
- `ImageConcatMulti` —— 13/16 个有
- `LoadWanVideoT5TextEncoder` —— 13/16 个有
- `SimpleMath+` —— 13/16 个有
- `WanVideoTextEncode` —— 13/16 个有
- `WanVideoTorchCompileSettings` —— 13/16 个有
- `GetNode` —— 12/16 个有
- `INTConstant` —— 12/16 个有
- `SetNode` —— 12/16 个有
- `CR Text` —— 9/16 个有
- `Int` —— 8/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/16 个有
- `MathExpression|pysssss` —— 7/16 个有
- `PreviewImage` —— 3/16 个有
- `WanVideoTextEncodeCached` —— 3/16 个有
- `Bookmark (rgthree)` —— 2/16 个有
- `MemoryCleaner` —— 2/16 个有
- `easy cleanGpuUsed` —— 2/16 个有
- `easy int` —— 2/16 个有
- `Amage Text` —— 1/16 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 1/16 个有
- `DWPreprocessor` —— 1/16 个有
- `Display Any (rgthree)` —— 1/16 个有
- `JWInteger` —— 1/16 个有
- `LoadNLFModel` —— 1/16 个有
- `Seed` —— 1/16 个有
- `SimpleCalculatorKJ` —— 1/16 个有
- `VHS_VideoInfoSource` —— 1/16 个有
- `easy boolean` —— 1/16 个有
- `ttN seed` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
