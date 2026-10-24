---
name: unknown_workflow_video_lora_sampler_341
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.739
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageCropByMaskAndResize, ImageFromBatch, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, PrimitiveInt, SetNode, SimpleMath+, Text, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, ttN float]
problems: []
missing: []
members: [视频生成/图生视频/AI跳舞唱歌！一边唱歌一边跳舞！_2066574337938907138.json, 视频生成/图生视频/AI跳舞唱歌！一边唱歌一边跳舞！艾橘溪_2060943711281967105.json, 视频生成/图生视频/Wan  图生视频 人物角色迁移 动作模仿+唱歌跳舞+舞剑   动作迁移 人物替换_2046059624503185409.json, 视频生成/图生视频/Wan2.2数字人跳舞+唱歌 实现一边跳舞一边唱歌_2061381332097396737.json, 视频生成/图生视频/Wan2.2数字人跳舞+唱歌 实现一边跳舞一边唱歌_2081255754593554433.json, 视频生成/图生视频/跳舞唱歌！一边唱歌一边跳舞！动作跟随迁移_2070319879026208770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_341

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/AI跳舞唱歌！一边唱歌一边跳舞！_2066574337938907138.json、视频生成/图生视频/AI跳舞唱歌！一边唱歌一边跳舞！艾橘溪_2060943711281967105.json、视频生成/图生视频/Wan  图生视频 人物角色迁移 动作模仿+唱歌跳舞+舞剑   动作迁移 人物替换_2046059624503185409.json、视频生成/图生视频/Wan2.2数字人跳舞+唱歌 实现一边跳舞一边唱歌_2061381332097396737.json、视频生成/图生视频/Wan2.2数字人跳舞+唱歌 实现一边跳舞一边唱歌_2081255754593554433.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageCropByMaskAndResize`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
- `Text`
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
- `Audio Duration (mtb)` —— 5/6 个有
- `AudioCrop` —— 5/6 个有
- `DownloadAndLoadWav2VecModel` —— 5/6 个有
- `GetImageRangeFromBatch` —— 5/6 个有
- `GetImageSizeAndCount` —— 5/6 个有
- `ImageFromBatch+` —— 5/6 个有
- `IntToString` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `MelBandRoFormerModelLoader` —— 5/6 个有
- `MelBandRoFormerSampler` —— 5/6 个有
- `MultiTalkModelLoader` —— 5/6 个有
- `MultiTalkWav2VecEmbeds` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `WanVideoEncode` —— 5/6 个有
- `WanVideoImageToVideoMultiTalk` —— 5/6 个有
- `WanVideoLoraSelect` —— 5/6 个有
- `VHS_VideoInfo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
