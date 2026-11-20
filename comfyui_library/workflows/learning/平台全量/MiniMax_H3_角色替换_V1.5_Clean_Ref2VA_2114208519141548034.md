---
key: 平台全量/MiniMax_H3_角色替换_V1.5_Clean_Ref2VA_2114208519141548034.json
name: MiniMax_H3_角色替换_V1.5_Clean_Ref2VA_2114208519141548034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax_H3_角色替换_V1.5_Clean_Ref2VA_2114208519141548034.json
hash: 9724145a943d7483
coverage: 0.952381
learned_at: 2026-11-14 00:45:06
nodes: [MiniMaxH3ReferenceToVideo, ComfyMathExpression, MiniMaxH3SigmaShift, BasicGuider, SamplerCustomAdvanced, VAEDecode, VHS_VideoCombine, LoadImage, VHS_LoadVideo, ResolutionSelector, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, KSamplerSelect, RandomNoise, LoraLoaderModelOnly, VAELoader, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 平台全量/MiniMax_H3_角色替换_V1.5_Clean_Ref2VA_2114208519141548034.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax_H3_角色替换_V1.5_Clean_Ref2VA_2114208519141548034.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（21 个）：
- `MiniMaxH3ReferenceToVideo`
- `ComfyMathExpression`
- `MiniMaxH3SigmaShift`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `ResolutionSelector`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`MiniMaxH3ReferenceToVideo`、`ComfyMathExpression`、`MiniMaxH3SigmaShift`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`KSamplerSelect`、`RandomNoise`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
