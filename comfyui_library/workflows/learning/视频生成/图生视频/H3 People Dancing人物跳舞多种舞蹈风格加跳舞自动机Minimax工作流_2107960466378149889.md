---
key: 视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json
name: H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json
hash: 34b7ad9b6a2c0d03
coverage: 0.895522
learned_at: 2026-10-17 22:17:20
nodes: [VAELoader, VAELoader, ManualSigmas, VAEDecode, VAEDecodeAudio, SplitSigmas, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, BasicScheduler, BasicGuider, BasicGuider, ManualSigmas, LTXVSeparateAVLatent, VAEDecode, VAEDecodeAudio, ModelAttentionBackend, MiniMaxH3SigmaShift, RandomNoise, VHS_VideoCombine, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, UNETLoader, ModelPreviewOverrideKJ, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, ResolutionSelector, RHHiddenNodes, easy showAnything, ComfyMathExpression, PrimitiveFloat, CR Prompt Text, LoadImage, EmptyImage, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `VAELoader`
- `VAELoader`
- `ManualSigmas`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SplitSigmas`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `BasicScheduler`
- `BasicGuider`
- `BasicGuider`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ReferenceToVideo`
- `UNETLoader` ★核心
- `ModelPreviewOverrideKJ`
- `MinimaxH3LatentUpscaler3D`
- `LTXVConcatAVLatent`
- `ResolutionSelector`
- `RHHiddenNodes`
- `easy showAnything`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `CR Prompt Text`
- `LoadImage`
- `EmptyImage`
- `PreviewImage`
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

覆盖率 **90%**（60/67）

**有卡**：`VAELoader`、`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`SplitSigmas`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`LTXVSeparateAVLatent`、`ModelAttentionBackend`、`MiniMaxH3SigmaShift`、`RandomNoise`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`、`ModelPreviewOverrideKJ`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`ResolutionSelector`、`RHHiddenNodes`、`ComfyMathExpression`、`CR Prompt Text`、`LoadImage`、`EmptyImage`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
