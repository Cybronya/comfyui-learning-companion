---
key: 平台全量/Flux.2 Klein 4B 瞬间擦除水印+批量处理_2032703743040425985.json
name: Flux.2 Klein 4B 瞬间擦除水印+批量处理_2032703743040425985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 Klein 4B 瞬间擦除水印+批量处理_2032703743040425985.json
hash: 5fec011b24cae5b7
coverage: 0.849057
learned_at: 2026-11-14 00:28:51
nodes: [KSamplerSelect, CFGGuider, EmptyFlux2LatentImage, Flux2Scheduler, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, ReferenceLatent, VAELoader, ConditioningZeroOut, DifferentialDiffusion, Reroute, UNETLoader, CLIPLoader, RandomNoise, VAEDecode, CLIPTextEncode, easy imageCount, easy forLoopEnd, Bjornulf_ShowInt, easy showAnything, KSamplerSelect, CFGGuider, EmptyFlux2LatentImage, Flux2Scheduler, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, ReferenceLatent, VAELoader, ConditioningZeroOut, DifferentialDiffusion, Reroute, UNETLoader, CLIPLoader, RandomNoise, CLIPTextEncode, easy forLoopStart, RHExtractImage, SaveImage, Reroute, VAEDecode, Reroute, RHUploadZip, RHBatchImages:, PreviewImage, RHExtractImage, PreviewImage, kkGetImage, SaveImage, LoadImage, kkGetImage, Note]
patterns: []
missing: []
---

# 平台全量/Flux.2 Klein 4B 瞬间擦除水印+批量处理_2032703743040425985.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 Klein 4B 瞬间擦除水印+批量处理_2032703743040425985.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `Reroute`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `easy imageCount`
- `easy forLoopEnd`
- `Bjornulf_ShowInt`
- `easy showAnything`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `Reroute`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `RHExtractImage`
- `SaveImage`
- `Reroute`
- `VAEDecode` ★核心
- `Reroute`
- `RHUploadZip`
- `RHBatchImages:`
- `PreviewImage`
- `RHExtractImage`
- `PreviewImage`
- `kkGetImage`
- `SaveImage`
- `LoadImage`
- `kkGetImage`
- `Note`

## 知识

覆盖率 **85%**（45/53）

**有卡**：`KSamplerSelect`、`CFGGuider`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`VAEEncode`、`ReferenceLatent`、`VAELoader`、`ConditioningZeroOut`、`DifferentialDiffusion`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`VAEDecode`、`CLIPTextEncode`、`easy imageCount`、`easy forLoopEnd`、`Bjornulf_ShowInt`、`easy forLoopStart`、`RHExtractImage`、`SaveImage`、`RHUploadZip`、`RHBatchImages:`、`kkGetImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider
