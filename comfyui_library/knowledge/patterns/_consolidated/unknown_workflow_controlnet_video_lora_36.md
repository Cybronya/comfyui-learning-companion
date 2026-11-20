---
name: unknown_workflow_controlnet_video_lora_36
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.504
common_nodes: [BBoxYOLO, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, CLIPVisionLoader, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageResizeKJv2, ImpactConditionalBranch, JjkText, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PlaySound|pysssss, PoseAndFaceDetection, PoseJSONToPoseKeypoint, PoseKeypointPreview, PreviewImage, PrimitiveBoolean, SDPoseKeypointExtractor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [平台全量/merged_wf_v5_2064500324639010818.json, 数字人/数字人/merged_wf_v5_api_2064278343247294465.json, 视频生成/图生视频/Wan2.2+Animate+动作迁移天花板级工作流（加强版）_2069239719984189441.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_36

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/merged_wf_v5_2064500324639010818.json、数字人/数字人/merged_wf_v5_api_2064278343247294465.json、视频生成/图生视频/Wan2.2+Animate+动作迁移天花板级工作流（加强版）_2069239719984189441.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 3 个 workflow 都包含：
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
- `GetImageRangeFromBatch` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageBatchMulti` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_LoadVideoFFmpeg` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `WanVideoSampler` —— 2/3 个有
- `easy int` —— 2/3 个有
- `Notif-PlaySound` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `ShellAgentPluginSaveAudios` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `WanVideoSamplerFromSettings` —— 1/3 个有
- `WanVideoSamplerSettings` —— 1/3 个有
- `WanVideoSetBlockSwap` —— 1/3 个有
- `WanVideoSetLoRAs` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
