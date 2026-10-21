---
name: unknown_workflow_video_lora_sampler_381
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7975
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, PreviewAudio, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1967501356460335105.json, 视频生成/图生视频/1996928089819136001.json, 视频生成/图生视频/2010602329619304450.json, 视频生成/图生视频/1996900266379300866.json, 视频生成/图生视频/2000473873579638786.json, 视频生成/图生视频/2010621857124323330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_381

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1967501356460335105.json、视频生成/图生视频/1996928089819136001.json、视频生成/图生视频/2010602329619304450.json、视频生成/图生视频/1996900266379300866.json、视频生成/图生视频/2000473873579638786.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `PreviewAudio`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `AudioCrop` —— 4/6 个有
- `ImageUpscaleWithModel` —— 3/6 个有
- `IndexTTS2Run` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `UpscaleModelLoader` —— 3/6 个有
- `AudioCropProcessUTK` —— 2/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `LayerUtility: TextBox` —— 2/6 个有
- `WanVideoEncode` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `Fast Bypasser (rgthree)` —— 1/6 个有
- `ImageScaleByAspectRatio_UTK` —— 1/6 个有
- `MelBandRoFormerModelLoader` —— 1/6 个有
- `MelBandRoFormerSampler` —— 1/6 个有
- `Switch any [Crystools]` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `Wav2VecModelLoader` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
