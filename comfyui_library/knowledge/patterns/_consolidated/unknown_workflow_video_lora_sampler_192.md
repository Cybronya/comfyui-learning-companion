---
name: unknown_workflow_video_lora_sampler_192
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8313
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2001603322555559938.json, 视频生成/图生视频/2024108725971193857.json, 视频生成/图生视频/2000630427444539394.json, 视频生成/图生视频/2000617753667137537.json, 视频生成/图生视频/2012140955029213186.json, 视频生成/图生视频/2011401964541710338.json, 视频生成/图生视频/2003684559344574466.json, 视频生成/图生视频/2001210415457632258.json, 视频生成/图生视频/2000648605100802049.json, 视频生成/文生视频/Scail单双人动作迁移_2002461334463758338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_192

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2001603322555559938.json、视频生成/图生视频/2024108725971193857.json、视频生成/图生视频/2000630427444539394.json、视频生成/图生视频/2000617753667137537.json、视频生成/图生视频/2012140955029213186.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
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
- `CR Prompt Text` —— 9/10 个有
- `ImageConcatMulti` —— 9/10 个有
- `WanVideoContextOptions` —— 9/10 个有
- `WanVideoEncode` —— 9/10 个有
- `WanVideoSamplerExtraArgs` —— 9/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 9/10 个有
- `WanVideoUni3C_embeds` —— 9/10 个有
- `RunningHub Deepcleaner` —— 8/10 个有
- `PDIMAGE_LongerSize` —— 7/10 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 4/10 个有
- `DWPreprocessor` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ImageFromBatch+` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `CM_IntToFloat` —— 1/10 个有
- `DF_Int_to_Float` —— 1/10 个有
- `Evaluate Integers` —— 1/10 个有
- `If ANY execute A else B` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `Int` —— 1/10 个有
- `Inversed Switch` —— 1/10 个有
- `Logic Boolean` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `Text` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
