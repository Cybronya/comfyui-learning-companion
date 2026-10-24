---
name: unknown_workflow_video_lora_sampler_209
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.839
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AudioDiT单人语音克隆TTS+对口型数字人Infinite+Talk 音色克隆带语气情感_2039872167524966402.json, 视频生成/图生视频/INF图片数字人对口型多动态_1982787027227803649.json, 视频生成/图生视频/Inf-Talk_1976659195296727041.json, 视频生成/图生视频/Infinite Talk 数字人（对口型）_1980462262907527170.json, 视频生成/图生视频/Infinite Talk 音频驱动图说话唱歌，提示词调度多动作_1958946563538235394.json, 视频生成/图生视频/Infinite Talk单图+音频+提示词=数字人无限MV_1981723961920757761.json, 视频生成/图生视频/Infinite Talk极速高质量提示词调度动作控制图生视频KTV_1960989551487594497.json, 视频生成/图生视频/Infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人_1958729195713097730.json, 视频生成/图生视频/跨模态仿OVI无限时长图生视频含配音数字人工作流V1（支持中文）_1974878137764982786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_209

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/AudioDiT单人语音克隆TTS+对口型数字人Infinite+Talk 音色克隆带语气情感_2039872167524966402.json、视频生成/图生视频/INF图片数字人对口型多动态_1982787027227803649.json、视频生成/图生视频/Inf-Talk_1976659195296727041.json、视频生成/图生视频/Infinite Talk 数字人（对口型）_1980462262907527170.json、视频生成/图生视频/Infinite Talk 音频驱动图说话唱歌，提示词调度多动作_1958946563538235394.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 8/9 个有
- `SaveAudio` —— 2/9 个有
- `Audio To Text (mtb)` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GetAudioDurationFromAudio` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `Load Whisper (mtb)` —— 1/9 个有
- `LongCatVoiceCloneTTS` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `NormalizeAudioLoudness` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `SaveAudioMP3` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `WanVideoTorchCompileSettings` —— 1/9 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/9 个有
- `easy indexTTSGenerateSimple` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
