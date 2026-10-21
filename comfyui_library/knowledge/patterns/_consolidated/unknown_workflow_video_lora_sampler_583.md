---
name: unknown_workflow_video_lora_sampler_583
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.783
common_nodes: [AudioCrop, AudioCropProcessUTK, CM_IntToFloat, CR Text, CR Text Concatenate, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PrimitiveString, RH_Captioner, RH_LLMAPI_NODE, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: [AudioCropProcessUTK, CR Text, CR Text Concatenate, ImageFromBatch+, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, easy imageConcat, easy int]
members: [视频生成/图生视频/1973665727783809025.json, 视频生成/图生视频/1974314423789727745.json, 视频生成/文生视频/1973665727783809025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_583

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1973665727783809025.json、视频生成/图生视频/1974314423789727745.json、视频生成/文生视频/1973665727783809025.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioCropProcessUTK`
- `CM_IntToFloat`
- `CR Text`
- `CR Text Concatenate`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `PrimitiveString`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CM_FloatUnaryOperation` —— 2/3 个有
- `HuMoEmbeds` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `LayerUtility: CropByMask V2` —— 2/3 个有
- `LoadLynxResampler` —— 2/3 个有
- `RMBG` —— 2/3 个有
- `WhisperModelLoader` —— 2/3 个有
- `easy imageConcat` —— 2/3 个有
- `AudioEncoderEncode` —— 1/3 个有
- `AudioEncoderLoader` —— 1/3 个有
- `LazySwitch1way` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `WanVideoAddS2VEmbeds` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：AudioCropProcessUTK、CR Text、CR Text Concatenate、ImageFromBatch+、LayerUtility: CropByMask V2
