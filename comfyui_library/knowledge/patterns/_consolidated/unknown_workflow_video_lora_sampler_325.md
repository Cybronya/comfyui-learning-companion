---
name: unknown_workflow_video_lora_sampler_325
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.884857
common_nodes: [CLIPVisionLoader, Int, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/数字人图片单人_1964652057074520065.json, 视频生成/图生视频/虚拟演播室数字人_2045009566550724610.json, 视频生成/图生视频/高清数字人-稳定加强V2.0版(对口型、口播、唱歌）最强AI数字人高清InfiniteTalk单人口_2075038609807339522.json, 视频生成/文生视频/infinitetalk单人-100%对口型_1986675627816349697.json, 视频生成/文生视频/infinitetalk单人_1962411738001969154.json, 视频生成/文生视频/infinitetalk单人_1979004243053023234.json, 视频生成/文生视频/最强的数字人，声音克隆+文本驱动+图生视频_2078774161115275266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_325

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/数字人图片单人_1964652057074520065.json、视频生成/图生视频/虚拟演播室数字人_2045009566550724610.json、视频生成/图生视频/高清数字人-稳定加强V2.0版(对口型、口播、唱歌）最强AI数字人高清InfiniteTalk单人口_2075038609807339522.json、视频生成/文生视频/infinitetalk单人-100%对口型_1986675627816349697.json、视频生成/文生视频/infinitetalk单人_1962411738001969154.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `Int`
- `LoadAudio`
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
- `AudioCrop` —— 6/7 个有
- `AudioSeparation` —— 6/7 个有
- `DownloadAndLoadWav2VecModel` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `RH_GetAudioDuration` —— 6/7 个有
- `CR Prompt Text` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `Apply Whisper` —— 1/7 个有
- `AudioGetTempo` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetCurrentTimeNode` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `OmniVoiceLongformTTS` —— 1/7 个有
- `OmniVoiceMultiSpeakerTTS` —— 1/7 个有
- `OmniVoiceVoiceDesignTTS` —— 1/7 个有
- `OmniVoiceWhisperLoader` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/7 个有
- `WanVideoUni3C_embeds` —— 1/7 个有
- `Wav2VecModelLoader` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
