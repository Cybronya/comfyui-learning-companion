---
name: unknown_workflow_video_lora_sampler_79
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.788588
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, PrimitiveInt, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, ttN float]
problems: []
missing: []
members: [视频生成/图生视频/2082283032458907650.json, 视频生成/图生视频/1969244065881595906.json, 视频生成/图生视频/2058552984040198146.json, 视频生成/图生视频/2058894447605280770.json, 视频生成/图生视频/2058904092608651265.json, 视频生成/图生视频/2060366272411557890.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801.json, 视频生成/图生视频/2030816272992178178.json, 视频生成/图生视频/2047151840906711042.json, 视频生成/图生视频/2072563254043430913.json, 视频生成/图生视频/2066574337938907138.json, 视频生成/图生视频/2060943711281967105.json, 视频生成/图生视频/1986294172028207106.json, 视频生成/图生视频/2046059624503185409.json, 视频生成/图生视频/2061381332097396737.json, 视频生成/图生视频/2081255754593554433.json, 视频生成/图生视频/2070319879026208770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2082283032458907650.json、视频生成/图生视频/1969244065881595906.json、视频生成/图生视频/2058552984040198146.json、视频生成/图生视频/2058894447605280770.json、视频生成/图生视频/2058904092608651265.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveInt`
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
- `easy cleanGpuUsed`
- `ttN float`

**可变部分**（部分 workflow 才有）：
- `Text` —— 16/17 个有
- `ImageFromBatch` —— 13/17 个有
- `VHS_VideoInfo` —— 12/17 个有
- `Audio Duration (mtb)` —— 5/17 个有
- `AudioCrop` —— 5/17 个有
- `DownloadAndLoadWav2VecModel` —— 5/17 个有
- `GetImageRangeFromBatch` —— 5/17 个有
- `GetImageSizeAndCount` —— 5/17 个有
- `ImageFromBatch+` —— 5/17 个有
- `IntToString` —— 5/17 个有
- `LoadAudio` —— 5/17 个有
- `MelBandRoFormerModelLoader` —— 5/17 个有
- `MelBandRoFormerSampler` —— 5/17 个有
- `MultiTalkModelLoader` —— 5/17 个有
- `MultiTalkWav2VecEmbeds` —— 5/17 个有
- `PreviewAny` —— 5/17 个有
- `WanVideoEncode` —— 5/17 个有
- `WanVideoImageToVideoMultiTalk` —— 5/17 个有
- `WanVideoLoraSelect` —— 5/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
