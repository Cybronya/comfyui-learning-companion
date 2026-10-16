---
key: 视频生成/图生视频/minimax 1.0 8步加速1.0正式版_2088137884623785985.json
name: minimax 1.0 8步加速1.0正式版_2088137884623785985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax 1.0 8步加速1.0正式版_2088137884623785985.json
hash: 9591ca9089ad4389
coverage: 0.909091
learned_at: 2026-10-16 21:27:55
nodes: [VAEDecodeAudio, VAEDecode, KSamplerSelect, SamplerCustomAdvanced, BasicGuider, RandomNoise, VAELoader, VAELoader, UNETLoader, BasicScheduler, CreateVideo, SaveVideo, SolAttnPatch, CLIPLoader, LoraLoaderModelOnly, ResolutionSelector, ComfyMathExpression, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, 孤海注释, LoadImage, PrimitiveFloat, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax 1.0 8步加速1.0正式版_2088137884623785985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax 1.0 8步加速1.0正式版_2088137884623785985.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（33 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `BasicScheduler`
- `CreateVideo`
- `SaveVideo`
- `SolAttnPatch`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `孤海注释`
- `LoadImage`
- `PrimitiveFloat`
- `LoadAudio`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`VAELoader`、`UNETLoader`、`BasicScheduler`、`CreateVideo`、`SaveVideo`、`SolAttnPatch`、`CLIPLoader`、`LoraLoaderModelOnly`、`ResolutionSelector`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
