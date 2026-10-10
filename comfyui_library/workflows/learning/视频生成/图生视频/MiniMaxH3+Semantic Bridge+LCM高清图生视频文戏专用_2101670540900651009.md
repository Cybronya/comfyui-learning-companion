---
key: 视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM高清图生视频文戏专用_2101670540900651009.json
name: MiniMaxH3+Semantic Bridge+LCM高清图生视频文戏专用_2101670540900651009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM高清图生视频文戏专用_2101670540900651009.json
hash: 8361af4d47602121
coverage: 0.916667
learned_at: 2026-10-10 22:53:28
nodes: [VAELoader, VAELoader, RandomNoise, KSamplerSelect, CLIPLoader, MiniMaxH3SigmaShift, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, BasicScheduler, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, CLIPTextEncode, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, RH_Screenwriter, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, H3SigmaRefiner, CFGGuider, ResolutionSelector, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, WujiCleaner, VHS_VideoCombine, Int, PrimitiveStringMultiline, WujiH3PromptEnhancer, easy promptConcat, ComfyMathExpression, MiniMaxH3AudioConditioningT8]
patterns: []
missing: [easy promptConcat]
discoveries: [次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM高清图生视频文戏专用_2101670540900651009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM高清图生视频文戏专用_2101670540900651009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（36 个）：
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

## 知识

覆盖率 **92%**（33/36）

**有卡**：`VAELoader`、`RandomNoise`、`KSamplerSelect`、`CLIPLoader`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`UNETLoader`、`BasicScheduler`、`LoadImage`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CLIPTextEncode`、`ImageResizeKJv2`、`RH_Screenwriter`、`MiniMaxH3SemanticBridgeApplyT8`、`MiniMaxH3SemanticBridgeConfigT8`、`H3SigmaRefiner`、`CFGGuider`、`ResolutionSelector`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`WujiCleaner`、`VHS_VideoCombine`、`Int`、`WujiH3PromptEnhancer`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`

**缺卡**（1）：`easy promptConcat`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader

## 学习发现

- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
