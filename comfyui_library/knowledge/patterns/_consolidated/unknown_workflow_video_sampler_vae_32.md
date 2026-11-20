---
name: unknown_workflow_video_sampler_vae_32
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.692333
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, ImageConcatMulti, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(单人)_2006028757395578881.json, 视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(多人)_2006202937944576001.json, 视频生成/图生视频/scail 增加晃动lora 跳舞更诱人 自带提示词-抖动_2050494894682189826.json, 视频生成/图生视频/scail 增加晃动lora_2006433739613675522.json, 视频生成/图生视频/scail多人动作迁移_2015612655679053825.json, 视频生成/图生视频/scail多人动作迁移_2031033766637998081.json, 视频生成/图生视频/wanvideo_SCAIL_basic_pose_control_workflow_2000760906177015810.json, 视频生成/图生视频/wanvideo_SCAIL_pose and camera_control_workflow_2000851201182793729.json, 视频生成/图生视频/【动迁】Wan_SCAIL动作迁移+Light2v加速_2005453601126445058.json, 视频生成/图生视频/【多人】SCAIL Video Multi-Character Motion Transfer V1_2002334338010234881.json, 视频生成/图生视频/骨骼自适应SCAIL多人跳舞或单人跳舞_2001528036937854977.json, 视频生成/图生视频/骨骼自适应SCAIL多人跳舞或单人跳舞scail小猫小狗人物多人跳舞单人跳舞_2014606161722482689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_32

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(单人)_2006028757395578881.json、视频生成/图生视频/Wan_SCAIL_视频3D动作迁移(多人)_2006202937944576001.json、视频生成/图生视频/scail 增加晃动lora 跳舞更诱人 自带提示词-抖动_2050494894682189826.json、视频生成/图生视频/scail 增加晃动lora_2006433739613675522.json、视频生成/图生视频/scail多人动作迁移_2015612655679053825.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
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
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 10/12 个有
- `GetNode` —— 10/12 个有
- `SetNode` —— 10/12 个有
- `WanVideoLoraSelect` —— 10/12 个有
- `WanVideoSetBlockSwap` —— 10/12 个有
- `WanVideoSetLoRAs` —— 10/12 个有
- `WanVideoEncode` —— 8/12 个有
- `WanVideoUni3C_ControlnetLoader` —— 8/12 个有
- `WanVideoUni3C_embeds` —— 8/12 个有
- `INTConstant` —— 7/12 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 6/12 个有
- `DWPreprocessor` —— 6/12 个有
- `LoadWanVideoT5TextEncoder` —— 6/12 个有
- `SimpleCalculatorKJ` —— 6/12 个有
- `SimpleMath+` —— 6/12 个有
- `WanVideoTextEncode` —— 6/12 个有
- `WanVideoTextEncodeCached` —— 6/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/12 个有
- `PreviewImage` —— 5/12 个有
- `CR Prompt Text` —— 3/12 个有
- `FloatConstant` —— 3/12 个有
- `WanVideoTorchCompileSettings` —— 3/12 个有
- `Display Any (rgthree)` —— 2/12 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/12 个有
- `GIMMVFI_interpolate` —— 2/12 个有
- `GetImageRangeFromBatch` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `LayerUtility: PurgeVRAM V2` —— 2/12 个有
- `Switch any [Crystools]` —— 2/12 个有
- `Text Multiline` —— 2/12 个有
- `WanVideoLoraSelectMulti` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `Int` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
