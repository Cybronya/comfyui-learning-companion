---
name: unknown_workflow_video_upscale_lora_21
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.631667
common_nodes: [DownloadAndLoadWav2VecModel, FaceRestoreCFWithModel, FaceRestoreModelLoader, Float, GetNode, ImageFromBatch+, ImageResize+, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, NormalizeAudioLoudness, Note _O, PreviewAudio, PrimitiveBoolean, RH_Captioner, RH_GetAudioDuration, ReActorFaceSwap, SetNode, SimpleMath+, Text Concatenate, Text Multiline, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/子易奇谭V2.0beta_1965268707083735042.json, 视频生成/图生视频/子易奇谭V2.0【仅首帧+wan2.2 insight】_1973648860415397889.json, 视频生成/图生视频/子易奇谭V2.0仅首帧_1965183125162704897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/子易奇谭V2.0beta_1965268707083735042.json、视频生成/图生视频/子易奇谭V2.0【仅首帧+wan2.2 insight】_1973648860415397889.json、视频生成/图生视频/子易奇谭V2.0仅首帧_1965183125162704897.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadWav2VecModel`
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `Float`
- `GetNode`
- `ImageFromBatch+`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `NormalizeAudioLoudness`
- `Note _O`
- `PreviewAudio`
- `PrimitiveBoolean`
- `RH_Captioner`
- `RH_GetAudioDuration`
- `ReActorFaceSwap`
- `SetNode`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CreateCFGScheduleFloatList` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/3 个有
- `StringToFloatList` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `WanVideoImageToVideoMultiTalk` —— 1/3 个有
- `WanVideoScheduler` —— 1/3 个有
- `WanVideoSigmaToStep` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
