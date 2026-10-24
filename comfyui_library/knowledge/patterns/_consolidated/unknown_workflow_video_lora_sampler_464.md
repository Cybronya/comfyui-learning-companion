---
name: unknown_workflow_video_lora_sampler_464
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6885
common_nodes: [Audio Duration (mtb), BlockifyMask, CLIPVisionLoader, DownloadAndLoadWav2VecModel, DrawMaskOnImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PointsEditor, PreviewAny, ReverseImageBatch, SetNode, SimpleMath+, ToInt, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [图片生成/图生图/视频对口型-多人选一人+老八v3_2028080510215397377.json, 视频生成/图生视频/视频对口型-多人选一人 老八_2018290540470607873.json, 视频生成/图生视频/视频对口型-多人选一人+老八v2_2027669191704186881.json, 视频生成/图生视频/视频对口型-多人选一人_2007293154239713282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_464

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/视频对口型-多人选一人+老八v3_2028080510215397377.json、视频生成/图生视频/视频对口型-多人选一人 老八_2018290540470607873.json、视频生成/图生视频/视频对口型-多人选一人+老八v2_2027669191704186881.json、视频生成/图生视频/视频对口型-多人选一人_2007293154239713282.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `Audio Duration (mtb)`
- `BlockifyMask`
- `CLIPVisionLoader`
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
- `DownloadAndLoadSAM2Model` —— 3/4 个有
- `LayerMask: MaskGrow` —— 3/4 个有
- `Sam2Segmentation` —— 3/4 个有
- `easy sam3ModelLoader` —— 3/4 个有
- `easy sam3VideoSegmentation` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ACE_TextGoogleTranslate` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `GrowMask` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RunningHub Deepcleaner` —— 2/4 个有
- `RH_Translator` —— 1/4 个有
- `SeCModelLoader` —— 1/4 个有
- `SeCVideoSegmentation` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
