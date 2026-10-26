---
name: unknown_workflow_video_lora_sampler_322
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.92625
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, Int, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/单人音频+图片生成视频「说话，唱歌，支持中文」InfiniteTalk_1968700475308691457.json, 视频生成/图生视频/图生万影-说话_1983881923028287489.json, 视频生成/图生视频/图生视频+声音克隆数字人（一张图片对口型）_1985498577474625538.json, 视频生成/图生视频/图生视频-infinitetalk单人_2033715529726300161.json, 视频生成/图生视频/图生视频-infinitetalk单人_2034066519231041538.json, 视频生成/图生视频/图生视频-infinitetalk单人_2077567710116012034.json, 视频生成/图生视频/图生视频-infinitetalk单人_2084526458785058817.json, 视频生成/图生视频/数字人infinitetalk_1966325384155475970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_322

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/单人音频+图片生成视频「说话，唱歌，支持中文」InfiniteTalk_1968700475308691457.json、视频生成/图生视频/图生万影-说话_1983881923028287489.json、视频生成/图生视频/图生视频+声音克隆数字人（一张图片对口型）_1985498577474625538.json、视频生成/图生视频/图生视频-infinitetalk单人_2033715529726300161.json、视频生成/图生视频/图生视频-infinitetalk单人_2034066519231041538.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
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
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `ToInt` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `RH_GetAudioDuration` —— 6/8 个有
- `CR Text` —— 2/8 个有
- `Audio Duration (mtb)` —— 1/8 个有
- `FlashVSRNode` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `IndexTTS2_Emotion` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `Sleep` —— 1/8 个有
- `TrimAudioDuration` —— 1/8 个有
- `VHS_LoadAudioUpload` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
