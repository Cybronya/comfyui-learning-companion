---
key: 视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json
name: MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json
hash: 2cff3241a815b2a3
coverage: 0.918033
learned_at: 2026-10-18 00:23:29
nodes: [PathchSageAttentionKJ, BasicScheduler, VAEDecode, SamplerCustomAdvanced, MiniMaxLowVRAMAttention, RandomNoise, KSamplerSelect, CFGGuider, MiniMaxH3SigmaShift, LTXVSeparateAVLatent, VAEDecodeAudio, VAELoader, CreateVideo, LTXVConcatAVLatent, SaveVideo, SamplerCustomAdvanced, VRAM_Debug, VRAM_Debug, SplitSigmas, LoraLoaderModelOnly, ConditioningZeroOut, CFGGuider, UNETLoader, CLIPLoader, VAELoader, ComfyMathExpression, PrimitiveFloat, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxLowVRAMAttention`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `MiniMaxH3SigmaShift`
- `LTXVSeparateAVLatent`
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `VRAM_Debug`
- `VRAM_Debug`
- `SplitSigmas`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `CFGGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **92%**（56/61）

**有卡**：`PathchSageAttentionKJ`、`BasicScheduler`、`VAEDecode`、`SamplerCustomAdvanced`、`MiniMaxLowVRAMAttention`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`MiniMaxH3SigmaShift`、`LTXVSeparateAVLatent`、`VAEDecodeAudio`、`VAELoader`、`CreateVideo`、`LTXVConcatAVLatent`、`SaveVideo`、`VRAM_Debug`、`SplitSigmas`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`ComfyMathExpression`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`MinimaxH3LatentUpscaler3D`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
