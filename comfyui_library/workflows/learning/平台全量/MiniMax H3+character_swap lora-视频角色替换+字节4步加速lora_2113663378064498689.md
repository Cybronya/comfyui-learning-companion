---
key: 平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2113663378064498689.json
name: MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2113663378064498689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2113663378064498689.json
hash: e9bfac28ed9bafb8
coverage: 0.46
learned_at: 2026-11-14 00:41:37
nodes: [UNETLoader, MiniMaxH3SigmaShift, SetNode, GetNode, GetNode, GetNode, GetImageSize, GetNode, CFGGuider, GetNode, BasicScheduler, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, GetNode, VAEDecode, MiniMaxH3AddGuide, LoraLoaderModelOnly, GetNode, SetNode, SetNode, ComfyMathExpression, GetNode, MarkdownNote, SetNode, LoraLoaderModelOnly, SetNode, CLIPLoader, SetNode, VAELoader, ResolutionSelector, SetNode, SetNode, GetNode, MiniMaxH3ReferenceToVideo, Text, SamplerCustomAdvanced, 孤海注释, SetNode, GetNode, GetNode, ImageResizeKJv2, 孤海注释, MarkdownNote, MarkdownNote, PrimitiveFloat, LoadImage, VHS_LoadVideo, VHS_VideoCombine, 孤海注释]
patterns: []
missing: []
---

# 平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2113663378064498689.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2113663378064498689.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `MiniMaxH3AddGuide`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `MarkdownNote`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `Text`
- `SamplerCustomAdvanced` ★核心
- `孤海注释`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `孤海注释`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveFloat`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `孤海注释`

## 知识

覆盖率 **46%**（23/50）

**有卡**：`UNETLoader`、`MiniMaxH3SigmaShift`、`GetImageSize`、`CFGGuider`、`BasicScheduler`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecode`、`MiniMaxH3AddGuide`、`LoraLoaderModelOnly`、`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`Text`、`SamplerCustomAdvanced`、`ImageResizeKJv2`、`LoadImage`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、CFGGuider
