---
name: unknown_workflow_video_lora_sampler_500
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8805
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MultiTalk+Aniwan图生数字人+音色克隆_1948391193374797826.json, 视频生成/图生视频/Multitalk+aniwan数字人，可说话演讲可唱歌_1940356622893953026.json, 视频生成/图生视频/ani ③-Multitalk数字人_1945034637402099713.json, 音频生成/音频生成/Multitalk+aniwan数字人，可说话演讲可唱歌_1949746352932741121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_500

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MultiTalk+Aniwan图生数字人+音色克隆_1948391193374797826.json、视频生成/图生视频/Multitalk+aniwan数字人，可说话演讲可唱歌_1940356622893953026.json、视频生成/图生视频/ani ③-Multitalk数字人_1945034637402099713.json、音频生成/音频生成/Multitalk+aniwan数字人，可说话演讲可唱歌_1949746352932741121.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 3/4 个有
- `AudioCrop` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `TextInput_` —— 3/4 个有
- `WanVideoEasyCache` —— 3/4 个有
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoExperimentalArgs` —— 3/4 个有
- `WanVideoFreeInitArgs` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `WanVideoSetRadialAttention` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `JWIntegerToString` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `IndexTTSRun` —— 1/4 个有
- `Int` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoEncode` —— 1/4 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/4 个有
- `WanVideoUni3C_embeds` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
