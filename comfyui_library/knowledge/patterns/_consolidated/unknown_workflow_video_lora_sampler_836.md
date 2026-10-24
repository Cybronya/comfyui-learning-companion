---
name: unknown_workflow_video_lora_sampler_836
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.912
common_nodes: [AudioCrop, AudioCropProcessUTK, CM_IntToFloat, CR Text, CR Text Concatenate, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PrimitiveString, RH_Captioner, RH_LLMAPI_NODE, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/wan-S2V-数字人_1974314423789727745.json, 视频生成/文生视频/数字人-文生视频-Humo_1973665727783809025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_836

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan-S2V-数字人_1974314423789727745.json、视频生成/文生视频/数字人-文生视频-Humo_1973665727783809025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
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
- `AudioEncoderEncode` —— 1/2 个有
- `AudioEncoderLoader` —— 1/2 个有
- `CM_FloatUnaryOperation` —— 1/2 个有
- `HuMoEmbeds` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LayerUtility: CropByMask V2` —— 1/2 个有
- `LazySwitch1way` —— 1/2 个有
- `LoadLynxResampler` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `WanVideoAddS2VEmbeds` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WhisperModelLoader` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
