---
name: unknown_workflow_video_upscale_lora_15
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8175
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, ImageUpscaleWithModel, LayerUtility: PurgeVRAM V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveStringMultiline, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1958081939452342273.json, 视频生成/图生视频/1989952363156918273.json, 视频生成/图生视频/1960712411261153281.json, 音频生成/音频生成/数字人_视频_infinite【720P+高清+声音克隆】_1984533428567687169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_15

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1958081939452342273.json、视频生成/图生视频/1989952363156918273.json、视频生成/图生视频/1960712411261153281.json、音频生成/音频生成/数字人_视频_infinite【720P+高清+声音克隆】_1984533428567687169.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveStringMultiline`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 3/4 个有
- `Float to Int` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `IndexTTS2Run` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `LoadWanVideoT5TextEncoder` —— 3/4 个有
- `RH_GetAudioDuration` —— 3/4 个有
- `SaveAudio` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `WanVideoTextEncode` —— 3/4 个有
- `easy anythingIndexSwitch` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `WanVideoEncode` —— 1/4 个有
- `WanVideoTextEncodeCached` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
