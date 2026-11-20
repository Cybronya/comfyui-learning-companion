---
name: unknown_workflow_video_lora_sampler_231
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.766545
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Scail 一键跳舞！骨骼完美驱动！_2001570151873015810.json, 平台全量/Scail 最强动作迁移_PLUS模式运行_2005661946890383361.json, 平台全量/Scail单_双人动作迁移自由切换版_2000863323744763906.json, 平台全量/Scail单人动作迁移(720P高质量版)V2_2001623314743345153.json, 平台全量/WanVideo SCAIL Context LongLength - SCAIL上下文长视频_2001122624182812674.json, 平台全量/Wanvideo SCAIL 动作和镜头控制_2001578961287147521.json, 平台全量/scail 增加晃动lora 跳舞更诱人 自带提示词_2001830125261975554.json, 平台全量/【舞蹈】超稳舞蹈Scail单_双人动作迁移_2030222144050827266.json, 视频生成/图生视频/(卡通-脸部识别)Scail双人动作迁移(720P高质量版)V2_2001008301930315778.json, 视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001007812647976961.json, 视频生成/图生视频/(脸部识别版)Scail多人动作迁移(720P高质量版)V2_2001114999428968450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_231

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Scail 一键跳舞！骨骼完美驱动！_2001570151873015810.json、平台全量/Scail 最强动作迁移_PLUS模式运行_2005661946890383361.json、平台全量/Scail单_双人动作迁移自由切换版_2000863323744763906.json、平台全量/Scail单人动作迁移(720P高质量版)V2_2001623314743345153.json、平台全量/WanVideo SCAIL Context LongLength - SCAIL上下文长视频_2001122624182812674.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
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
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadNLFModel` —— 10/11 个有
- `GetImageSizeAndCount` —— 10/11 个有
- `ImageConcatMulti` —— 10/11 个有
- `WanVideoLoraSelect` —— 10/11 个有
- `LoadWanVideoT5TextEncoder` —— 9/11 个有
- `WanVideoTextEncode` —— 9/11 个有
- `WanVideoEncode` —— 8/11 个有
- `WanVideoUni3C_ControlnetLoader` —— 8/11 个有
- `WanVideoUni3C_embeds` —— 8/11 个有
- `CR Prompt Text` —— 6/11 个有
- `JWInteger` —— 6/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/11 个有
- `MathExpression|pysssss` —— 6/11 个有
- `PreviewImage` —— 5/11 个有
- `INTConstant` —— 4/11 个有
- `PDIMAGE_LongerSize` —— 4/11 个有
- `RunningHub Deepcleaner` —— 4/11 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 3/11 个有
- `DWPreprocessor` —— 3/11 个有
- `GetNode` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `SimpleMath+` —— 3/11 个有
- `WanVideoTorchCompileSettings` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `FloatConstant` —— 2/11 个有
- `ImageFromBatch+` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `SimpleCalculatorKJ` —— 2/11 个有
- `WanVideoScheduler` —— 2/11 个有
- `WanVideoTextEncodeCached` —— 2/11 个有
- `CM_IntToFloat` —— 1/11 个有
- `CR SDXL Aspect Ratio` —— 1/11 个有
- `LoadNLFModel` —— 1/11 个有
- `MuyeTextEditOutput` —— 1/11 个有
- `PIP_IntegerCalculator` —— 1/11 个有
- `WanVideoLoraSelectMulti` —— 1/11 个有
- `WanVideoSampler` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
