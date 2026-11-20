---
key: 平台全量/星绘-自动COS修图（Automatic COS photo editing）_2022573412341784578.json
name: 星绘-自动COS修图（Automatic COS photo editing）_2022573412341784578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/星绘-自动COS修图（Automatic COS photo editing）_2022573412341784578.json
hash: 0db31417f62183ec
coverage: 0.956522
learned_at: 2026-11-14 02:13:19
nodes: [KSamplerSelect, CFGGuider, CLIPLoader, GrowMaskWithBlur, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, ConditioningZeroOut, Flux2Scheduler, VAEDecode, SaveImage, VAELoader, VAEEncode, ReferenceLatent, ReferenceLatent, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, DifferentialDiffusion, CLIPTextEncode, LoadImage, CR Text]
patterns: []
missing: []
---

# 平台全量/星绘-自动COS修图（Automatic COS photo editing）_2022573412341784578.json

> 来源文件 `comfyui_library/workflows/平台全量/星绘-自动COS修图（Automatic COS photo editing）_2022573412341784578.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPLoader`
- `GrowMaskWithBlur`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DifferentialDiffusion`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`KSamplerSelect`、`CFGGuider`、`CLIPLoader`、`GrowMaskWithBlur`、`EmptyFlux2LatentImage`、`RandomNoise`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`Flux2Scheduler`、`VAEDecode`、`SaveImage`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoraLoaderModelOnly`、`DifferentialDiffusion`、`CLIPTextEncode`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
