---
name: unknown_workflow_video_lora_sampler_528
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.67325
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1958336218591334402.json, 视频生成/图生视频/2010602329619304450.json, 视频生成/图生视频/2010621857124323330.json, 视频生成/图生视频/1969815681778786306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_528

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1958336218591334402.json、视频生成/图生视频/2010602329619304450.json、视频生成/图生视频/2010621857124323330.json、视频生成/图生视频/1969815681778786306.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
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
- `VHS_LoadVideo` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `AudioCropProcessUTK` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `LayerUtility: TextBox` —— 2/4 个有
- `PDIMAGE_LongerSize` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ImageScaleByAspectRatio_UTK` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
