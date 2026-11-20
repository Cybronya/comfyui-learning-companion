---
name: unknown_workflow_controlnet_video_lora_32
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4945
common_nodes: [BBoxYOLO, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, CLIPVisionLoader, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageResizeKJv2, ImpactConditionalBranch, JjkText, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PlaySound|pysssss, PoseAndFaceDetection, PoseJSONToPoseKeypoint, PoseKeypointPreview, PreviewImage, PrimitiveBoolean, SDPoseKeypointExtractor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [数字人/数字人/merged_wf_v5_api_2064278343247294465.json, 视频生成/图生视频/Wan2.2+Animate+动作迁移天花板级工作流（加强版）_2069239719984189441.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/merged_wf_v5_api_2064278343247294465.json、视频生成/图生视频/Wan2.2+Animate+动作迁移天花板级工作流（加强版）_2069239719984189441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `BBoxYOLO`
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `JjkText`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PoseAndFaceDetection`
- `PoseJSONToPoseKeypoint`
- `PoseKeypointPreview`
- `PreviewImage`
- `PrimitiveBoolean`
- `SDPoseKeypointExtractor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VHS_LoadVideoFFmpeg` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoSampler` —— 1/2 个有
- `WanVideoSamplerFromSettings` —— 1/2 个有
- `WanVideoSamplerSettings` —— 1/2 个有
- `WanVideoSetBlockSwap` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
