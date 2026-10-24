---
name: unknown_workflow_video_sampler_vae_68
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.921286
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/人物对口型_2035299713183916034.json, 数字人/数字人/Infinitetalk单人数字人无限时长自循环_2088948708812611585.json, 数字人/数字人/Infinitetalk单人数字人无限时长自循环_2108715715753766913.json, 数字人/数字人/数字人-口播_2088243121611173889.json, 视频生成/图生视频/API-对口型-数字人_2051682079896809474.json, 视频生成/图生视频/CCC的InfiniteTalk数字人_2026963272511000578.json, 视频生成/图生视频/IndexTTS2+InfiniteTalk图生数字人单人-B站UP主@好奇漫步!音频数字人同时生成_1983563401169444866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_68

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/人物对口型_2035299713183916034.json、数字人/数字人/Infinitetalk单人数字人无限时长自循环_2088948708812611585.json、数字人/数字人/Infinitetalk单人数字人无限时长自循环_2108715715753766913.json、数字人/数字人/数字人-口播_2088243121611173889.json、视频生成/图生视频/API-对口型-数字人_2051682079896809474.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `Int` —— 5/7 个有
- `ToInt` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `RH_GetAudioDuration` —— 4/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `Audio Duration (mtb)` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `Float to Int` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `IndexTTS2_Emotion` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `OmniVoiceVoiceCloneTTS` —— 1/7 个有
- `OmniVoiceWhisperLoader` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `SaveAudioMP3` —— 1/7 个有
- `VHS_LoadAudioUpload` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
