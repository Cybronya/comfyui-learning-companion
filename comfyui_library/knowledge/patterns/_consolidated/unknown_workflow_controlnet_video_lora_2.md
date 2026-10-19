---
name: unknown_workflow_controlnet_video_lora_2
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.671684
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, NLFPredict, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2012926675255828482.json, 视频生成/图生视频/2000549729010319361.json, 视频生成/图生视频/2000605226488954881.json, 视频生成/图生视频/2000601327501705218.json, 视频生成/图生视频/2001380320773537793.json, 视频生成/图生视频/2001114629822705666.json, 视频生成/图生视频/2002634251973607426.json, 视频生成/图生视频/2001969039012446209.json, 视频生成/图生视频/2002968528913350658.json, 视频生成/图生视频/2001265311133429761.json, 视频生成/图生视频/2000519506155929601.json, 视频生成/图生视频/2000804833005367297.json, 视频生成/图生视频/2001144706195222530.json, 视频生成/图生视频/2001092437491712001.json, 视频生成/图生视频/2000796264725872641.json, 视频生成/图生视频/2001142236438032385.json, 视频生成/图生视频/2001090043416543233.json, 视频生成/图生视频/2000521244929818626.json, 视频生成/图生视频/2002394851083730946.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_2

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/2012926675255828482.json、视频生成/图生视频/2000549729010319361.json、视频生成/图生视频/2000605226488954881.json、视频生成/图生视频/2000601327501705218.json、视频生成/图生视频/2001380320773537793.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
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
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoSetLoRAs` —— 18/19 个有
- `GetNode` —— 17/19 个有
- `SetNode` —— 17/19 个有
- `SimpleMath+` —— 17/19 个有
- `WanVideoTorchCompileSettings` —— 17/19 个有
- `ImageConcatMulti` —— 16/19 个有
- `LoadWanVideoT5TextEncoder` —— 16/19 个有
- `OnnxDetectionModelLoader` —— 16/19 个有
- `PoseDetectionVitPoseToDWPose` —— 16/19 个有
- `WanVideoSetBlockSwap` —— 16/19 个有
- `WanVideoTextEncode` —— 16/19 个有
- `INTConstant` —— 13/19 个有
- `FloatConstant` —— 10/19 个有
- `Int` —— 10/19 个有
- `PreviewImage` —— 9/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/19 个有
- `CR Text` —— 7/19 个有
- `MathExpression|pysssss` —— 6/19 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 5/19 个有
- `DWPreprocessor` —— 5/19 个有
- `Fast Groups Muter (rgthree)` —— 3/19 个有
- `WanVideoTextEncodeCached` —— 3/19 个有
- `easy showAnything` —— 3/19 个有
- `ImageFromBatch` —— 2/19 个有
- `JjkText` —— 2/19 个有
- `Primitive integer [Crystools]` —— 2/19 个有
- `SimpleCalculatorKJ` —— 2/19 个有
- `GetImage` —— 1/19 个有
- `ImageFromBatch+` —— 1/19 个有
- `JWInteger` —— 1/19 个有
- `LayerUtility: PurgeVRAM V2` —— 1/19 个有
- `PixelPerfectResolution` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
