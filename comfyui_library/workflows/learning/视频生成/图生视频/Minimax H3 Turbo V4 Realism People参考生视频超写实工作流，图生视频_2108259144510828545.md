---
key: 视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json
name: Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json
hash: a8fb1b24a14815c3
coverage: 0.510638
learned_at: 2026-10-17 22:18:42
nodes: [SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, SetNode, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, ComfyMathExpression, SetNode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, LoadAudio, SetNode, LoadAudio, SetNode, RandomNoise, KSamplerSelect, SplitSigmas, LoadImage, VHS_LoadVideo, VHS_VideoCombine, SamplerCustomAdvanced, SetNode, MinimaxH3LatentUpscaler3D, BasicScheduler, VHS_VideoCombine, LoadAudio, LoadImage, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, Text, easy float, SetNode, SetNode, GetNode, MiniMaxH3DualClockSamplerT8, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（141 个）：
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `ComfyMathExpression`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `MinimaxH3LatentUpscaler3D`
- `BasicScheduler`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `ResolutionSelector`
- `Text`
- `easy float`
- `SetNode`
- `SetNode`
- `GetNode`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **51%**（72/141）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`VAEDecodeAudio`、`VAEDecode`、`MiniMaxH3ReferenceToVideo`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LoadAudio`、`RandomNoise`、`KSamplerSelect`、`SplitSigmas`、`VHS_VideoCombine`、`MinimaxH3LatentUpscaler3D`、`BasicScheduler`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ResolutionSelector`、`Text`、`easy float`、`MiniMaxH3DualClockSamplerT8`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
