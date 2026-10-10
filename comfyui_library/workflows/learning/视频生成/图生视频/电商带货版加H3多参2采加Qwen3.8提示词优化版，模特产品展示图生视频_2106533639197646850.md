---
key: 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106533639197646850.json
name: 电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106533639197646850
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106533639197646850.json
hash: 7f0127240badb69a
coverage: 0.508333
learned_at: 2026-10-10 22:55:16
nodes: [SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, SetNode, SetNode, SetNode, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, RandomNoise, KSamplerSelect, SetNode, GetNode, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, LoadImage, easy float, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, easy showAnything, RH_Translator, PreviewAny, easy saveText, easy saveText, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoadImage, LoadImage, SetNode, ComfyMathExpression, SetNode, easy indexTTSForceCleanup, SamplerCustomAdvanced, easy indexTTSForceCleanup, BasicScheduler, SplitSigmas, PrimitiveFloat, CR Prompt Text, MiniMaxH3PromptEnhancerT8, ResolutionSelector, VHS_VideoCombine, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: [easy float, easy indexTTSForceCleanup, easy indexTTSForceCleanup, CR Prompt Text, easy saveText, easy saveText]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexTTSForceCleanup` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexTTSForceCleanup` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106533639197646850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106533639197646850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（120 个）：
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

覆盖率 **51%**（61/120）

**有卡**：`VAELoader`、`CLIPLoader`、`VAEDecodeAudio`、`VAEDecode`、`BasicGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RandomNoise`、`KSamplerSelect`、`MinimaxH3LatentUpscaler3D`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RH_Translator`、`LoraLoaderModelOnly`、`UNETLoader`、`ComfyMathExpression`、`BasicScheduler`、`SplitSigmas`、`MiniMaxH3PromptEnhancerT8`、`ResolutionSelector`、`VHS_VideoCombine`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**缺卡**（6）：`easy float`、`easy indexTTSForceCleanup`、`easy indexTTSForceCleanup`、`CR Prompt Text`、`easy saveText`、`easy saveText`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexTTSForceCleanup` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexTTSForceCleanup` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
