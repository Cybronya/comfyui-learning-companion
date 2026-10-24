---
key: 图片生成/图生图/Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457.json
name: Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457.json
hash: 59d49f0801b9f9c3
coverage: 0.909091
learned_at: 2026-10-23 10:58:46
nodes: [ConditioningZeroOut, ReferenceLatent, ReferenceLatent, KSamplerSelect, Flux2Scheduler, CLIPLoader, VAELoader, CFGGuider, IdentityFeatureTransferV3, RandomNoise, SamplerCustomAdvanced, MarkdownNote, PrimitiveString, ImageResize+, LoadImage, easy globalSeed, EmptyFlux2LatentImage, VAEEncode, VAEDecode, SaveImage, UNETLoader, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `IdentityFeatureTransferV3`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `PrimitiveString`
- `ImageResize+`
- `LoadImage`
- `easy globalSeed`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **91%**（20/22）

**有卡**：`ConditioningZeroOut`、`ReferenceLatent`、`KSamplerSelect`、`Flux2Scheduler`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`IdentityFeatureTransferV3`、`RandomNoise`、`SamplerCustomAdvanced`、`ImageResize+`、`LoadImage`、`easy globalSeed`、`EmptyFlux2LatentImage`、`VAEEncode`、`VAEDecode`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
