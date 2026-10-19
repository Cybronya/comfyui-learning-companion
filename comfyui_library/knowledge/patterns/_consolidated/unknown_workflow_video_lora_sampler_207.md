---
name: unknown_workflow_video_lora_sampler_207
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.811444
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [CR Prompt Text]
members: [图片生成/文生图/1970453209825374209.json, 视频生成/图生视频/2047149486551605249.json, 视频生成/图生视频/2047141901102489601.json, 视频生成/图生视频/2051961839407386625.json, 视频生成/图生视频/2048682075724718081.json, 视频生成/图生视频/2054096337670557697.json, 视频生成/图生视频/2060540846868619266.json, 视频生成/图生视频/2062041921597562882.json, 视频生成/图生视频/2054799806060605442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_207

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1970453209825374209.json、视频生成/图生视频/2047149486551605249.json、视频生成/图生视频/2047141901102489601.json、视频生成/图生视频/2051961839407386625.json、视频生成/图生视频/2048682075724718081.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FB_Qwen3TTSVoiceClone` —— 8/9 个有
- `GetImageSize` —— 8/9 个有
- `ResizeImagesByLongerEdge` —— 8/9 个有
- `Text` —— 8/9 个有
- `WanVideoPassImagesFromSamples` —— 8/9 个有
- `GetNode` —— 5/9 个有
- `PreviewAny` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `WanVideoTorchCompileSettings` —— 5/9 个有
- `Wav2VecModelLoader` —— 5/9 个有
- `PreviewAudio` —— 4/9 个有
- `CR Prompt Text` —— 1/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/9 个有
- `GIMMVFI_interpolate` —— 1/9 个有
- `HAIGC_VideoSubtitleTimestampPro` —— 1/9 个有
- `ImageUpscaleWithModel` —— 1/9 个有
- `IndexTTS2Run` —— 1/9 个有
- `SaveAudio` —— 1/9 个有
- `UpscaleModelLoader` —— 1/9 个有
- `WanVideoDecode` —— 1/9 个有
- `ZML_TextInput` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
