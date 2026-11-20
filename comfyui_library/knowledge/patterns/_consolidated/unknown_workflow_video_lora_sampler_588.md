---
name: unknown_workflow_video_lora_sampler_588
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.97325
common_nodes: [Anything Everywhere, Apply Whisper, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SoundFlow_TrimAudio, String Literal, VHS_VideoCombine, VoxCPM_TTS, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2-图生数字人_1986321706753150978.json, 视频生成/图生视频/图生数字人+配音（自动匹配音频时长）_1986106739839946753.json, 音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json, 音频生成/音频生成/视频数字人对口型_1985952196049215490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_588

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.2-图生数字人_1986321706753150978.json、视频生成/图生视频/图生数字人+配音（自动匹配音频时长）_1986106739839946753.json、音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json、音频生成/音频生成/视频数字人对口型_1985952196049215490.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `Apply Whisper`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SoundFlow_TrimAudio`
- `String Literal`
- `VHS_VideoCombine`
- `VoxCPM_TTS`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `Float to Int` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `RH_GetAudioDuration` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
