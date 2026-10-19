---
name: unknown_workflow_video_lora_sampler_149
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.902273
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk单人数字人无限时长自循环_2088948708812611585.json, 数字人/数字人/Infinitetalk单人数字人无限时长自循环_2108715715753766913.json, 数字人/数字人/数字人-口播_2088243121611173889.json, 视频生成/图生视频/1957952304787898369.json, 视频生成/图生视频/1962411738001969154.json, 视频生成/图生视频/1979004243053023234.json, 视频生成/图生视频/2051682079896809474.json, 视频生成/图生视频/2026963272511000578.json, 视频生成/图生视频/1983563401169444866.json, 视频生成/图生视频/1985498577474625538.json, 视频生成/图生视频/2080617453847138306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_149

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/Infinitetalk单人数字人无限时长自循环_2088948708812611585.json、数字人/数字人/Infinitetalk单人数字人无限时长自循环_2108715715753766913.json、数字人/数字人/数字人-口播_2088243121611173889.json、视频生成/图生视频/1957952304787898369.json、视频生成/图生视频/1962411738001969154.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 10/11 个有
- `Int` —— 9/11 个有
- `ToInt` —— 9/11 个有
- `easy showAnything` —— 8/11 个有
- `RH_GetAudioDuration` —— 6/11 个有
- `Audio Duration (mtb)` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `CR Text` —— 3/11 个有
- `IndexTTS2_Emotion` —— 3/11 个有
- `PrimitiveFloat` —— 3/11 个有
- `SaveAudio` —— 2/11 个有
- `easy anythingIndexSwitch` —— 2/11 个有
- `Float to Int` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `OmniVoiceVoiceCloneTTS` —— 1/11 个有
- `OmniVoiceWhisperLoader` —— 1/11 个有
- `SaveAudioMP3` —— 1/11 个有
- `VHS_LoadAudioUpload` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
