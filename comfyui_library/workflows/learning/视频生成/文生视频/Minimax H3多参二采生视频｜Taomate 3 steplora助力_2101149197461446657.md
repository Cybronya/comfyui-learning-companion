---
key: 视频生成/文生视频/Minimax H3多参二采生视频｜Taomate 3 steplora助力_2101149197461446657.json
name: Minimax H3多参二采生视频｜Taomate 3 steplora助力_2101149197461446657
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3多参二采生视频｜Taomate 3 steplora助力_2101149197461446657.json
hash: 1484f4de08e021f9
coverage: 0.924051
learned_at: 2026-10-15 22:46:36
nodes: [VAELoader, VAELoader, VAEDecode, VAEDecodeAudio, LTXVConcatAVLatent, ModelPreviewOverrideKJ, VAEDecodeAudio, SamplerCustomAdvanced, KSamplerSelect, VAEDecode, UNETLoader, RandomNoise, ComfyMathExpression, CreateVideo, SaveVideo, LoadImage, PrimitiveFloat, MiniMaxH3SigmaShift, ModelAttentionBackend, BasicGuider, ManualSigmas, MinimaxH3LatentUpscaler3D, ClownsharKSampler_Beta, ClownsharKSampler_Beta, SeedGenerator, ConditioningZeroOut, LTXVSeparateAVLatent, MiniMaxH3ReferenceToVideo, Text, PrimitiveFloat, ResolutionSelector, LoraLoaderModelOnly, LoraLoaderModelOnly, CreateVideo, SaveVideo, CLIPLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Minimax H3多参二采生视频｜Taomate 3 steplora助力_2101149197461446657.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3多参二采生视频｜Taomate 3 steplora助力_2101149197461446657.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LTXVConcatAVLatent`
- `ModelPreviewOverrideKJ`
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `RandomNoise`
- `ComfyMathExpression`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `PrimitiveFloat`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BasicGuider`
- `ManualSigmas`
- `MinimaxH3LatentUpscaler3D`
- `ClownsharKSampler_Beta` ★核心
- `ClownsharKSampler_Beta` ★核心
- `SeedGenerator`
- `ConditioningZeroOut`
- `LTXVSeparateAVLatent`
- `MiniMaxH3ReferenceToVideo`
- `Text`
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

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

覆盖率 **92%**（73/79）

**有卡**：`VAELoader`、`VAEDecode`、`VAEDecodeAudio`、`LTXVConcatAVLatent`、`ModelPreviewOverrideKJ`、`SamplerCustomAdvanced`、`KSamplerSelect`、`UNETLoader`、`RandomNoise`、`ComfyMathExpression`、`CreateVideo`、`SaveVideo`、`LoadImage`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BasicGuider`、`ManualSigmas`、`MinimaxH3LatentUpscaler3D`、`ClownsharKSampler_Beta`、`SeedGenerator`、`ConditioningZeroOut`、`LTXVSeparateAVLatent`、`MiniMaxH3ReferenceToVideo`、`Text`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
