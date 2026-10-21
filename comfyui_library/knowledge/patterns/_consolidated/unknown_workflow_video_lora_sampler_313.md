---
name: unknown_workflow_video_lora_sampler_313
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.547714
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1971146513277689858.json, 视频生成/图生视频/1969930159883231234.json, 视频生成/图生视频/2018529838486790146.json, 视频生成/图生视频/2037140996198240257.json, 视频生成/图生视频/1969240711893839873.json, 视频生成/图生视频/1969526770116554754.json, 视频生成/图生视频/1971057186338152449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_313

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1971146513277689858.json、视频生成/图生视频/1969930159883231234.json、视频生成/图生视频/2018529838486790146.json、视频生成/图生视频/2037140996198240257.json、视频生成/图生视频/1969240711893839873.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageConcatMulti`
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 6/7 个有
- `Int` —— 5/7 个有
- `BlockifyMask` —— 4/7 个有
- `DrawMaskOnImage` —— 4/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `GrowMask` —— 4/7 个有
- `LayerUtility: PurgeVRAM` —— 4/7 个有
- `VHS_VideoInfo` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `LayerMask: SegformerB2ClothesUltra` —— 2/7 个有
- `WanVideoTorchCompileSettings` —— 2/7 个有
- `AILab_MiniCPM_4_V` —— 1/7 个有
- `DownloadAndLoadSAM2Model` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LayerMask: LoadFlorence2Model` —— 1/7 个有
- `LayerMask: ObjectDetectorFL2` —— 1/7 个有
- `LayerMask: SAM2VideoUltra` —— 1/7 个有
- `PointsEditor` —— 1/7 个有
- `Sam2Segmentation` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `Text` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
