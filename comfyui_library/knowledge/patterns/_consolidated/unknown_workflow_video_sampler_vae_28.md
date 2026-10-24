---
name: unknown_workflow_video_sampler_vae_28
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.940917
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, Int, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkWav2VecEmbeds, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/黑鲸千帆-1m左右高质量（1248幅度大）_1994344708442890242.json, 图片生成/文生图/黑鲸千帆-中质量2m内长视频（960幅度大）_1994320938558750721.json, 视频生成/图生视频/Infinite Talk单人版_1968672721771143169.json, 视频生成/图生视频/Infinite Talk数字人_2069716627356217345.json, 视频生成/图生视频/InfiniteTalk 数字人 图生视频 视频配音_1998698671518666753.json, 视频生成/图生视频/InfiniteTalk 数字人-对口型_1983542488248033281.json, 视频生成/图生视频/InfiniteTalk_单人 数字人_1978645327920173058.json, 视频生成/图生视频/InfiniteTalk单人对口型_1978307219957637121.json, 视频生成/图生视频/InfiniteTalk图生数字人单人-B站UP主@好奇漫步_1982650082937978882.json, 视频生成/图生视频/InfiniteTalk图生数字人双人-B站UP主@好奇漫步_1982712177004027905.json, 视频生成/图生视频/Wan2.1 InfiniteTalk 单人版_1990298374261927937.json, 视频生成/图生视频/Wan双人对口型不需要遮罩_2042473229025021954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_28

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/黑鲸千帆-1m左右高质量（1248幅度大）_1994344708442890242.json、图片生成/文生图/黑鲸千帆-中质量2m内长视频（960幅度大）_1994320938558750721.json、视频生成/图生视频/Infinite Talk单人版_1968672721771143169.json、视频生成/图生视频/Infinite Talk数字人_2069716627356217345.json、视频生成/图生视频/InfiniteTalk 数字人 图生视频 视频配音_1998698671518666753.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `Int`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 11/12 个有
- `MultiTalkModelLoader` —— 9/12 个有
- `WanVideoBlockSwap` —— 9/12 个有
- `WanVideoLoraSelect` —— 9/12 个有
- `WanVideoModelLoader` —— 9/12 个有
- `WanVideoTorchCompileSettings` —— 9/12 个有
- `ImageResizeKJv2` —— 8/12 个有
- `RH_GetAudioDuration` —— 8/12 个有
- `Audio Duration (mtb)` —— 4/12 个有
- `CreateVideo` —— 3/12 个有
- `JWFloat` —— 3/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/12 个有
- `PreViewVideo` —— 3/12 个有
- `RHHiddenNodes` —— 3/12 个有
- `AudioCombine` —— 2/12 个有
- `JjkText` —— 2/12 个有
- `DF_Image_scale_to_side` —— 1/12 个有
- `GetImageRangeFromBatch` —— 1/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `SeedVR2` —— 1/12 个有
- `SeedVR2BlockSwap` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `kkGetImage` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
