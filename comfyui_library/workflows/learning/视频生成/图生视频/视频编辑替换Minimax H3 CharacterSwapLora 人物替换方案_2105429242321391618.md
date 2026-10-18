---
key: 视频生成/图生视频/视频编辑替换Minimax H3 CharacterSwapLora 人物替换方案_2105429242321391618.json
name: 视频编辑替换Minimax H3 CharacterSwapLora 人物替换方案_2105429242321391618
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频编辑替换Minimax H3 CharacterSwapLora 人物替换方案_2105429242321391618.json
hash: 9698278166556a35
coverage: 0.717647
learned_at: 2026-10-17 22:20:20
nodes: [GetNode, GetNode, GetNode, GetNode, SetNode, ConditioningZeroOut, Prompts Everywhere, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, H3SigmaRefiner, ModelPreviewOverrideKJ, LoraLoaderModelOnly, VAEDecodeAudio, BasicScheduler, MiniMaxH3ReferenceToVideo, VAEDecode, SelfLiftH3Sampler, UNETLoader, ModelAttentionBackend, Anything Everywhere3, VAELoader, VAELoader, SetNode, SetNode, CLIPLoader, SetNode, EasyCache, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, LoraLoaderModelOnly, ComfySwitchNode, LoraLoaderModelOnly, ResolutionSelector, GetNode, ComfyMathExpression, GetNode, VHS_VideoCombine, PrimitiveStringMultiline, LayerMask: RmBgUltra V2, EmptyImage, InvertMask, ImageCompositeMasked, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, DF_Integer, DF_Integer, SetNode, VHS_LoadVideo, ShowAnything|Mie, DF_Integer, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/视频编辑替换Minimax H3 CharacterSwapLora 人物替换方案_2105429242321391618.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/视频编辑替换Minimax H3 CharacterSwapLora 人物替换方案_2105429242321391618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ConditioningZeroOut`
- `Prompts Everywhere`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `H3SigmaRefiner`
- `ModelPreviewOverrideKJ`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeAudio` ★核心
- `BasicScheduler`
- `MiniMaxH3ReferenceToVideo`
- `VAEDecode` ★核心
- `SelfLiftH3Sampler` ★核心
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `Anything Everywhere3`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `EasyCache`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LayerMask: RmBgUltra V2`
- `EmptyImage`
- `InvertMask`
- `ImageCompositeMasked`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DF_Integer`
- `DF_Integer`
- `SetNode`
- `VHS_LoadVideo`
- `ShowAnything|Mie`
- `DF_Integer`
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

覆盖率 **72%**（61/85）

**有卡**：`ConditioningZeroOut`、`Prompts Everywhere`、`KSamplerSelect`、`H3SigmaRefiner`、`ModelPreviewOverrideKJ`、`LoraLoaderModelOnly`、`VAEDecodeAudio`、`BasicScheduler`、`MiniMaxH3ReferenceToVideo`、`VAEDecode`、`SelfLiftH3Sampler`、`UNETLoader`、`ModelAttentionBackend`、`VAELoader`、`CLIPLoader`、`EasyCache`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`ResolutionSelector`、`ComfyMathExpression`、`VHS_VideoCombine`、`LayerMask: RmBgUltra V2`、`EmptyImage`、`InvertMask`、`ImageCompositeMasked`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`DF_Integer`、`VHS_LoadVideo`、`ShowAnything|Mie`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
