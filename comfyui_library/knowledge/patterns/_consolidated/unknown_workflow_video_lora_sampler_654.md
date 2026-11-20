---
name: unknown_workflow_video_lora_sampler_654
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.914667
common_nodes: [AudioCrop, AudioCropProcessUTK, CM_IntToFloat, CR Text, CR Text Concatenate, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PrimitiveString, RH_Captioner, RH_LLMAPI_NODE, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [数字人/数字人/Wan-S2V-数字人(说话、唱歌）_1990712412338884610.json, 视频生成/图生视频/wan-S2V-数字人_1974314423789727745.json, 视频生成/文生视频/数字人-文生视频-Humo_1973665727783809025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_654

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/Wan-S2V-数字人(说话、唱歌）_1990712412338884610.json、视频生成/图生视频/wan-S2V-数字人_1974314423789727745.json、视频生成/文生视频/数字人-文生视频-Humo_1973665727783809025.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

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
- `AudioEncoderEncode` —— 2/3 个有
- `AudioEncoderLoader` —— 2/3 个有
- `LazySwitch1way` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `WanVideoAddS2VEmbeds` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `WanVideoEmptyEmbeds` —— 2/3 个有
- `WanVideoEncode` —— 2/3 个有
- `CM_FloatUnaryOperation` —— 1/3 个有
- `HuMoEmbeds` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LayerUtility: CropByMask V2` —— 1/3 个有
- `LoadLynxResampler` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `WhisperModelLoader` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
