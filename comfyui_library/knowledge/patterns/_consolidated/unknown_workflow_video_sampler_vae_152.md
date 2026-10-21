---
name: unknown_workflow_video_sampler_vae_152
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.931333
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CM_FloatToInt, CR Prompt Text, ImageResize+, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PlaySound|pysssss, PreviewAudio, SoundFlow_GetLength, VHS_VideoCombine, WanVideoAddAudioEmbeds, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1983508119022149633.json, 视频生成/图生视频/1984410578229870594.json, 视频生成/图生视频/1981551177856892929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_152

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1983508119022149633.json、视频生成/图生视频/1984410578229870594.json、视频生成/图生视频/1981551177856892929.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CM_FloatToInt`
- `CR Prompt Text`
- `ImageResize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `PlaySound|pysssss`
- `PreviewAudio`
- `SoundFlow_GetLength`
- `VHS_VideoCombine`
- `WanVideoAddAudioEmbeds`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 2/3 个有
- `PreviewImage` —— 1/3 个有
- `WanVideoBlockSwap` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `WanVideoModelLoader` —— 1/3 个有
- `WanVideoSetBlockSwap` —— 1/3 个有
- `WanVideoSetLoRAs` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
