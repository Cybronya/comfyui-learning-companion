---
key: 图片生成/图生图/F.2Klein9b产品渲染精修_2058016361133207554.json
name: F.2Klein9b产品渲染精修_2058016361133207554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein9b产品渲染精修_2058016361133207554.json
hash: e283a948490eec0e
coverage: 0.869565
learned_at: 2026-10-23 10:52:42
nodes: [EmptyFlux2LatentImage, GetImageSize, ConditioningZeroOut, ReferenceLatent, RandomNoise, VAEDecode, KSamplerSelect, SamplerCustomAdvanced, ReferenceLatent, VAELoader, CFGGuider, VAEEncode, Flux2Scheduler, ConstrainImage|pysssss, Image Comparer (rgthree), Fast Groups Muter (rgthree), Note, UNETLoader, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/F.2Klein9b产品渲染精修_2058016361133207554.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein9b产品渲染精修_2058016361133207554.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `RandomNoise`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `VAELoader`
- `CFGGuider`
- `VAEEncode` ★核心
- `Flux2Scheduler`
- `ConstrainImage|pysssss`
- `Image Comparer (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`EmptyFlux2LatentImage`、`GetImageSize`、`ConditioningZeroOut`、`ReferenceLatent`、`RandomNoise`、`VAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAELoader`、`CFGGuider`、`VAEEncode`、`Flux2Scheduler`、`ConstrainImage|pysssss`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
