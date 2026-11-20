---
name: unknown_workflow_controlnet_video_lora_24
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8438
common_nodes: [CLIPVisionLoader, CR Prompt Text, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/骨骼自适应SCAIL多人跳舞或单人跳舞_2001528036937854977.json, 视频生成/图生视频/骨骼自适应SCAIL多人跳舞或单人跳舞scail小猫小狗人物多人跳舞单人跳舞_2014606161722482689.json, 视频生成/图生视频/（脸部识别）Scail双人动作迁移(720P高质量版)V4_2000648605100802049.json, 视频生成/图生视频/（自用）Scail单人动作迁移(720P高质量版)V2_2000980028173283329.json, 视频生成/文生视频/Scail单双人动作迁移_2002461334463758338.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/骨骼自适应SCAIL多人跳舞或单人跳舞_2001528036937854977.json、视频生成/图生视频/骨骼自适应SCAIL多人跳舞或单人跳舞scail小猫小狗人物多人跳舞单人跳舞_2014606161722482689.json、视频生成/图生视频/（脸部识别）Scail双人动作迁移(720P高质量版)V4_2000648605100802049.json、视频生成/图生视频/（自用）Scail单人动作迁移(720P高质量版)V2_2000980028173283329.json、视频生成/文生视频/Scail单双人动作迁移_2002461334463758338.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/5 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 3/5 个有
- `DWPreprocessor` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `WanVideoSetBlockSwap` —— 3/5 个有
- `WanVideoSetLoRAs` —— 3/5 个有
- `Display Any (rgthree)` —— 2/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `RunningHub Deepcleaner` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `Switch any [Crystools]` —— 2/5 个有
- `DuckHideNode` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `PDIMAGE_LongerSize` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有
- `TT_img_enc_v2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
