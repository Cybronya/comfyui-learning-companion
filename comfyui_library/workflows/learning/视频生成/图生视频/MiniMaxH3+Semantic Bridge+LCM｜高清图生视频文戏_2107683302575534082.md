---
key: 视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏_2107683302575534082.json
name: MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏_2107683302575534082
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏_2107683302575534082.json
hash: a9158a42230cb1f9
coverage: 0.924051
learned_at: 2026-10-17 22:18:27
nodes: [VAELoader, VAELoader, RandomNoise, KSamplerSelect, CLIPLoader, MiniMaxH3SigmaShift, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, BasicScheduler, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, CLIPTextEncode, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, RH_Screenwriter, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, H3SigmaRefiner, CFGGuider, ResolutionSelector, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, WujiCleaner, VHS_VideoCombine, Int, PrimitiveStringMultiline, WujiH3PromptEnhancer, easy promptConcat, ComfyMathExpression, MiniMaxH3AudioConditioningT8, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏_2107683302575534082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏_2107683302575534082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `VAELoader`
- `VAELoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `MiniMaxH3SigmaShift`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `BasicScheduler`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `RH_Screenwriter`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `H3SigmaRefiner`
- `CFGGuider`
- `ResolutionSelector`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `WujiCleaner`
- `VHS_VideoCombine`
- `Int`
- `PrimitiveStringMultiline`
- `WujiH3PromptEnhancer`
- `easy promptConcat`
- `ComfyMathExpression`
- `MiniMaxH3AudioConditioningT8`
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

覆盖率 **92%**（73/79）

**有卡**：`VAELoader`、`RandomNoise`、`KSamplerSelect`、`CLIPLoader`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`UNETLoader`、`BasicScheduler`、`LoadImage`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CLIPTextEncode`、`ImageResizeKJv2`、`RH_Screenwriter`、`MiniMaxH3SemanticBridgeApplyT8`、`MiniMaxH3SemanticBridgeConfigT8`、`H3SigmaRefiner`、`CFGGuider`、`ResolutionSelector`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`WujiCleaner`、`VHS_VideoCombine`、`Int`、`WujiH3PromptEnhancer`、`easy promptConcat`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
