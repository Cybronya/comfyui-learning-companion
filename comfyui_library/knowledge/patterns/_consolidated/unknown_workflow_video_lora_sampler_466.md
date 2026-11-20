---
name: unknown_workflow_video_lora_sampler_466
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5348
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, INTConstant, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/wan-2.2-动作迁移-V3_2058811529675501570.json, 数字人/数字人/wan2.2_Animate_14B视频人物替换_1969312509834502146.json, 视频生成/图生视频/Wan-Animate动作表情迁移不遮罩_1968169520768647170.json, 视频生成/图生视频/wan2.2_Animate_14B视频人物替换（gguf配置，可以本地运行）_1969709240275378178.json, 视频生成/图生视频/绝对王炸！Wan2.2 Animate 无限长度姿势控制参考图像到 AI 视频 工作流_1969703350885380098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_466

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/wan-2.2-动作迁移-V3_2058811529675501570.json、数字人/数字人/wan2.2_Animate_14B视频人物替换_1969312509834502146.json、视频生成/图生视频/Wan-Animate动作表情迁移不遮罩_1968169520768647170.json、视频生成/图生视频/wan2.2_Animate_14B视频人物替换（gguf配置，可以本地运行）_1969709240275378178.json、视频生成/图生视频/绝对王炸！Wan2.2 Animate 无限长度姿势控制参考图像到 AI 视频 工作流_1969703350885380098.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 3/5 个有
- `CLIPLoader` —— 3/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `DrawMaskOnImage` —— 3/5 个有
- `GrowMask` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `WanVideoTextEmbedBridge` —— 3/5 个有
- `WanVideoTextEncodeCached` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `InspyrenetRembgAdvanced` —— 2/5 个有
- `PreviewAnimation` —— 2/5 个有
- `Switch image [Crystools]` —— 2/5 个有
- `VHS_VideoInfoLoaded` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `DownloadAndLoadSAM2Model` —— 1/5 个有
- `Int` —— 1/5 个有
- `PointsEditor` —— 1/5 个有
- `RIFEInterpolation` —— 1/5 个有
- `Sam2Segmentation` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `SeedVR2ExtraArgs` —— 1/5 个有
- `UNETLoader` —— 1/5 个有
- `UltimateSDUpscaleNoUpscale` —— 1/5 个有
- `VAELoader` —— 1/5 个有
- `WanVideoContextOptions` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
