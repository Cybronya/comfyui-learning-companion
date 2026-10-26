---
name: unknown_workflow_video_lora_sampler_345
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.899714
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, Int, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/数字人-图片对口型唱歌_口播（infinitetalk）_1988257488845889538.json, 数字人/数字人/超自然图片数字人对口型（根叔）_1977237089068687361.json, 视频生成/图生视频/CCC的InfiniteTalk数字人_2026963272511000578.json, 视频生成/图生视频/IndexTTS2+InfiniteTalk图生数字人单人-B站UP主@好奇漫步!音频数字人同时生成_1983563401169444866.json, 视频生成/图生视频/Infinite Talk单人版_1968672721771143169.json, 视频生成/图生视频/Infinite Talk数字人_2069716627356217345.json, 视频生成/图生视频/蓝天AI口播工作流_2080617453847138306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_345

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/数字人-图片对口型唱歌_口播（infinitetalk）_1988257488845889538.json、数字人/数字人/超自然图片数字人对口型（根叔）_1977237089068687361.json、视频生成/图生视频/CCC的InfiniteTalk数字人_2026963272511000578.json、视频生成/图生视频/IndexTTS2+InfiniteTalk图生数字人单人-B站UP主@好奇漫步!音频数字人同时生成_1983563401169444866.json、视频生成/图生视频/Infinite Talk单人版_1968672721771143169.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `Int`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 6/7 个有
- `ToInt` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `Audio Duration (mtb)` —— 3/7 个有
- `RH_GetAudioDuration` —— 3/7 个有
- `SaveAudio` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `IndexTTS2_Emotion` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `CM_IntToFloat` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `SeedVR2BlockSwap` —— 1/7 个有
- `Upscale Model Loader` —— 1/7 个有
- `WanVideoTextEncodeCached` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
