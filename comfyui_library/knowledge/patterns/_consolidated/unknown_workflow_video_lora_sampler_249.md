---
name: unknown_workflow_video_lora_sampler_249
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9545
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, Int, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk官方版本-单人表演（质量不劣化）_2019287708035719169.json, 视频生成/图生视频/InfiniteTalk数字人-简单好用好理解_1992127690593595394.json, 视频生成/图生视频/InfiniteTalk数字人图生语音视频【AI小王子】_1962034287111553026.json, 视频生成/图生视频/InfiniteTalk数字人，口播讲解视频，动态比较小，适合拿着产品口播，图生视频（自用）_1966880247608172545.json, 视频生成/图生视频/Infinitetalk 单人版_KJ加速_1977653780160368641.json, 视频生成/图生视频/Infinitetalk-数字人_2066404192645898242.json, 视频生成/图生视频/Infinitetalk单人数字人无限时长自循环_2084891209599897602.json, 视频生成/图生视频/Infinitetalk数字人_1989166244014198786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_249

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk官方版本-单人表演（质量不劣化）_2019287708035719169.json、视频生成/图生视频/InfiniteTalk数字人-简单好用好理解_1992127690593595394.json、视频生成/图生视频/InfiniteTalk数字人图生语音视频【AI小王子】_1962034287111553026.json、视频生成/图生视频/InfiniteTalk数字人，口播讲解视频，动态比较小，适合拿着产品口播，图生视频（自用）_1966880247608172545.json、视频生成/图生视频/Infinitetalk 单人版_KJ加速_1977653780160368641.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 7/8 个有
- `ImageUpscaleWithModel` —— 3/8 个有
- `ImpactInt` —— 3/8 个有
- `RH_GetAudioDuration` —— 3/8 个有
- `Upscale Model Loader` —— 3/8 个有
- `Audio Duration (mtb)` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `GetImageSizeAndCount` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `Qwen3TTSModelLoader` —— 1/8 个有
- `Qwen3TTSVoiceDesign` —— 1/8 个有
- `SaveAudio` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `Text` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `WanVideoEncode` —— 1/8 个有
- `WanVideoTextEncodeCached` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
