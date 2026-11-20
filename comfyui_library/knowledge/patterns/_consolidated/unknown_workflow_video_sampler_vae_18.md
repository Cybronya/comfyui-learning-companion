---
name: unknown_workflow_video_sampler_vae_18
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.951429
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, Int, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkWav2VecEmbeds, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/黑鲸千帆-1m左右高质量（1248幅度大）_1994344708442890242.json, 图片生成/文生图/黑鲸千帆-中质量2m内长视频（960幅度大）_1994320938558750721.json, 数字人/数字人/API-对口型-数字人-最新_2070339599389511682.json, 数字人/数字人/API-对口型-数字人_2043715361241047042.json, 数字人/数字人/API-对口型-数字人_2067238745916657666.json, 数字人/数字人/API-对口型-数字人（1280）_2057461580308238337.json, 数字人/数字人/API-对口型数字人-1280_2057455520889524226.json, 数字人/数字人/CustomerKing 数字人商品带货_2080338543561502721.json, 数字人/数字人/Infinite Talk数字人_1978415131019382786.json, 数字人/数字人/InfiniteTalk单人版数字人【超过1分钟的】_2003019304549380098.json, 数字人/数字人/InfiniteTalk图片对口型_1999422006565236738.json, 数字人/数字人/InfiniteTalk数字人-简单好用易理解_1991355341403193346.json, 数字人/数字人/Infinitetalk数字人_2006979668984991746.json, 视频生成/图生视频/Infinitetalk数字人_1989166244014198786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_18

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/黑鲸千帆-1m左右高质量（1248幅度大）_1994344708442890242.json、图片生成/文生图/黑鲸千帆-中质量2m内长视频（960幅度大）_1994320938558750721.json、数字人/数字人/API-对口型-数字人-最新_2070339599389511682.json、数字人/数字人/API-对口型-数字人_2043715361241047042.json、数字人/数字人/API-对口型-数字人_2067238745916657666.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `Int`
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

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 13/14 个有
- `easy showAnything` —— 13/14 个有
- `LoadAudio` —— 12/14 个有
- `WanVideoBlockSwap` —— 12/14 个有
- `MultiTalkModelLoader` —— 11/14 个有
- `WanVideoLoraSelect` —— 11/14 个有
- `WanVideoModelLoader` —— 11/14 个有
- `WanVideoTorchCompileSettings` —— 11/14 个有
- `ImageResizeKJv2` —— 10/14 个有
- `RH_GetAudioDuration` —— 10/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/14 个有
- `easy int` —— 8/14 个有
- `ImageUpscaleWithModel` —— 3/14 个有
- `ImpactInt` —— 3/14 个有
- `RHHiddenNodes` —— 3/14 个有
- `Upscale Model Loader` —— 3/14 个有
- `VHS_LoadAudioUpload` —— 3/14 个有
- `CreateVideo` —— 2/14 个有
- `GetImageRangeFromBatch` —— 2/14 个有
- `GetImageSizeAndCount` —— 2/14 个有
- `GetNode` —— 2/14 个有
- `JWFloat` —— 2/14 个有
- `PreViewVideo` —— 2/14 个有
- `SaveAudio` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `VHS_LoadVideo` —— 2/14 个有
- `WanVideoEncode` —— 2/14 个有
- `WanVideoTextEncodeCached` —— 2/14 个有
- `Audio Duration (mtb)` —— 1/14 个有
- `Text` —— 1/14 个有
- `ToFloat` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
