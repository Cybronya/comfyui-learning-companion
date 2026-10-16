---
key: 视频生成/图生视频/双模双采加速｜MinimaxH3 hybrid+remix双larry工作流_2093241754479845378.json
name: 双模双采加速｜MinimaxH3 hybrid+remix双larry工作流_2093241754479845378
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/双模双采加速｜MinimaxH3 hybrid+remix双larry工作流_2093241754479845378.json
hash: 51096d1d42b46981
coverage: 0.921053
learned_at: 2026-10-16 23:42:56
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, ModelPreviewOverrideKJ, ShellAgentPluginVideoCombineEncrypt, SamplerCustomAdvanced, BasicScheduler, H3SigmaRefiner, SplitSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, KSamplerSelect, BasicGuider, ModelPreviewOverrideKJ, BasicGuider, SplitSigmas, BasicScheduler, H3SigmaRefiner, easy cleanGpuUsed, MiniMaxH3MemoryEfficientSageAttentionPatch, ComfyMathExpression, LoadImage, PrimitiveStringMultiline, MiniMaxLowVRAMAttention, Seed (rgthree), MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoadImage, CLIPLoader, VAELoader, VAELoader, UNETLoader, MiniMaxH3ReferenceToVideo, RandomNoise, MiniMaxLowVRAMAttention, MiniMaxH3TurboLoRA, MiniMaxH3SigmaShift, ModelAttentionBackend, MiniMaxH3TurboLoRA, MiniMaxH3SigmaShift, ModelAttentionBackend, VAEDecode, VHS_VideoCombine, VAEDecodeAudio, MinimaxH3LatentUpscaler3D, ResolutionSelector, PrimitiveFloat, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/双模双采加速｜MinimaxH3 hybrid+remix双larry工作流_2093241754479845378.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/双模双采加速｜MinimaxH3 hybrid+remix双larry工作流_2093241754479845378.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
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
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（70/76）

**有卡**：`LoadImage`、`ModelPreviewOverrideKJ`、`ShellAgentPluginVideoCombineEncrypt`、`SamplerCustomAdvanced`、`BasicScheduler`、`H3SigmaRefiner`、`SplitSigmas`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicGuider`、`easy cleanGpuUsed`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ComfyMathExpression`、`MiniMaxLowVRAMAttention`、`Seed (rgthree)`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`、`MiniMaxH3TurboLoRA`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`VAEDecode`、`VHS_VideoCombine`、`VAEDecodeAudio`、`MinimaxH3LatentUpscaler3D`、`ResolutionSelector`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
