---
key: 图片生成/图生图/【灵感工具】影视动画剧情分镜延展_FLUX.2.0-Klein9B_2031248180645470210.json
name: 【灵感工具】影视动画剧情分镜延展_FLUX.2.0-Klein9B_2031248180645470210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【灵感工具】影视动画剧情分镜延展_FLUX.2.0-Klein9B_2031248180645470210.json
hash: 1577c82179e087a8
coverage: 0.933333
learned_at: 2026-10-23 11:50:53
nodes: [Anything Everywhere3, CLIPLoader, VAELoader, UNETLoader, easy getNode, SaveImage, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPTextEncode, easy promptLine, VAEEncode, SamplerCustomAdvanced, CFGGuider, RandomNoise, KSamplerSelect, VAEDecode, easy setNode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, Text Multiline, JWStringConcat, Qwen3_VQA, INTConstant, INTConstant, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/图生图/【灵感工具】影视动画剧情分镜延展_FLUX.2.0-Klein9B_2031248180645470210.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【灵感工具】影视动画剧情分镜延展_FLUX.2.0-Klein9B_2031248180645470210.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `Anything Everywhere3`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `easy getNode`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `easy promptLine`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `Text Multiline`
- `JWStringConcat`
- `Qwen3_VQA`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`easy getNode`、`SaveImage`、`CLIPTextEncode`、`ReferenceLatent`、`easy promptLine`、`VAEEncode`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`VAEDecode`、`easy setNode`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Multiline`、`JWStringConcat`、`Qwen3_VQA`、`INTConstant`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
