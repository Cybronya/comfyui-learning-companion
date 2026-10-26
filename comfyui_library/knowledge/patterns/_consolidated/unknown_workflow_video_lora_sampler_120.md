---
name: unknown_workflow_video_lora_sampler_120
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.652667
common_nodes: [CLIPVisionLoader, GetNode, ImageConcatMulti, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(单人)_2006028757395578881.json, 视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(多人)_2006202937944576001.json, 视频生成/图生视频/scail 增加晃动lora 跳舞更诱人 自带提示词-抖动_2050494894682189826.json, 视频生成/图生视频/scail 增加晃动lora_2006433739613675522.json, 视频生成/图生视频/scail多人动作迁移_2015612655679053825.json, 视频生成/图生视频/scail多人动作迁移_2031033766637998081.json, 视频生成/图生视频/wanvideo_SCAIL_basic_pose_control_workflow_2000760906177015810.json, 视频生成/图生视频/wanvideo_SCAIL_pose and camera_control_workflow_2000851201182793729.json, 视频生成/图生视频/【动迁】Wan_SCAIL动作迁移+Light2v加速_2005453601126445058.json, 视频生成/图生视频/【多人】SCAIL Video Multi-Character Motion Transfer V1_2002334338010234881.json, 视频生成/图生视频/动作运镜最强迁移-SCAIL_3D单人、多人姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2018306523847467009.json, 视频生成/图生视频/动作运镜最强迁移-SCAIL_3D单人、多人姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2023998769439711234.json, 视频生成/图生视频/萌宠跳舞-动作运镜最强迁移-SCAIL_姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2018335059614375937.json, 视频生成/图生视频/角色动作迁移模仿-人物动物姿态驱动-骨骼对齐-运镜控制-360度旋转【公众号：70后教你做自媒体】_2066354482107207682.json, 视频生成/图生视频/🐱Scail模型-单双人视频动作迁移-言灵ru😼_2002394851083730946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(单人)_2006028757395578881.json、视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(多人)_2006202937944576001.json、视频生成/图生视频/scail 增加晃动lora 跳舞更诱人 自带提示词-抖动_2050494894682189826.json、视频生成/图生视频/scail 增加晃动lora_2006433739613675522.json、视频生成/图生视频/scail多人动作迁移_2015612655679053825.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 13/15 个有
- `WanVideoLoraSelect` —— 13/15 个有
- `INTConstant` —— 12/15 个有
- `DownloadAndLoadNLFModel` —— 11/15 个有
- `WanVideoEncode` —— 11/15 个有
- `WanVideoUni3C_ControlnetLoader` —— 11/15 个有
- `WanVideoUni3C_embeds` —— 11/15 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 9/15 个有
- `DWPreprocessor` —— 9/15 个有
- `LoadWanVideoT5TextEncoder` —— 9/15 个有
- `SimpleMath+` —— 9/15 个有
- `WanVideoTextEncode` —— 9/15 个有
- `FloatConstant` —— 8/15 个有
- `WanVideoTorchCompileSettings` —— 8/15 个有
- `SimpleCalculatorKJ` —— 6/15 个有
- `WanVideoTextEncodeCached` —— 6/15 个有
- `Label (rgthree)` —— 5/15 个有
- `LoadNLFModel` —— 4/15 个有
- `PreviewImage` —— 4/15 个有
- `CustomAddLabel` —— 3/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/15 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/15 个有
- `GIMMVFI_interpolate` —— 2/15 个有
- `LayerUtility: PurgeVRAM V2` —— 2/15 个有
- `Text Multiline` —— 2/15 个有
- `WanVideoLoraSelectMulti` —— 2/15 个有
- `CR Prompt Text` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `Int` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有
- `TTResolutionSelector` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有
- `easy showAnything` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
