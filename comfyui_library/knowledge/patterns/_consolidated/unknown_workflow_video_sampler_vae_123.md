---
name: unknown_workflow_video_sampler_vae_123
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CM_FloatToInt, CR Prompt Text, ImageResize+, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PlaySound|pysssss, PreviewAudio, SoundFlow_GetLength, VHS_VideoCombine, WanVideoAddAudioEmbeds, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/s2v口播_1962087593619996674.json, 视频生成/图生视频/S2V-长视频数字人工作流_1983508119022149633.json, 视频生成/图生视频/S2V-长视频数字人工作流_1984410578229870594.json, 视频生成/图生视频/video_wan2_2_s2v口播_1981551177856892929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_123

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/s2v口播_1962087593619996674.json、视频生成/图生视频/S2V-长视频数字人工作流_1983508119022149633.json、视频生成/图生视频/S2V-长视频数字人工作流_1984410578229870594.json、视频生成/图生视频/video_wan2_2_s2v口播_1981551177856892929.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `RHHiddenNodes` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `WanVideoBlockSwap` —— 1/4 个有
- `WanVideoLoraSelectMulti` —— 1/4 个有
- `WanVideoModelLoader` —— 1/4 个有
- `WanVideoSetBlockSwap` —— 1/4 个有
- `WanVideoSetLoRAs` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
