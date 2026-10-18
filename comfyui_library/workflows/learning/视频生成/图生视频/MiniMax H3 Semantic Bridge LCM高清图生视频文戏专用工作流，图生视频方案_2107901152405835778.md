---
key: 视频生成/图生视频/MiniMax H3 Semantic Bridge LCM高清图生视频文戏专用工作流，图生视频方案_2107901152405835778.json
name: MiniMax H3 Semantic Bridge LCM高清图生视频文戏专用工作流，图生视频方案_2107901152405835778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Semantic Bridge LCM高清图生视频文戏专用工作流，图生视频方案_2107901152405835778.json
hash: 7d75e574525a1a4d
coverage: 0.909091
learned_at: 2026-10-17 22:18:04
nodes: [VAELoader, VAELoader, RandomNoise, KSamplerSelect, CLIPLoader, MiniMaxH3SigmaShift, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, BasicScheduler, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, CLIPTextEncode, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, RH_Screenwriter, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, H3SigmaRefiner, CFGGuider, ResolutionSelector, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, WujiCleaner, VHS_VideoCombine, Int, PrimitiveStringMultiline, WujiH3PromptEnhancer, easy promptConcat, ComfyMathExpression, MiniMaxH3AudioConditioningT8, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3 Semantic Bridge LCM高清图生视频文戏专用工作流，图生视频方案_2107901152405835778.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Semantic Bridge LCM高清图生视频文戏专用工作流，图生视频方案_2107901152405835778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
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

覆盖率 **91%**（60/66）

**有卡**：`VAELoader`、`RandomNoise`、`KSamplerSelect`、`CLIPLoader`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`UNETLoader`、`BasicScheduler`、`LoadImage`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CLIPTextEncode`、`ImageResizeKJv2`、`RH_Screenwriter`、`MiniMaxH3SemanticBridgeApplyT8`、`MiniMaxH3SemanticBridgeConfigT8`、`H3SigmaRefiner`、`CFGGuider`、`ResolutionSelector`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`WujiCleaner`、`VHS_VideoCombine`、`Int`、`WujiH3PromptEnhancer`、`easy promptConcat`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
