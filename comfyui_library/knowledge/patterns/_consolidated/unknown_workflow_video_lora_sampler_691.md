---
name: unknown_workflow_video_lora_sampler_691
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.724
common_nodes: [CLIPVisionLoader, DWPreprocessor, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/wan2.2动作迁移、动作模仿_1984949634684633090.json, 平台全量/【让手办跳出魔性舞蹈！】Wan Animate动作模仿 + ComfyUI实战教程_1969947200048558081.json, 平台全量/工作流基础系列23-Wan2.2-Animate-动作迁移基础工作流_2057671538660429825.json, 平台全量/工作流系列12-Wan2.2-Animate-动作迁移单人半身版本_2058867117709160450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_691

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/wan2.2动作迁移、动作模仿_1984949634684633090.json、平台全量/【让手办跳出魔性舞蹈！】Wan Animate动作模仿 + ComfyUI实战教程_1969947200048558081.json、平台全量/工作流基础系列23-Wan2.2-Animate-动作迁移基础工作流_2057671538660429825.json、平台全量/工作流系列12-Wan2.2-Animate-动作迁移单人半身版本_2058867117709160450.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 3/4 个有
- `FaceMaskFromPoseKeypoints` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `ImageCropByMaskAndResize` —— 3/4 个有
- `PixelPerfectResolution` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `WanVideoAnimateEmbeds` —— 3/4 个有
- `WanVideoContextOptions` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `DrawViTPose` —— 2/4 个有
- `LayerUtility: NumberCalculatorV2` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `OnnxDetectionModelLoader` —— 2/4 个有
- `PoseAndFaceDetection` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `BodyRatioMapperProportionTransfer` —— 1/4 个有
- `BodyRatioMapperSDPoseRender` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `SDPoseKeypointExtractor` —— 1/4 个有
- `Switch any [Crystools]` —— 1/4 个有
- `Text` —— 1/4 个有
- `VHS_VideoInfoSource` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
