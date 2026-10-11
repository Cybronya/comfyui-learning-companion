---
key: 视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json
name: MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json
hash: 80432fd5de6e22aa
coverage: 0.649123
learned_at: 2026-10-11 20:53:43
nodes: [Label (rgthree), BasicGuider, MarkdownNote, MarkdownNote, PrimitiveStringMultiline, MarkdownNote, KSamplerSelect, PrimitiveFloat, SamplerCustomAdvanced, RandomNoise, VAELoader, VAELoader, CLIPLoader, PrimitiveStringMultiline, ComfyMathExpression, BasicScheduler, ImageResizeKJv2, MiniMaxH3ReferenceToVideo, Reroute, VAEEncode, VAEEncodeAudio, BasicGuider, PT_H3ConcatAVLatent, RandomNoise, RunningHub Deepcleaner, Note, LoadAudio, VHS_LoadVideo, LoadAudio, VHS_LoadVideo, LoadAudio, VHS_LoadVideo, Fast Groups Bypasser (rgthree), KSamplerSelect, VAEDecode, VHS_VideoCombine, SamplerCustomAdvanced, CS-MultiImageLoader, ResolutionSelector, MiniMaxH3MemoryEfficientSageAttentionPatch, Reroute, Label (rgthree), Label (rgthree), MiniMaxH3AVDecodeT8, BasicScheduler, ResolutionSelector, Label (rgthree), Label (rgthree), DiffusionModelLoaderKJ, Fast Groups Bypasser (rgthree), UniBlockSwap, Fast Groups Bypasser (rgthree), MarkdownNote, LoraLoaderModelOnly, VHS_VideoCombine, SaveImage, LoadImage]
patterns: []
missing: [CS-MultiImageLoader, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), RunningHub Deepcleaner]
discoveries: [次要节点 `CS-MultiImageLoader` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax+H3+多参考生视频双采放大高清流+Multi_Ref+Video+Gen_2087401084498309122.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `Label (rgthree)`
- `BasicGuider`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `PrimitiveFloat`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `BasicScheduler`
- `ImageResizeKJv2`
- `MiniMaxH3ReferenceToVideo`
- `Reroute`
- `VAEEncode` ★核心
- `VAEEncodeAudio` ★核心
- `BasicGuider`
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `RunningHub Deepcleaner`
- `Note`
- `LoadAudio`
- `VHS_LoadVideo`
- `LoadAudio`
- `VHS_LoadVideo`
- `LoadAudio`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `CS-MultiImageLoader`
- `ResolutionSelector`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `Reroute`
- `Label (rgthree)`
- `Label (rgthree)`
- `MiniMaxH3AVDecodeT8`
- `BasicScheduler`
- `ResolutionSelector`
- `Label (rgthree)`
- `Label (rgthree)`
- `DiffusionModelLoaderKJ`
- `Fast Groups Bypasser (rgthree)`
- `UniBlockSwap`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **65%**（37/57）

**有卡**：`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`BasicScheduler`、`ImageResizeKJv2`、`MiniMaxH3ReferenceToVideo`、`VAEEncode`、`VAEEncodeAudio`、`PT_H3ConcatAVLatent`、`LoadAudio`、`VHS_LoadVideo`、`VAEDecode`、`VHS_VideoCombine`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AVDecodeT8`、`DiffusionModelLoaderKJ`、`UniBlockSwap`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`

**缺卡**（7）：`CS-MultiImageLoader`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`RunningHub Deepcleaner`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CS-MultiImageLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识
