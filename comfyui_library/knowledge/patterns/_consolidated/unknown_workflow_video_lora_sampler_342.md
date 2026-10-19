---
name: unknown_workflow_video_lora_sampler_342
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.786833
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Wan2.1单人对口型_2096760991131455490.json, 视频生成/图生视频/1983435435332575234.json, 视频生成/图生视频/1988813564645355522.json, 视频生成/图生视频/2064352779824623618.json, 视频生成/图生视频/1958125817404542978.json, 视频生成/图生视频/1958125770365423618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_342

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/Wan2.1单人对口型_2096760991131455490.json、视频生成/图生视频/1983435435332575234.json、视频生成/图生视频/1988813564645355522.json、视频生成/图生视频/2064352779824623618.json、视频生成/图生视频/1958125817404542978.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 5/6 个有
- `DownloadAndLoadWav2VecModel` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `WanVideoDecode` —— 3/6 个有
- `WanVideoPassImagesFromSamples` —— 3/6 个有
- `Wav2VecModelLoader` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `FancyTimerNode` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `ImageScale` —— 2/6 个有
- `IndexTTSNode` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `easy getNode` —— 2/6 个有
- `easy setNode` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `JWIntegerToString` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `VHS_LoadAudioUpload` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
