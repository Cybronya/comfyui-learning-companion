---
name: unknown_workflow_video_lora_sampler_106
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.643571
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetNode, GrowMask, ImageResizeKJv2, LoadImage, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy promptConcat]
problems: []
missing: []
members: [视频生成/图生视频/1970083557895008257.json, 视频生成/图生视频/1978476869785899009.json, 视频生成/图生视频/1980483253431877633.json, 视频生成/图生视频/1979152858195070977.json, 视频生成/图生视频/1971412866429599745.json, 视频生成/图生视频/2032500996332593153.json, 视频生成/图生视频/1975168158174679041.json, 视频生成/图生视频/1975168163258175490.json, 视频生成/图生视频/1977316291763675138.json, 视频生成/图生视频/2037208657041035265.json, 视频生成/图生视频/2039247939687686145.json, 视频生成/图生视频/1977681903191056385.json, 视频生成/图生视频/1975168167381217282.json, 视频生成/图生视频/1973741910089142274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1970083557895008257.json、视频生成/图生视频/1978476869785899009.json、视频生成/图生视频/1980483253431877633.json、视频生成/图生视频/1979152858195070977.json、视频生成/图生视频/1971412866429599745.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 14 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `SimpleMath+`
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
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 13/14 个有
- `AudioSeparation` —— 11/14 个有
- `DownloadAndLoadWav2VecModel` —— 11/14 个有
- `MultiTalkModelLoader` —— 11/14 个有
- `MultiTalkWav2VecEmbeds` —— 11/14 个有
- `LayerMask: LoadSegmentAnythingModels` —— 10/14 个有
- `LayerMask: SegmentAnythingUltra V3` —— 10/14 个有
- `RH_Captioner` —— 10/14 个有
- `easy cleanGpuUsed` —— 10/14 个有
- `DWPreprocessor` —— 8/14 个有
- `FaceMaskFromPoseKeypoints` —— 8/14 个有
- `GetImageSizeAndCount` —— 8/14 个有
- `ImageCropByMaskAndResize` —— 8/14 个有
- `PixelPerfectResolution` —— 8/14 个有
- `Anything Everywhere` —— 7/14 个有
- `CR Text` —— 7/14 个有
- `EmptyImage` —— 7/14 个有
- `INTConstant` —— 7/14 个有
- `ImageConcatMulti` —— 7/14 个有
- `ImpactInt` —— 7/14 个有
- `MaskToImage` —— 7/14 个有
- `SaveAudio` —— 7/14 个有
- `Text` —— 7/14 个有
- `DrawViTPose` —— 6/14 个有
- `OnnxDetectionModelLoader` —— 6/14 个有
- `PoseAndFaceDetection` —— 6/14 个有
- `DownloadAndLoadSAM2Model` —— 4/14 个有
- `RH_LLMAPI_NODE` —— 4/14 个有
- `Sam2Segmentation` —— 4/14 个有
- `WanVideoEncode` —— 3/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/14 个有
- `WanVideoUni3C_embeds` —— 3/14 个有
- `ImageFromBatch` —— 2/14 个有
- `PointsEditor` —— 2/14 个有
- `SeCModelLoader` —— 2/14 个有
- `SeCVideoSegmentation` —— 2/14 个有
- `ClothesSegment` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `SaveAudioMP3` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
