---
name: unknown_workflow_video_lora_sampler_240
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.6115
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GrowMask, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2055549996304478210.json, 视频生成/图生视频/1981708744444780545.json, 视频生成/图生视频/1981690387544842241.json, 视频生成/图生视频/1992566625708691457.json, 视频生成/图生视频/1969765016436154369.json, 视频生成/图生视频/1971382393225592834.json, 视频生成/图生视频/1971226836661420034.json, 视频生成/图生视频/1969270955216412673.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_240

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2055549996304478210.json、视频生成/图生视频/1981708744444780545.json、视频生成/图生视频/1981690387544842241.json、视频生成/图生视频/1992566625708691457.json、视频生成/图生视频/1969765016436154369.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 8 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `WanVideoLoraSelectMulti` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `DownloadAndLoadSAM2Model` —— 6/8 个有
- `GetImageSizeAndCount` —— 6/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `PointsEditor` —— 6/8 个有
- `Sam2Segmentation` —— 6/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `VHS_VideoInfo` —— 4/8 个有
- `INTConstant` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `Text` —— 3/8 个有
- `WanVideoEncode` —— 3/8 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/8 个有
- `WanVideoUni3C_embeds` —— 3/8 个有
- `easy int` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 2/8 个有
- `ImageBatchGet` —— 1/8 个有
- `ImitationHueNode` —— 1/8 个有
- `LoadRembgByBiRefNetModel` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `RembgByBiRefNet` —— 1/8 个有
- `WanVideoLoraSelect` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
