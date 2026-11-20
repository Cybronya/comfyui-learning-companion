---
name: unknown_workflow_controlnet_video_lora_33
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.464
common_nodes: [BBoxYOLO, BodyRatioMapperProportionTransfer, BodyRatioMapperSDPoseRender, CLIPVisionLoader, CR Prompt Text, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, ImpactConditionalBranch, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PurgeVRAM_UTK, SDPoseKeypointExtractor, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader, easy compare]
problems: []
missing: []
members: [平台全量/Animate-小孩爱宠Q版萌物比例动作迁移_2047681773076746242.json, 平台全量/图片模仿视频动作-v2.0无缩放_2058872137120833537.json, 平台全量/图片模仿视频动作-v2.0自动缩放_2058898312429920258.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_33

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Animate-小孩爱宠Q版萌物比例动作迁移_2047681773076746242.json、平台全量/图片模仿视频动作-v2.0无缩放_2058872137120833537.json、平台全量/图片模仿视频动作-v2.0自动缩放_2058898312429920258.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 3 个 workflow 都包含：
- `BBoxYOLO`
- `BodyRatioMapperProportionTransfer`
- `BodyRatioMapperSDPoseRender`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PurgeVRAM_UTK`
- `SDPoseKeypointExtractor`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy compare`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `BatchCount+` —— 2/3 个有
- `DrawViTPose` —— 2/3 个有
- `FloatConstant` —— 2/3 个有
- `ImageBatch` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `RTDETR_detect` —— 2/3 个有
- `RepeatImageBatch` —— 2/3 个有
- `SDPoseDrawKeypoints` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `easy boolean` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Image Sharpen FS` —— 1/3 个有
- `Int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
