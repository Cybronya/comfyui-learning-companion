---
name: unknown_workflow_video_lora_sampler_687
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.683667
common_nodes: [Audio Duration (mtb), BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DownloadAndLoadWav2VecModel, DrawMaskOnImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PointsEditor, PreviewAny, ReverseImageBatch, Sam2Segmentation, SetNode, SimpleMath+, ToInt, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2018290540470607873.json, 视频生成/图生视频/2027669191704186881.json, 视频生成/图生视频/2007293154239713282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_687

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2018290540470607873.json、视频生成/图生视频/2027669191704186881.json、视频生成/图生视频/2007293154239713282.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DownloadAndLoadWav2VecModel`
- `DrawMaskOnImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PointsEditor`
- `PreviewAny`
- `ReverseImageBatch`
- `Sam2Segmentation`
- `SetNode`
- `SimpleMath+`
- `ToInt`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 2/3 个有
- `LayerMask: MaskGrow` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy sam3ModelLoader` —— 2/3 个有
- `easy sam3VideoSegmentation` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ACE_TextGoogleTranslate` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
