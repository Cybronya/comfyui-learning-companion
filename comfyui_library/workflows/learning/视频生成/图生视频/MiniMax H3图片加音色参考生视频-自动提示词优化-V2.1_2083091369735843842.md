---
key: 视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V2.1_2083091369735843842.json
name: MiniMax H3图片加音色参考生视频-自动提示词优化-V2.1_2083091369735843842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V2.1_2083091369735843842.json
hash: 24b9b845948b64eb
coverage: 0.588235
learned_at: 2026-10-16 01:17:12
nodes: [VAELoader, VAELoader, KSamplerSelect, RandomNoise, MarkdownNote, MarkdownNote, SamplerCustomAdvanced, ToString, GetNode, StringConcatenate, SetNode, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, llama_cpp_parameters, GetNode, UNETLoader, GetNode, SetNode, Any Switch (rgthree), CLIPLoader, UNETLoader, CLIPLoader, BatchImagesNode, MarkdownNote, PrimitiveFloat, ComfyMathExpression, SetNode, SetNode, easy showAnything, easy showAnything, ResolutionSelector, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, JoinStringMulti, StringConcatenate, MiniMaxH3ReferenceToVideo, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy showAnything, easy showAnything, LoadAudio, LoadAudio, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PurgeVRAM_UTK, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, BasicScheduler, BasicGuider, GetNode, llama_cpp_model_loader, llama_cpp_instruct_adv]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V2.1_2083091369735843842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V2.1_2083091369735843842.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（68 个）：
- `VAELoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `MarkdownNote`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `ToString`
- `GetNode`
- `StringConcatenate`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `llama_cpp_parameters`
- `GetNode`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `BatchImagesNode`
- `MarkdownNote`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `JoinStringMulti`
- `StringConcatenate`
- `MiniMaxH3ReferenceToVideo`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `easy showAnything`
- `LoadAudio`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `BasicScheduler`
- `BasicGuider`
- `GetNode`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`

## 知识

覆盖率 **59%**（40/68）

**有卡**：`VAELoader`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`ToString`、`StringConcatenate`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`llama_cpp_parameters`、`UNETLoader`、`CLIPLoader`、`BatchImagesNode`、`ComfyMathExpression`、`ResolutionSelector`、`JoinStringMulti`、`MiniMaxH3ReferenceToVideo`、`LoadAudio`、`LoadImage`、`PurgeVRAM_UTK`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`BasicGuider`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
