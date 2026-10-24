---
name: unknown_workflow_video_lora_sampler_138
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.9045
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Scail动作复刻工作流_2008843749622816769.json, 视频生成/图生视频/Scail动物跳舞工作流_1953472755108904961.json, 视频生成/图生视频/Scail单_双人动作迁移自由切换版_2024108725971193857.json, 视频生成/图生视频/Scail单人动作迁移(720P-Uni3c运镜版)V2_2000630427444539394.json, 视频生成/图生视频/Scail单人动作迁移(720P高质量版)V2_2000617753667137537.json, 视频生成/图生视频/Scail双人动作迁移_2012140955029213186.json, 视频生成/图生视频/Scail多人动作迁移(720P高质量版)V2_2011401964541710338.json, 视频生成/图生视频/Scail多人跳舞，24G版_1954212955724378113.json, 视频生成/图生视频/Scail武术动作，单人动作模仿，可转身，可武术_1995058553109065730.json, 视频生成/图生视频/Scail：单人动作迁移_2003684559344574466.json, 视频生成/图生视频/Wan+Scail多人姿势控制_2001210415457632258.json, 视频生成/图生视频/动作迁移SCAIL-48G_2004839644334354433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_138

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Scail动作复刻工作流_2008843749622816769.json、视频生成/图生视频/Scail动物跳舞工作流_1953472755108904961.json、视频生成/图生视频/Scail单_双人动作迁移自由切换版_2024108725971193857.json、视频生成/图生视频/Scail单人动作迁移(720P-Uni3c运镜版)V2_2000630427444539394.json、视频生成/图生视频/Scail单人动作迁移(720P高质量版)V2_2000617753667137537.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
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
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoContextOptions` —— 11/12 个有
- `WanVideoSamplerExtraArgs` —— 11/12 个有
- `JWInteger` —— 8/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/12 个有
- `MathExpression|pysssss` —— 8/12 个有
- `WanVideoEncode` —— 7/12 个有
- `WanVideoUni3C_ControlnetLoader` —— 7/12 个有
- `WanVideoUni3C_embeds` —— 7/12 个有
- `CR Prompt Text` —— 6/12 个有
- `PDIMAGE_LongerSize` —— 6/12 个有
- `RunningHub Deepcleaner` —— 6/12 个有
- `SimpleMath+` —— 5/12 个有
- `WanVideoTorchCompileSettings` —— 5/12 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 4/12 个有
- `DWPreprocessor` —— 4/12 个有
- `INTConstant` —— 4/12 个有
- `PreviewImage` —— 2/12 个有
- `Amage Text` —— 1/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `Display Any (rgthree)` —— 1/12 个有
- `Evaluate Integers` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `FloatConstant` —— 1/12 个有
- `If ANY execute A else B` —— 1/12 个有
- `ImageFromBatch+` —— 1/12 个有
- `Int` —— 1/12 个有
- `Logic Boolean` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `Text` —— 1/12 个有
- `VHS_VideoInfoSource` —— 1/12 个有
- `easy boolean` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy int` —— 1/12 个有
- `ttN seed` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
