---
key: 平台全量/FLUX.2-Klein_老照片修复与画质超分多模式智能V2  _ 图像去噪 _ 细节重构 _ 旧照_2063114156718510082.json
name: FLUX.2-Klein_老照片修复与画质超分多模式智能V2  _ 图像去噪 _ 细节重构 _ 旧照_2063114156718510082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.2-Klein_老照片修复与画质超分多模式智能V2  _ 图像去噪 _ 细节重构 _ 旧照_2063114156718510082.json
hash: 3f25af83ea6e0ba7
coverage: 0.777778
learned_at: 2026-11-14 00:25:12
nodes: [VAELoader, CLIPLoader, LoadImage, EmptyFlux2LatentImage, Flux2Scheduler, ReferenceLatent, KSamplerSelect, VAEDecode, SamplerCustomAdvanced, PlaySound|pysssss, RandomNoise, CFGGuider, CLIPTextEncode, CLIPTextEncode, ReferenceLatent, UNETLoader, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Image Comparer (rgthree), LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, ImpactSwitch, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 平台全量/FLUX.2-Klein_老照片修复与画质超分多模式智能V2  _ 图像去噪 _ 细节重构 _ 旧照_2063114156718510082.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.2-Klein_老照片修复与画质超分多模式智能V2  _ 图像去噪 _ 细节重构 _ 旧照_2063114156718510082.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ReferenceLatent`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `PlaySound|pysssss`
- `RandomNoise`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ImpactSwitch`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **78%**（21/27）

**有卡**：`VAELoader`、`CLIPLoader`、`LoadImage`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ReferenceLatent`、`KSamplerSelect`、`VAEDecode`、`SamplerCustomAdvanced`、`PlaySound|pysssss`、`RandomNoise`、`CFGGuider`、`CLIPTextEncode`、`UNETLoader`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider
