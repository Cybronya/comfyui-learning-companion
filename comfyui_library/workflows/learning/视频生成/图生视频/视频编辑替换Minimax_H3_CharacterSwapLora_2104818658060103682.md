---
key: 视频生成/图生视频/视频编辑替换Minimax_H3_CharacterSwapLora_2104818658060103682.json
name: 视频编辑替换Minimax_H3_CharacterSwapLora_2104818658060103682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频编辑替换Minimax_H3_CharacterSwapLora_2104818658060103682.json
hash: 435afa3ebd12f7fe
coverage: 0.614035
learned_at: 2026-10-17 22:20:21
nodes: [GetNode, GetNode, GetNode, GetNode, SetNode, ConditioningZeroOut, Prompts Everywhere, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, H3SigmaRefiner, ModelPreviewOverrideKJ, LoraLoaderModelOnly, VAEDecodeAudio, BasicScheduler, MiniMaxH3ReferenceToVideo, VAEDecode, SelfLiftH3Sampler, UNETLoader, ModelAttentionBackend, Anything Everywhere3, VAELoader, VAELoader, SetNode, SetNode, CLIPLoader, SetNode, EasyCache, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, LoraLoaderModelOnly, ComfySwitchNode, LoraLoaderModelOnly, ResolutionSelector, GetNode, ComfyMathExpression, GetNode, VHS_VideoCombine, PrimitiveStringMultiline, LayerMask: RmBgUltra V2, EmptyImage, InvertMask, ImageCompositeMasked, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Note, DF_Integer, DF_Integer, SetNode, VHS_LoadVideo, ShowAnything|Mie, DF_Integer, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/视频编辑替换Minimax_H3_CharacterSwapLora_2104818658060103682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/视频编辑替换Minimax_H3_CharacterSwapLora_2104818658060103682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（57 个）：
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
- `Note`
- `DF_Integer`
- `DF_Integer`
- `SetNode`
- `VHS_LoadVideo`
- `ShowAnything|Mie`
- `DF_Integer`
- `Note`

## 知识

覆盖率 **61%**（35/57）

**有卡**：`ConditioningZeroOut`、`Prompts Everywhere`、`KSamplerSelect`、`H3SigmaRefiner`、`ModelPreviewOverrideKJ`、`LoraLoaderModelOnly`、`VAEDecodeAudio`、`BasicScheduler`、`MiniMaxH3ReferenceToVideo`、`VAEDecode`、`SelfLiftH3Sampler`、`UNETLoader`、`ModelAttentionBackend`、`VAELoader`、`CLIPLoader`、`EasyCache`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`ResolutionSelector`、`ComfyMathExpression`、`VHS_VideoCombine`、`LayerMask: RmBgUltra V2`、`EmptyImage`、`InvertMask`、`ImageCompositeMasked`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`DF_Integer`、`VHS_LoadVideo`、`ShowAnything|Mie`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
