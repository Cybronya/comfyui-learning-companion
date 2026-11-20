---
name: unknown_workflow_video_lora_sampler_82
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.7154
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_2003025271127175169.json, 视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_uni3c_2003035793427972097.json, 视频生成/图生视频/【遇见AI】SCAIL-Pose姿势迁移，支持丝滑转身，支持双人对打_2000492359223832578.json, 视频生成/图生视频/一键SCAIL多只宠物跳舞_2014755319490023425.json, 视频生成/图生视频/丝滑动作迁移-SCAIL无限人数版_2001543214261780482.json, 视频生成/图生视频/动作迁移-丝滑转身-SCAIL_2001524857722531841.json, 视频生成/图生视频/动作迁移支持手部细节（单人）SCAIL支持丝滑转身_2000804833005367297.json, 视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）2.0_2001144706195222530.json, 视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）_2001092437491712001.json, 视频生成/图生视频/动作迁移（双人）SCAIL支持丝滑转身支持双人对打_2000796264725872641.json, 视频生成/图生视频/动作迁移（双人）SCAIL（支持丝滑转身、双人对打）2.0_2001142236438032385.json, 视频生成/图生视频/动作迁移（双人）SCAIL（支持丝滑转身、双人对打）_2001090043416543233.json, 视频生成/图生视频/动作运镜最强迁移-SCAIL_3D单人、多人姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2018306523847467009.json, 视频生成/图生视频/动作运镜最强迁移-SCAIL_3D单人、多人姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2023998769439711234.json, 视频生成/图生视频/单人多人动作迁移 运镜迁移 Scail-一键切换综合版_2002182497679077377.json, 视频生成/图生视频/多人动作迁移 单人动作迁移 Scail综合版_1996588683803369474.json, 视频生成/图生视频/多人动作迁移 单人动作迁移 Scail综合版_2058885569916264450.json, 视频生成/图生视频/最新SCAIL动作迁移美女跳舞，支持双人对战_2000446117890359297.json, 视频生成/图生视频/萌宠跳舞-动作运镜最强迁移-SCAIL_姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2018335059614375937.json, 视频生成/图生视频/角色动作迁移模仿-人物动物姿态驱动-骨骼对齐-运镜控制-360度旋转【公众号：70后教你做自媒体】_2066354482107207682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_82

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_2003025271127175169.json、视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_uni3c_2003035793427972097.json、视频生成/图生视频/【遇见AI】SCAIL-Pose姿势迁移，支持丝滑转身，支持双人对打_2000492359223832578.json、视频生成/图生视频/一键SCAIL多只宠物跳舞_2014755319490023425.json、视频生成/图生视频/丝滑动作迁移-SCAIL无限人数版_2001543214261780482.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 20 个 workflow 都包含：
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
- `GetImageSizeAndCount` —— 19/20 个有
- `WanVideoEncode` —— 19/20 个有
- `WanVideoUni3C_ControlnetLoader` —— 19/20 个有
- `WanVideoUni3C_embeds` —— 19/20 个有
- `NLFPredict` —— 18/20 个有
- `OnnxDetectionModelLoader` —— 18/20 个有
- `PoseDetectionVitPoseToDWPose` —— 18/20 个有
- `RenderNLFPoses` —— 18/20 个有
- `GetNode` —— 17/20 个有
- `INTConstant` —— 17/20 个有
- `LoadWanVideoT5TextEncoder` —— 17/20 个有
- `SetNode` —— 17/20 个有
- `SimpleMath+` —— 17/20 个有
- `WanVideoTextEncode` —— 17/20 个有
- `WanVideoTorchCompileSettings` —— 17/20 个有
- `FloatConstant` —— 15/20 个有
- `ImageConcatMulti` —— 15/20 个有
- `DownloadAndLoadNLFModel` —— 10/20 个有
- `Int` —— 10/20 个有
- `CR Text` —— 9/20 个有
- `LoadNLFModel` —— 8/20 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 7/20 个有
- `DWPreprocessor` —— 7/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/20 个有
- `MathExpression|pysssss` —— 6/20 个有
- `easy cleanGpuUsed` —— 5/20 个有
- `CustomAddLabel` —— 3/20 个有
- `JjkText` —— 3/20 个有
- `Label (rgthree)` —— 3/20 个有
- `PreviewImage` —— 3/20 个有
- `TwoWaySwitch` —— 3/20 个有
- `WanVideoTextEncodeCached` —— 3/20 个有
- `intToFloat _O` —— 3/20 个有
- `easy int` —— 2/20 个有
- `Bookmark (rgthree)` —— 1/20 个有
- `MemoryCleaner` —— 1/20 个有
- `Seed` —— 1/20 个有
- `SimpleCalculatorKJ` —— 1/20 个有
- `TTResolutionSelector` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
