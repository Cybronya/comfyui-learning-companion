---
name: unknown_workflow_video_lora_sampler_120
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.829538
common_nodes: [CLIPVisionLoader, CR Text, GetImageSizeAndCount, ImageResizeKJv2, ImpactInt, LoadImage, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1987930419398119426.json, 视频生成/图生视频/2015387238657433602.json, 视频生成/图生视频/2026954923237183490.json, 视频生成/图生视频/1978005827682455554.json, 视频生成/图生视频/1992946454725672962.json, 视频生成/图生视频/1981708814372225026.json, 视频生成/图生视频/1980606139123585025.json, 视频生成/图生视频/2009584371598102530.json, 视频生成/图生视频/1979145028213837826.json, 视频生成/图生视频/2015053987497648129.json, 视频生成/图生视频/2041179422866284546.json, 视频生成/图生视频/1975078330166849538.json, 视频生成/图生视频/1969605920248504321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1987930419398119426.json、视频生成/图生视频/2015387238657433602.json、视频生成/图生视频/2026954923237183490.json、视频生成/图生视频/1978005827682455554.json、视频生成/图生视频/1992946454725672962.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `ImpactInt`
- `LoadImage`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 12/13 个有
- `DownloadAndLoadWav2VecModel` —— 12/13 个有
- `Fast Groups Bypasser (rgthree)` —— 12/13 个有
- `GetNode` —— 12/13 个有
- `JWInteger` —— 12/13 个有
- `LayerUtility: PurgeVRAM` —— 12/13 个有
- `MultiTalkModelLoader` —— 12/13 个有
- `MultiTalkWav2VecEmbeds` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `WanVideoEncode` —— 12/13 个有
- `WanVideoUni3C_ControlnetLoader` —— 12/13 个有
- `WanVideoUni3C_embeds` —— 12/13 个有
- `DrawViTPose` —— 10/13 个有
- `OnnxDetectionModelLoader` —— 10/13 个有
- `PoseAndFaceDetection` —— 10/13 个有
- `ImageConcatMulti` —— 7/13 个有
- `WanVideoLoraSelect` —— 6/13 个有
- `FaceMaskFromPoseKeypoints` —— 3/13 个有
- `ImageCropByMaskAndResize` —— 3/13 个有
- `PixelPerfectResolution` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `TT_img_enc_v2` —— 3/13 个有
- `DWPreprocessor` —— 2/13 个有
- `DuckHideNode` —— 2/13 个有
- `Note Plus (mtb)` —— 2/13 个有
- `SaveImage` —— 2/13 个有
- `ColorMatch` —— 1/13 个有
- `Image Resize To Width` —— 1/13 个有
- `ImageMirror` —— 1/13 个有
- `ImpactSwitch` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `LoadAudio` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `SimpleCondition+` —— 1/13 个有
- `WanVideoContextOptions` —— 1/13 个有
- `easy float` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
