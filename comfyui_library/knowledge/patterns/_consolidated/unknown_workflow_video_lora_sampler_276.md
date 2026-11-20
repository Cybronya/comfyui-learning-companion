---
name: unknown_workflow_video_lora_sampler_276
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7213
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, INTConstant, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json, 视频生成/图生视频/Infinitetalk-视频对口型_2073213335511846913.json, 视频生成/图生视频/infiniteTalk（音色克隆+音频生成）_1970143422839463937.json, 视频生成/图生视频/三笔成书——数字人=图片+文本+声音克隆_1996928089819136001.json, 视频生成/图生视频/数字人=图片+文本+声音克隆_1996900266379300866.json, 视频生成/图生视频/数字人=图片+文本+声音克隆王改革_2000473873579638786.json, 视频生成/图生视频/数字人TTS2+infiniteTalk高清电影对嘴型_1965116783160082434.json, 视频生成/图生视频/数字人对嘴型InfiniteTalk无限时长加载音频版_1965715999553159169.json, 音频生成/音频生成/infiniteTalk（音色克隆+音频生成）_1970169527449382913.json, 音频生成/音频生成/数字人TTS2+infiniteTalk高清电影对嘴型_1965919852949082113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_276

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json、视频生成/图生视频/Infinitetalk-视频对口型_2073213335511846913.json、视频生成/图生视频/infiniteTalk（音色克隆+音频生成）_1970143422839463937.json、视频生成/图生视频/三笔成书——数字人=图片+文本+声音克隆_1996928089819136001.json、视频生成/图生视频/数字人=图片+文本+声音克隆_1996900266379300866.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `LayerUtility: PurgeVRAM V2` —— 8/10 个有
- `PreviewAny` —— 8/10 个有
- `PreviewAudio` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `IndexTTS2Run` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `GetNode` —— 6/10 个有
- `ImageUpscaleWithModel` —— 6/10 个有
- `UpscaleModelLoader` —— 6/10 个有
- `JjkText` —— 4/10 个有
- `MegaTTS3` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `GetImageRangeFromBatch` —— 2/10 个有
- `ImpactSwitch` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `WanVideoEncode` —— 2/10 个有
- `ColorMatch` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `ImageFromBatch` —— 1/10 个有
- `MultiLinePromptIndex` —— 1/10 个有
- `SaveAudioMP3` —— 1/10 个有
- `Text` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
