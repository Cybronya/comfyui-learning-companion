---
name: unknown_workflow_video_sampler_vae_39
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9418
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/黑鲸千帆-1m左右高质量（1248幅度大）_1994344708442890242.json, 图片生成/文生图/黑鲸千帆-中质量2m内长视频（960幅度大）_1994320938558750721.json, 数字人/数字人/Infinitetalk单人数字人无限时长自循环_2088948708812611585.json, 数字人/数字人/Infinitetalk单人数字人无限时长自循环_2108715715753766913.json, 数字人/数字人/数字人-口播_2088243121611173889.json, 视频生成/图生视频/1962411738001969154.json, 视频生成/图生视频/1979004243053023234.json, 视频生成/图生视频/2051682079896809474.json, 视频生成/图生视频/2026963272511000578.json, 视频生成/图生视频/1983542488248033281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_39

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/黑鲸千帆-1m左右高质量（1248幅度大）_1994344708442890242.json、图片生成/文生图/黑鲸千帆-中质量2m内长视频（960幅度大）_1994320938558750721.json、数字人/数字人/Infinitetalk单人数字人无限时长自循环_2088948708812611585.json、数字人/数字人/Infinitetalk单人数字人无限时长自循环_2108715715753766913.json、数字人/数字人/数字人-口播_2088243121611173889.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 9/10 个有
- `RH_GetAudioDuration` —— 9/10 个有
- `ToInt` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `ImageResizeKJv2` —— 7/10 个有
- `MultiTalkModelLoader` —— 7/10 个有
- `WanVideoBlockSwap` —— 7/10 个有
- `WanVideoLoraSelect` —— 7/10 个有
- `WanVideoModelLoader` —— 7/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/10 个有
- `CreateVideo` —— 3/10 个有
- `JWFloat` —— 3/10 个有
- `PreViewVideo` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `RHHiddenNodes` —— 3/10 个有
- `Audio Duration (mtb)` —— 1/10 个有
- `Float to Int` —— 1/10 个有
- `OmniVoiceVoiceCloneTTS` —— 1/10 个有
- `OmniVoiceWhisperLoader` —— 1/10 个有
- `SaveAudioMP3` —— 1/10 个有
- `VHS_LoadAudioUpload` —— 1/10 个有
- `easy anythingIndexSwitch` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
