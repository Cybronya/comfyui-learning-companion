---
name: unknown_workflow_video_lora_sampler_447
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.973
common_nodes: [Apply Whisper, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SoundFlow_TrimAudio, String Literal, VHS_VideoCombine, VoxCPM_TTS, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1986321706753150978.json, 视频生成/图生视频/1994362409961857025.json, 视频生成/图生视频/1986106739839946753.json, 音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json, 音频生成/音频生成/视频数字人对口型_1985952196049215490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_447

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1986321706753150978.json、视频生成/图生视频/1994362409961857025.json、视频生成/图生视频/1986106739839946753.json、音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json、音频生成/音频生成/视频数字人对口型_1985952196049215490.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Anything Everywhere` —— 4/5 个有
- `Float to Int` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `RH_GetAudioDuration` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
