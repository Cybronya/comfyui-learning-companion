---
key: 平台全量/老照片修复：FLUX.2-Klein+一致性LORA  更精准还原老照片的细节和神态！_2029956719916355586.json
name: 老照片修复：FLUX.2-Klein+一致性LORA  更精准还原老照片的细节和神态！_2029956719916355586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/老照片修复：FLUX.2-Klein+一致性LORA  更精准还原老照片的细节和神态！_2029956719916355586.json
hash: d7e09c4a9ff67532
coverage: 0.740741
learned_at: 2026-11-14 02:30:32
nodes: [EmptyFlux2LatentImage, Flux2Scheduler, ReferenceLatent, VAEEncode, VAELoader, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, SamplerCustomAdvanced, PlaySound|pysssss, Image Comparer (rgthree), RandomNoise, PrimitiveStringMultiline, PrimitiveStringMultiline, CFGGuider, CLIPTextEncode, CLIPLoader, ReferenceLatent, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, PrimitiveStringMultiline, LoadImage, SaveImage, VAEDecode, PreviewImage, ImpactSwitch, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 平台全量/老照片修复：FLUX.2-Klein+一致性LORA  更精准还原老照片的细节和神态！_2029956719916355586.json

> 来源文件 `comfyui_library/workflows/平台全量/老照片修复：FLUX.2-Klein+一致性LORA  更精准还原老照片的细节和神态！_2029956719916355586.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SamplerCustomAdvanced` ★核心
- `PlaySound|pysssss`
- `Image Comparer (rgthree)`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImpactSwitch`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`PlaySound|pysssss`、`RandomNoise`、`CFGGuider`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`SaveImage`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider
