---
name: unknown_workflow_video_sampler_vae_100
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.853
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/infinitetalk数字人_2084490925362999297.json, 视频生成/图生视频/INFINITE talk，实现无限时长、口型精准的视频配音_1972120402749222914.json, 视频生成/图生视频/InfiniteTalk-单人视频转数字人_1991134809961398273.json, 视频生成/图生视频/InfiniteTalk图像双人对口型_1971843495331819522.json, 视频生成/图生视频/视频对口型_1971064636227391489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_100

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/infinitetalk数字人_2084490925362999297.json、视频生成/图生视频/INFINITE talk，实现无限时长、口型精准的视频配音_1972120402749222914.json、视频生成/图生视频/InfiniteTalk-单人视频转数字人_1991134809961398273.json、视频生成/图生视频/InfiniteTalk图像双人对口型_1971843495331819522.json、视频生成/图生视频/视频对口型_1971064636227391489.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `Audio Duration (mtb)` —— 3/5 个有
- `AudioCrop` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `VHS_VideoInfo` —— 3/5 个有
- `WanVideoLoraSelect` —— 3/5 个有
- `INTConstant` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `JWIntegerToString` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `WanVideoLoraSelectMulti` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `JWFloat` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
