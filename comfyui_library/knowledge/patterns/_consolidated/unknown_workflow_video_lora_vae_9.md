---
name: unknown_workflow_video_lora_vae_9
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4462
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetNode, GrowMaskWithBlur, ImageFromBatch, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SeCModelLoader, SeCVideoSegmentation, SetNode, Text, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/【二创优选】  Wan2.2 AV2+SeC遮罩（不丢帧、识别精确、速度快）_2031268309001310209.json, 平台全量/视频换人换背景自动识别升级版_2016427828908134401.json, 平台全量/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2001649570004254721.json, 数字人/数字人/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097.json, 视频生成/图生视频/人物替换+动作迁移：Wan2.2AnimateV2+Sa2VA+SeC最强遮罩_1992222168801144834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_9

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/【二创优选】  Wan2.2 AV2+SeC遮罩（不丢帧、识别精确、速度快）_2031268309001310209.json、平台全量/视频换人换背景自动识别升级版_2016427828908134401.json、平台全量/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2001649570004254721.json、数字人/数字人/视频换背景+人物替换：Wan2.2AnimateV2+Sa2VA+SeC_2003042420428292097.json、视频生成/图生视频/人物替换+动作迁移：Wan2.2AnimateV2+Sa2VA+SeC最强遮罩_1992222168801144834.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_MaskPreview` —— 4/5 个有
- `CoordinatePlotter` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `MaskPreview+` —— 4/5 个有
- `PointsEditor` —— 4/5 个有
- `SDPoseOODLoader` —— 4/5 个有
- `SDPoseOODProcessor` —— 4/5 个有
- `Sa2VANodeTpl` —— 4/5 个有
- `WanVideoSamplerExtraArgs` —— 4/5 个有
- `WanVideoSamplerv2` —— 4/5 个有
- `WanVideoSchedulerv2` —— 4/5 个有
- `WanVideoSetBlockSwap` —— 4/5 个有
- `YOLOModelLoader` —— 4/5 个有
- `AdaptiveWanVideoAnimateEmbeds` —— 3/5 个有
- `VHS_VideoInfo` —— 3/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 2/5 个有
- `Float` —— 2/5 个有
- `ImageBlend` —— 2/5 个有
- `InvertMask` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `VHS_VideoInfoLoaded` —— 2/5 个有
- `WanVideoAnimateEmbeds` —— 2/5 个有
- `WanVideoSampler` —— 2/5 个有
- `easy convertAnything` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `workflow>Frame Padder-1` —— 2/5 个有
- `workflow>Frame Padder-2` —— 2/5 个有
- `BatchCount+` —— 1/5 个有
- `DrawViTPose` —— 1/5 个有
- `Evaluate Integers` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `ImageBatch` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RepeatImageBatch` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
