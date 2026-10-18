---
key: 视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json
name: H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json
hash: e6a7c51f760893c2
coverage: 0.517007
learned_at: 2026-10-17 22:17:26
nodes: [SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, VHS_LoadVideo, SetNode, SetNode, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, SetNode, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, SetNode, SetNode, SetNode, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, LoadAudio, SetNode, LoadAudio, SetNode, LoadAudio, SetNode, RandomNoise, KSamplerSelect, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, LoadImage, easy float, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, easy showAnything, RH_Translator, PreviewAny, easy saveText, easy saveText, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoadImage, LoadImage, SetNode, ResolutionSelector, ComfyMathExpression, SetNode, CR Prompt Text, easy indexTTSForceCleanup, SamplerCustomAdvanced, easy indexTTSForceCleanup, BasicScheduler, SplitSigmas, MiniMaxH3PromptEnhancerT8, PrimitiveFloat, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（147 个）：
- `SetNode`
- `VAELoader`
- `VAELoader`
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
- `VHS_VideoCombine`
- `MinimaxH3LatentUpscaler3D`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `easy showAnything`
- `RH_Translator`
- `PreviewAny`
- `easy saveText`
- `easy saveText`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `SetNode`
- `ResolutionSelector`
- `ComfyMathExpression`
- `SetNode`
- `CR Prompt Text`
- `easy indexTTSForceCleanup`
- `SamplerCustomAdvanced` ★核心
- `easy indexTTSForceCleanup`
- `BasicScheduler`
- `SplitSigmas`
- `MiniMaxH3PromptEnhancerT8`
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

覆盖率 **52%**（76/147）

**有卡**：`VAELoader`、`VHS_LoadVideo`、`LoadImage`、`CLIPLoader`、`VAEDecodeAudio`、`VAEDecode`、`BasicGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LoadAudio`、`RandomNoise`、`KSamplerSelect`、`VHS_VideoCombine`、`MinimaxH3LatentUpscaler3D`、`easy float`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RH_Translator`、`easy saveText`、`LoraLoaderModelOnly`、`UNETLoader`、`ResolutionSelector`、`ComfyMathExpression`、`CR Prompt Text`、`easy indexTTSForceCleanup`、`BasicScheduler`、`SplitSigmas`、`MiniMaxH3PromptEnhancerT8`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
