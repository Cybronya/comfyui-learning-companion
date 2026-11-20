---
key: 平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2114924144327479298.json
name: MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2114924144327479298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2114924144327479298.json
hash: 6e42cadc30331480
coverage: 0.5
learned_at: 2026-11-14 00:41:38
nodes: [UNETLoader, MiniMaxH3SigmaShift, SetNode, GetNode, GetNode, GetNode, GetImageSize, GetNode, CFGGuider, GetNode, BasicScheduler, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, GetNode, VAEDecode, MiniMaxH3AddGuide, MarkdownNote, MarkdownNote, MarkdownNote, 孤海注释, 孤海注释, LoraLoaderModelOnly, GetNode, SetNode, SetNode, ComfyMathExpression, GetNode, MarkdownNote, MarkdownNote, SetNode, LoraLoaderModelOnly, SetNode, CLIPLoader, SetNode, VAELoader, VHS_LoadVideo, ResolutionSelector, SetNode, PrimitiveFloat, SetNode, GetNode, MiniMaxH3ReferenceToVideo, Text, SamplerCustomAdvanced, VHS_VideoCombine, 孤海注释, SetNode, LoadImage, GetNode, GetNode, ImageResizeKJv2, AnyBooleanSwitch, CR Font File List, ImpactConditionalBranch, LoadFolderFromDir, VHS_SelectFilename, CompressImages]
patterns: []
missing: []
---

# 平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2114924144327479298.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2114924144327479298.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（58 个）：
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
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `VHS_LoadVideo`
- `ResolutionSelector`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `Text`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `孤海注释`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `AnyBooleanSwitch`
- `CR Font File List`
- `ImpactConditionalBranch`
- `LoadFolderFromDir`
- `VHS_SelectFilename`
- `CompressImages`

## 知识

覆盖率 **50%**（29/58）

**有卡**：`UNETLoader`、`MiniMaxH3SigmaShift`、`GetImageSize`、`CFGGuider`、`BasicScheduler`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecode`、`MiniMaxH3AddGuide`、`LoraLoaderModelOnly`、`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`VHS_LoadVideo`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`Text`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`AnyBooleanSwitch`、`CR Font File List`、`ImpactConditionalBranch`、`LoadFolderFromDir`、`VHS_SelectFilename`、`CompressImages`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、CFGGuider
