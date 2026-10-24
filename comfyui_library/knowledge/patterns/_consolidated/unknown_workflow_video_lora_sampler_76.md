---
name: unknown_workflow_video_lora_sampler_76
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.653611
common_nodes: [CLIPVisionLoader, GetNode, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(单人)_2006028757395578881.json, 视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(多人)_2006202937944576001.json, 视频生成/图生视频/scail 增加晃动lora 跳舞更诱人 自带提示词-抖动_2050494894682189826.json, 视频生成/图生视频/scail 增加晃动lora_2006433739613675522.json, 视频生成/图生视频/scail多人动作迁移_2015612655679053825.json, 视频生成/图生视频/scail多人动作迁移_2031033766637998081.json, 视频生成/图生视频/wanvideo_SCAIL_basic_pose_control_workflow_2000760906177015810.json, 视频生成/图生视频/wanvideo_SCAIL_pose and camera_control_workflow_2000851201182793729.json, 视频生成/图生视频/【动迁】Wan_SCAIL动作迁移+Light2v加速_2005453601126445058.json, 视频生成/图生视频/【多人】SCAIL Video Multi-Character Motion Transfer V1_2002334338010234881.json, 视频生成/图生视频/动作迁移支持手部细节（单人）SCAIL支持丝滑转身_2000804833005367297.json, 视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）2.0_2001144706195222530.json, 视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）_2001092437491712001.json, 视频生成/图生视频/动作迁移（双人）SCAIL支持丝滑转身支持双人对打_2000796264725872641.json, 视频生成/图生视频/动作迁移（双人）SCAIL（支持丝滑转身、双人对打）2.0_2001142236438032385.json, 视频生成/图生视频/动作迁移（双人）SCAIL（支持丝滑转身、双人对打）_2001090043416543233.json, 视频生成/图生视频/动作运镜最强迁移-SCAIL_3D单人、多人姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2023998769439711234.json, 视频生成/图生视频/影视剧替换人物第二步：视频驱动图片（可多人）_2013510010877251586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(单人)_2006028757395578881.json、视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(多人)_2006202937944576001.json、视频生成/图生视频/scail 增加晃动lora 跳舞更诱人 自带提示词-抖动_2050494894682189826.json、视频生成/图生视频/scail 增加晃动lora_2006433739613675522.json、视频生成/图生视频/scail多人动作迁移_2015612655679053825.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
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
- `DownloadAndLoadNLFModel` —— 17/18 个有
- `ImageConcatMulti` —— 17/18 个有
- `GetImageSizeAndCount` —— 16/18 个有
- `WanVideoLoraSelect` —— 16/18 个有
- `INTConstant` —— 15/18 个有
- `WanVideoEncode` —— 14/18 个有
- `WanVideoUni3C_ControlnetLoader` —— 14/18 个有
- `WanVideoUni3C_embeds` —— 14/18 个有
- `LoadWanVideoT5TextEncoder` —— 12/18 个有
- `SimpleMath+` —— 12/18 个有
- `WanVideoTextEncode` —— 12/18 个有
- `FloatConstant` —— 11/18 个有
- `WanVideoTorchCompileSettings` —— 11/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/18 个有
- `Int` —— 7/18 个有
- `CR Text` —— 6/18 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 6/18 个有
- `DWPreprocessor` —— 6/18 个有
- `MathExpression|pysssss` —— 6/18 个有
- `PreviewImage` —— 6/18 个有
- `SimpleCalculatorKJ` —— 6/18 个有
- `WanVideoTextEncodeCached` —— 6/18 个有
- `Label (rgthree)` —— 3/18 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/18 个有
- `GIMMVFI_interpolate` —— 2/18 个有
- `LayerUtility: PurgeVRAM V2` —— 2/18 个有
- `Text Multiline` —— 2/18 个有
- `WanVideoLoraSelectMulti` —— 2/18 个有
- `CR Prompt Text` —— 1/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `ImpactSwitch` —— 1/18 个有
- `LoadNLFModel` —— 1/18 个有
- `PrimitiveInt` —— 1/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有
- `easy showAnything` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
