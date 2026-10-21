---
name: unknown_workflow_video_lora_sampler_469
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92075
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Wan2.1单人对口型_2096760991131455490.json, 视频生成/图生视频/1983435435332575234.json, 视频生成/图生视频/1988813564645355522.json, 视频生成/图生视频/2064352779824623618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_469

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/Wan2.1单人对口型_2096760991131455490.json、视频生成/图生视频/1983435435332575234.json、视频生成/图生视频/1988813564645355522.json、视频生成/图生视频/2064352779824623618.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
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
- `AudioSeparation` —— 3/4 个有
- `DownloadAndLoadWav2VecModel` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `WanVideoPassImagesFromSamples` —— 3/4 个有
- `Wav2VecModelLoader` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `FancyTimerNode` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `easy getNode` —— 2/4 个有
- `easy setNode` —— 2/4 个有
- `INTConstant` —— 1/4 个有
- `IndexTTSNode` —— 1/4 个有
- `VHS_LoadAudioUpload` —— 1/4 个有
- `WanVideoDecode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
