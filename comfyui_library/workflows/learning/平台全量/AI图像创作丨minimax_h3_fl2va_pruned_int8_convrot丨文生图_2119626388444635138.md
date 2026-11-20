---
key: 平台全量/AI图像创作丨minimax_h3_fl2va_pruned_int8_convrot丨文生图_2119626388444635138.json
name: AI图像创作丨minimax_h3_fl2va_pruned_int8_convrot丨文生图_2119626388444635138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/AI图像创作丨minimax_h3_fl2va_pruned_int8_convrot丨文生图_2119626388444635138.json
hash: 6fd7a1e65abe2e9f
coverage: 0.875
learned_at: 2026-11-14 00:15:56
nodes: [SaveImage, MarkdownNote, ResolutionSelector, UNETLoader, CLIPLoader, LoraLoaderModelOnly, PrimitiveStringMultiline, VAELoader, MiniMaxH3SigmaShift, BasicGuider, KSamplerSelect, RandomNoise, ManualSigmas, SamplerCustomAdvanced, VAEDecode, PH3ImageConditioning]
patterns: []
missing: []
---

# 平台全量/AI图像创作丨minimax_h3_fl2va_pruned_int8_convrot丨文生图_2119626388444635138.json

> 来源文件 `comfyui_library/workflows/平台全量/AI图像创作丨minimax_h3_fl2va_pruned_int8_convrot丨文生图_2119626388444635138.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `SaveImage`
- `MarkdownNote`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `VAELoader`
- `MiniMaxH3SigmaShift`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PH3ImageConditioning`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`SaveImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`MiniMaxH3SigmaShift`、`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`PH3ImageConditioning`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
