---
name: unknown_workflow_video_lora_sampler_147
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.541
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetNode, GrowMask, INTConstant, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2_Animate_14B视频人物替换（gguf配置，可以本地运行）_1969709240275378178.json, 视频生成/图生视频/wanvideo2.2_Animate动画模型-视频动作迁移_1969437139119337473.json, 视频生成/图生视频/动作迁移_2017571137424723969.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042478976223940610.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042488839909937154.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2044301999423889409.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2047561888975822849.json, 视频生成/图生视频/多人镜头替换工具-MM_1970004050341208065.json, 视频生成/图生视频/最新WanAnimate之视频换装_1971421860208558082.json, 视频生成/图生视频/绝对王炸！Wan2.2 Animate 无限长度姿势控制参考图像到 AI 视频 工作流_1969703350885380098.json, 视频生成/图生视频/角色替换+动作参考_2000210160024944641.json, 视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_1969435322595635201.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_147

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/wan2.2_Animate_14B视频人物替换（gguf配置，可以本地运行）_1969709240275378178.json、视频生成/图生视频/wanvideo2.2_Animate动画模型-视频动作迁移_1969437139119337473.json、视频生成/图生视频/动作迁移_2017571137424723969.json、视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042478976223940610.json、视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042488839909937154.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 12 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GrowMask`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 11/12 个有
- `GetImageSizeAndCount` —— 11/12 个有
- `ImageConcatMulti` —— 11/12 个有
- `PointsEditor` —— 11/12 个有
- `Sam2Segmentation` —— 11/12 个有
- `WanVideoTorchCompileSettings` —— 11/12 个有
- `WanVideoContextOptions` —— 10/12 个有
- `WanVideoTextEncodeCached` —— 10/12 个有
- `AudioCropProcessUTK` —— 6/12 个有
- `GetImageRangeFromBatch` —— 6/12 个有
- `PreviewImage` —— 6/12 个有
- `CLIPLoader` —— 2/12 个有
- `CLIPTextEncode` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `GetImageSize` —— 2/12 个有
- `WanVideoTextEmbedBridge` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `InspyrenetRembgAdvanced` —— 1/12 个有
- `PreviewAnimation` —— 1/12 个有
- `RIFEInterpolation` —— 1/12 个有
- `UNETLoader` —— 1/12 个有
- `UltimateSDUpscaleNoUpscale` —— 1/12 个有
- `VAELoader` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
