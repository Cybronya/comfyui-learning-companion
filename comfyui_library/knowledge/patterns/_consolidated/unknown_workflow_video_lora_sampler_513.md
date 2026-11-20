---
name: unknown_workflow_video_lora_sampler_513
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.712333
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoPassImagesFromSamples, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/D_I2V（V1.1.1）_2047149486551605249.json, 视频生成/图生视频/I2V-林小茶_2047141901102489601.json, 视频生成/图生视频/Infinite或者Infinite+IndexTTS2(单人)_1993149833712254977.json, 视频生成/图生视频/V4.1（demo2）_2051961839407386625.json, 视频生成/图生视频/X_I2V（V1.1.1）_2048682075724718081.json, 视频生成/图生视频/图片对口型_infiniteTalk_声音克隆混合版_2072325525946851330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_513

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/D_I2V（V1.1.1）_2047149486551605249.json、视频生成/图生视频/I2V-林小茶_2047141901102489601.json、视频生成/图生视频/Infinite或者Infinite+IndexTTS2(单人)_1993149833712254977.json、视频生成/图生视频/V4.1（demo2）_2051961839407386625.json、视频生成/图生视频/X_I2V（V1.1.1）_2048682075724718081.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
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
- `WanVideoPassImagesFromSamples`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `Wav2VecModelLoader` —— 5/6 个有
- `FB_Qwen3TTSVoiceClone` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `PreviewAudio` —— 4/6 个有
- `ResizeImagesByLongerEdge` —— 4/6 个有
- `Text` —— 4/6 个有
- `IndexTTS2Run` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `AudioToFPS` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `ImpactConditionalBranch` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RunningHub Deepcleaner` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
