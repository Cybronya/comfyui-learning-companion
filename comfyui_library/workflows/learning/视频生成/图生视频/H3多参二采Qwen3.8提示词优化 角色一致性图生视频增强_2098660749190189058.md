---
key: 视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json
name: H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json
hash: a528224fb23393d6
coverage: 0.506944
learned_at: 2026-10-17 01:44:23
nodes: [MiniMaxH3PromptEnhancerT8, SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, VHS_LoadVideo, SetNode, SetNode, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, SetNode, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, LoadAudio, SetNode, LoadAudio, SetNode, LoadAudio, SetNode, RandomNoise, KSamplerSelect, SetNode, GetNode, VHS_VideoCombine, BasicScheduler, SplitSigmas, VHS_VideoCombine, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, PrimitiveFloat, easy float, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, SetNode, CR Prompt Text, easy showAnything, RH_Translator, PreviewAny, easy saveText, easy saveText, SetNode, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（144 个）：
- `MiniMaxH3PromptEnhancerT8`
- `SetNode`
- `VAELoader`
- `VAELoader`
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
- `CLIPLoader`
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
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
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
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `BasicScheduler`
- `SplitSigmas`
- `VHS_VideoCombine`
- `MinimaxH3LatentUpscaler3D`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveFloat`
- `easy float`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
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
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CR Prompt Text`
- `easy showAnything`
- `RH_Translator`
- `PreviewAny`
- `easy saveText`
- `easy saveText`
- `SetNode`
- `LoadImage`
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

覆盖率 **51%**（73/144）

**有卡**：`MiniMaxH3PromptEnhancerT8`、`VAELoader`、`VHS_LoadVideo`、`LoadImage`、`CLIPLoader`、`VAEDecodeAudio`、`VAEDecode`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LoadAudio`、`RandomNoise`、`KSamplerSelect`、`VHS_VideoCombine`、`BasicScheduler`、`SplitSigmas`、`MinimaxH3LatentUpscaler3D`、`ResolutionSelector`、`easy float`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CR Prompt Text`、`RH_Translator`、`easy saveText`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
