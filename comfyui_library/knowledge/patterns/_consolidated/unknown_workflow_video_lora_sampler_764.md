---
name: unknown_workflow_video_lora_sampler_764
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88425
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FB_Qwen3TTSVoiceClone, GetImageSize, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, ResizeImagesByLongerEdge, Text, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoPassImagesFromSamples, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/手串替换_2054096337670557697.json, 视频生成/图生视频/手串生活方式短视频不露脸稳定版_2060540846868619266.json, 视频生成/图生视频/手串生活版_v5.2_原稿精准字幕版_2062041921597562882.json, 视频生成/图生视频/鸿茅药酒志_2054799806060605442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_764

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/手串替换_2054096337670557697.json、视频生成/图生视频/手串生活方式短视频不露脸稳定版_2060540846868619266.json、视频生成/图生视频/手串生活版_v5.2_原稿精准字幕版_2062041921597562882.json、视频生成/图生视频/鸿茅药酒志_2054799806060605442.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FB_Qwen3TTSVoiceClone`
- `GetImageSize`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `ResizeImagesByLongerEdge`
- `Text`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoPassImagesFromSamples`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/4 个有
- `HAIGC_VideoSubtitleTimestampPro` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `Wav2VecModelLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
