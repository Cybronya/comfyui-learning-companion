---
name: unknown_workflow_video_lora_sampler_122
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.791812
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, PrimitiveInt, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, ttN float]
problems: []
missing: []
members: [数字人/数字人/animi跳舞_1989222596455575553.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞 Animate_2082283032458907650.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058552984040198146.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058894447605280770.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058904092608651265.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2060366272411557890.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801.json, 视频生成/图生视频/AI动作模仿+跳舞+剑舞=Animate wan2.2_2030816272992178178.json, 视频生成/图生视频/AI动作模仿+跳舞+剑舞=Animate wan2.2_2047151840906711042.json, 视频生成/图生视频/AI动作模仿+高清流畅！_2072563254043430913.json, 视频生成/图生视频/AI跳舞唱歌！一边唱歌一边跳舞！_2066574337938907138.json, 视频生成/图生视频/AI跳舞唱歌！一边唱歌一边跳舞！艾橘溪_2060943711281967105.json, 视频生成/图生视频/Wan2.2数字人跳舞+唱歌 实现一边跳舞一边唱歌_2061381332097396737.json, 视频生成/图生视频/Wan2.2数字人跳舞+唱歌 实现一边跳舞一边唱歌_2081255754593554433.json, 视频生成/图生视频/跳舞唱歌！一边唱歌一边跳舞！动作跟随迁移_2070319879026208770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_122

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（数字人/数字人/animi跳舞_1989222596455575553.json、视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞 Animate_2082283032458907650.json、视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json、视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058552984040198146.json、视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058894447605280770.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
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
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `ttN float`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 15/16 个有
- `Text` —— 15/16 个有
- `WanVideoModelLoader` —— 15/16 个有
- `ImageFromBatch` —— 12/16 个有
- `VHS_VideoInfo` —— 11/16 个有
- `Audio Duration (mtb)` —— 5/16 个有
- `AudioCrop` —— 5/16 个有
- `DownloadAndLoadWav2VecModel` —— 5/16 个有
- `GetImageRangeFromBatch` —— 5/16 个有
- `GetImageSizeAndCount` —— 5/16 个有
- `ImageFromBatch+` —— 5/16 个有
- `IntToString` —— 5/16 个有
- `LoadAudio` —— 5/16 个有
- `MelBandRoFormerModelLoader` —— 5/16 个有
- `MelBandRoFormerSampler` —— 5/16 个有
- `MultiTalkModelLoader` —— 5/16 个有
- `MultiTalkWav2VecEmbeds` —— 5/16 个有
- `PreviewAny` —— 5/16 个有
- `WanVideoEncode` —— 5/16 个有
- `WanVideoImageToVideoMultiTalk` —— 5/16 个有
- `WanVideoLoraSelect` —— 5/16 个有
- `RHHiddenNodes` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
