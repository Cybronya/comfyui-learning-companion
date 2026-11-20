---
name: unknown_workflow_video_lora_sampler_427
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.748571
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SimpleMath+, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan 2.1 SCAIL 视频人物替换_2062884370725302274.json, 数字人/数字人/Scail 一键跳舞！骨骼完美驱动！_2003096928302899201.json, 数字人/数字人/萌宠跳舞-动作运镜最强迁移-SCAIL_3D单人多人姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2019072391724408834.json, 视频生成/图生视频/02.16gSCAIL多人_2002262972904947714.json, 视频生成/图生视频/12号特工：保留原图场景+SCAIL动作迁移_2026286261522141186.json, 视频生成/图生视频/251220001.01.16gSCAIL单人_2002263013321261058.json, 视频生成/图生视频/251220001.03.SCAIL双角色超动态动作迁移_2002262953242030082.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_427

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Wan 2.1 SCAIL 视频人物替换_2062884370725302274.json、数字人/数字人/Scail 一键跳舞！骨骼完美驱动！_2003096928302899201.json、数字人/数字人/萌宠跳舞-动作运镜最强迁移-SCAIL_3D单人多人姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2019072391724408834.json、视频生成/图生视频/02.16gSCAIL多人_2002262972904947714.json、视频生成/图生视频/12号特工：保留原图场景+SCAIL动作迁移_2026286261522141186.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `SimpleMath+`
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
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `WanVideoSetBlockSwap` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `DownloadAndLoadNLFModel` —— 5/7 个有
- `FloatConstant` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `WanVideoEncode` —— 5/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 5/7 个有
- `WanVideoUni3C_embeds` —— 5/7 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 3/7 个有
- `DWPreprocessor` —— 3/7 个有
- `LoadNLFModel` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `CreateVideo` —— 1/7 个有
- `CustomAddLabel` —— 1/7 个有
- `Float to Int` —— 1/7 个有
- `GetImageSizeRatio` —— 1/7 个有
- `GetVideoComponents` —— 1/7 个有
- `INPAINT_InpaintWithModel` —— 1/7 个有
- `INPAINT_LoadInpaintModel` —— 1/7 个有
- `ImageFromBatch` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `ImageToMask` —— 1/7 个有
- `Int` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LoadVideo` —— 1/7 个有
- `Mask Invert` —— 1/7 个有
- `MaskToImage` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `SaveVideo` —— 1/7 个有
- `SolidMask` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
