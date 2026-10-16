---
key: 视频生成/图生视频/双模双采hybird+remix｜MinimaxH3图生视频双larry加速_2093078463535210498.json
name: 双模双采hybird+remix｜MinimaxH3图生视频双larry加速_2093078463535210498
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/双模双采hybird+remix｜MinimaxH3图生视频双larry加速_2093078463535210498.json
hash: 5921729900d799d0
coverage: 0.923077
learned_at: 2026-10-16 22:59:53
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, ModelPreviewOverrideKJ, ShellAgentPluginVideoCombineEncrypt, SamplerCustomAdvanced, BasicScheduler, H3SigmaRefiner, SplitSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, KSamplerSelect, BasicGuider, ModelPreviewOverrideKJ, BasicGuider, SplitSigmas, BasicScheduler, H3SigmaRefiner, easy cleanGpuUsed, MiniMaxH3MemoryEfficientSageAttentionPatch, ComfyMathExpression, LoadImage, PrimitiveStringMultiline, MiniMaxLowVRAMAttention, Seed (rgthree), MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoadImage, CLIPLoader, VAELoader, VAELoader, UNETLoader, MiniMaxH3ReferenceToVideo, RandomNoise, MiniMaxLowVRAMAttention, MiniMaxH3TurboLoRA, MiniMaxH3SigmaShift, ModelAttentionBackend, MiniMaxH3TurboLoRA, MiniMaxH3SigmaShift, ModelAttentionBackend, VAEDecode, VHS_VideoCombine, VAEDecodeAudio, MinimaxH3LatentUpscaler3D, ResolutionSelector, PrimitiveFloat, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/双模双采hybird+remix｜MinimaxH3图生视频双larry加速_2093078463535210498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/双模双采hybird+remix｜MinimaxH3图生视频双larry加速_2093078463535210498.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ModelPreviewOverrideKJ`
- `ShellAgentPluginVideoCombineEncrypt`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `H3SigmaRefiner`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ModelPreviewOverrideKJ`
- `BasicGuider`
- `SplitSigmas`
- `BasicScheduler`
- `H3SigmaRefiner`
- `easy cleanGpuUsed`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ComfyMathExpression`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MiniMaxLowVRAMAttention`
- `Seed (rgthree)`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `MiniMaxLowVRAMAttention`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAEDecodeAudio` ★核心
- `MinimaxH3LatentUpscaler3D`
- `ResolutionSelector`
- `PrimitiveFloat`
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
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
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

覆盖率 **92%**（72/78）

**有卡**：`LoadImage`、`ModelPreviewOverrideKJ`、`ShellAgentPluginVideoCombineEncrypt`、`SamplerCustomAdvanced`、`BasicScheduler`、`H3SigmaRefiner`、`SplitSigmas`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicGuider`、`easy cleanGpuUsed`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ComfyMathExpression`、`MiniMaxLowVRAMAttention`、`Seed (rgthree)`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`、`MiniMaxH3TurboLoRA`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`VAEDecode`、`VHS_VideoCombine`、`VAEDecodeAudio`、`MinimaxH3LatentUpscaler3D`、`ResolutionSelector`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
