---
name: unknown_workflow_video_lora_sampler_585
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.681
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/极速版-数字人_个人IP_2110421173111705601.json, 视频生成/图生视频/视频对口型数字人_InfiniteTalk_V2V_2083750945984442370.json, 音频生成/音频生成/★视频数字人支持克隆+配音_2048759846756945922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_585

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/极速版-数字人_个人IP_2110421173111705601.json、视频生成/图生视频/视频对口型数字人_InfiniteTalk_V2V_2083750945984442370.json、音频生成/音频生成/★视频数字人支持克隆+配音_2048759846756945922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `DownloadAndLoadWav2VecModel` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `AudioDuration_wan` —— 1/3 个有
- `AudioSeparation` —— 1/3 个有
- `H3ModeSwitch` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `Wav2VecModelLoader` —— 1/3 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/3 个有
- `easy indexTTSGenerateSimple` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
