---
name: unknown_workflow_video_lora_sampler_237
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.935818
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, Int, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/Infinite Talk单人版_1988502915675504642.json, 数字人/数字人/Infinite Talk多角色单人说话_1979921056326651906.json, 数字人/数字人/InfiniteTalk图片对口型_1999422006565236738.json, 数字人/数字人/InfiniteTalk数字人-简单好用易理解_1991355341403193346.json, 数字人/数字人/Infinitetalk数字人_2011352254523117570.json, 数字人/数字人/infinitetalk单图数字人_1972220887082725378.json, 数字人/数字人/infinitetalk单图数字人_2010695881040859138.json, 数字人/数字人/双人多人对口型数字人（漫剧、短剧、电商）_2040688295524438018.json, 数字人/数字人/数字人-图片对口型唱歌_口播（infinitetalk）_1988257488845889538.json, 视频生成/图生视频/InfiniteTalk数字人-简单好用好理解_1992127690593595394.json, 视频生成/图生视频/Infinitetalk-数字人_2066404192645898242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_237

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/Infinite Talk单人版_1988502915675504642.json、数字人/数字人/Infinite Talk多角色单人说话_1979921056326651906.json、数字人/数字人/InfiniteTalk图片对口型_1999422006565236738.json、数字人/数字人/InfiniteTalk数字人-简单好用易理解_1991355341403193346.json、数字人/数字人/Infinitetalk数字人_2011352254523117570.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `Int`
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
- `LoadWanVideoT5TextEncoder` —— 10/11 个有
- `ToInt` —— 10/11 个有
- `WanVideoTextEncode` —— 10/11 个有
- `LoadAudio` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `ImageUpscaleWithModel` —— 7/11 个有
- `ImpactInt` —— 7/11 个有
- `Upscale Model Loader` —— 7/11 个有
- `Audio Duration (mtb)` —— 2/11 个有
- `Load Image From Url (mtb)` —— 2/11 个有
- `LoadAudioFromUrl` —— 2/11 个有
- `PrimitiveString` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `SoundFlow_GetLength` —— 2/11 个有
- `Text` —— 2/11 个有
- `VHS_LoadAudio` —— 2/11 个有
- `AudioCombine` —— 1/11 个有
- `CM_IntToFloat` —— 1/11 个有
- `EmptyAudio` —— 1/11 个有
- `SaveAudio` —— 1/11 个有
- `WanVideoTextEncodeCached` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
