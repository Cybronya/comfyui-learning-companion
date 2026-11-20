---
name: unknown_workflow_video_lora_sampler_282
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.869125
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [数字人/数字人/InfiniteTalk_单人_上传图片王改革_2001205658894598146.json, 数字人/数字人/InfiniteTalk_单人_上传视频王改革_2001218323268370433.json, 数字人/数字人/InfiniteTalk_多人_上传图片王改革_2001218277286309889.json, 数字人/数字人/InfiniteTalk单人视频对口型_2027587542152908801.json, 数字人/数字人/Wan2.1单人对口型_2081005177934532609.json, 数字人/数字人/Wan2.1单人对口型_2096760991131455490.json, 视频生成/图生视频/Wan2.1+InfiniteTalk_单人_图片转数字人_1988813564645355522.json, 视频生成/图生视频/Wan2.1单人对口型_2064352779824623618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_282

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/InfiniteTalk_单人_上传图片王改革_2001205658894598146.json、数字人/数字人/InfiniteTalk_单人_上传视频王改革_2001218323268370433.json、数字人/数字人/InfiniteTalk_多人_上传图片王改革_2001218277286309889.json、数字人/数字人/InfiniteTalk单人视频对口型_2027587542152908801.json、数字人/数字人/Wan2.1单人对口型_2081005177934532609.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 7/8 个有
- `DownloadAndLoadWav2VecModel` —— 7/8 个有
- `LoadImage` —— 6/8 个有
- `WanVideoPassImagesFromSamples` —— 6/8 个有
- `VHS_LoadAudioUpload` —— 5/8 个有
- `CR Text` —— 3/8 个有
- `FancyTimerNode` —— 3/8 个有
- `ImageScale` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `easy getNode` —— 3/8 个有
- `easy setNode` —— 3/8 个有
- `GetImageRangeFromBatch` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `WanVideoDecode` —— 2/8 个有
- `WanVideoEncode` —— 2/8 个有
- `AudioConcat` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
