---
key: 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2109442962584334337.json
name: 电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2109442962584334337
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2109442962584334337.json
hash: 83b068021570d5c5
coverage: 0.636986
learned_at: 2026-10-18 00:24:43
nodes: [SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, SetNode, SetNode, SetNode, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, RandomNoise, KSamplerSelect, SetNode, GetNode, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, LoadImage, easy float, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, easy showAnything, RH_Translator, PreviewAny, easy saveText, easy saveText, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoadImage, LoadImage, SetNode, ComfyMathExpression, SetNode, easy indexTTSForceCleanup, SamplerCustomAdvanced, easy indexTTSForceCleanup, BasicScheduler, SplitSigmas, PrimitiveFloat, CR Prompt Text, MiniMaxH3PromptEnhancerT8, ResolutionSelector, VHS_VideoCombine, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, LoadImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2109442962584334337.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2109442962584334337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（146 个）：
- `SetNode`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `MinimaxH3LatentUpscaler3D`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy float`
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
- `ComfyMathExpression`
- `SetNode`
- `easy indexTTSForceCleanup`
- `SamplerCustomAdvanced` ★核心
- `easy indexTTSForceCleanup`
- `BasicScheduler`
- `SplitSigmas`
- `PrimitiveFloat`
- `CR Prompt Text`
- `MiniMaxH3PromptEnhancerT8`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
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
- `SaveImage`
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
- `LoadImage`
- `PreviewImage`

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

覆盖率 **64%**（93/146）

**有卡**：`VAELoader`、`CLIPLoader`、`VAEDecodeAudio`、`VAEDecode`、`BasicGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RandomNoise`、`KSamplerSelect`、`MinimaxH3LatentUpscaler3D`、`LoadImage`、`easy float`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RH_Translator`、`easy saveText`、`LoraLoaderModelOnly`、`UNETLoader`、`ComfyMathExpression`、`easy indexTTSForceCleanup`、`BasicScheduler`、`SplitSigmas`、`CR Prompt Text`、`MiniMaxH3PromptEnhancerT8`、`ResolutionSelector`、`VHS_VideoCombine`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
