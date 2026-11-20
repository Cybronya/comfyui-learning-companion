---
name: unknown_workflow_video_lora_sampler_222
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.664
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/视频对口型-多人选一人+老八v3_2028080510215397377.json, 平台全量/台词替换_2035184205684019202.json, 数字人/数字人/InfiniteTalk_V2V_多人场面控制单人说话-高画质版720p_2010599724411260929.json, 数字人/数字人/InfiniteTalk_V2V_多人场面控制单人说话_2000188855288557569.json, 数字人/数字人/数字人单人2_2042547376166014978.json, 数字人/数字人/数字人单人3_2043371209026441217.json, 数字人/数字人/数字人单人_2042510576282247169.json, 数字人/数字人/视频对口型-多人选一人_2004086022214434817.json, 视频生成/图生视频/视频对口型-多人选一人 老八_2018290540470607873.json, 视频生成/图生视频/视频对口型-多人选一人+老八v2_2027669191704186881.json, 视频生成/图生视频/视频对口型-多人选一人_2007293154239713282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_222

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/视频对口型-多人选一人+老八v3_2028080510215397377.json、平台全量/台词替换_2035184205684019202.json、数字人/数字人/InfiniteTalk_V2V_多人场面控制单人说话-高画质版720p_2010599724411260929.json、数字人/数字人/InfiniteTalk_V2V_多人场面控制单人说话_2000188855288557569.json、数字人/数字人/数字人单人2_2042547376166014978.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
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

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 10/11 个有
- `BlockifyMask` —— 10/11 个有
- `DrawMaskOnImage` —— 10/11 个有
- `ImageBatchMulti` —— 10/11 个有
- `PointsEditor` —— 10/11 个有
- `ReverseImageBatch` —— 10/11 个有
- `SimpleMath+` —— 10/11 个有
- `ToInt` —— 10/11 个有
- `Wav2VecModelLoader` —— 10/11 个有
- `DownloadAndLoadSAM2Model` —— 9/11 个有
- `Sam2Segmentation` —— 9/11 个有
- `GrowMask` —— 8/11 个有
- `PreviewImage` —— 8/11 个有
- `easy sam3ModelLoader` —— 4/11 个有
- `JjkText` —— 3/11 个有
- `LayerMask: MaskGrow` —— 3/11 个有
- `ShowText` —— 3/11 个有
- `easy sam3VideoSegmentation` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `ACE_TextGoogleTranslate` —— 2/11 个有
- `CR Text` —— 2/11 个有
- `RunningHub Deepcleaner` —— 2/11 个有
- `1hew_MaskBatchToList` —— 1/11 个有
- `RH_Translator` —— 1/11 个有
- `SeCModelLoader` —— 1/11 个有
- `SeCVideoSegmentation` —— 1/11 个有
- `easy sam3ImageSegmentation` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
