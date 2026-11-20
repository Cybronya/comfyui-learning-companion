---
key: 平台全量/电影海报生成器Movie Genre Switcher Parody Poster_1838534026260017153.json
name: 电影海报生成器Movie Genre Switcher Parody Poster_1838534026260017153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/电影海报生成器Movie Genre Switcher Parody Poster_1838534026260017153.json
hash: 6c7574ee6cae4484
coverage: 0.913043
learned_at: 2026-11-14 02:25:36
nodes: [BasicGuider, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, VAELoader, LoraTagLoader, BasicScheduler, ModelSamplingFlux, Int, Int, EmptyLatentImage, CLIPTextEncode, VAEDecode, SaveImage, CheckpointLoaderSimple, DualCLIPLoader, ConcatStringSingle, ImpactWildcardProcessor, ImpactWildcardProcessor, RH_Prompter, ShowText|pysssss, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "flux1-dev-fp8.safetensors", "height": 1920, "width": 1080}
---

# 平台全量/电影海报生成器Movie Genre Switcher Parody Poster_1838534026260017153.json

> 来源文件 `comfyui_library/workflows/平台全量/电影海报生成器Movie Genre Switcher Parody Poster_1838534026260017153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `BasicGuider`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `LoraTagLoader`
- `BasicScheduler`
- `ModelSamplingFlux`
- `Int`
- `Int`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `DualCLIPLoader`
- `ConcatStringSingle`
- `ImpactWildcardProcessor`
- `ImpactWildcardProcessor`
- `RH_Prompter`
- `ShowText|pysssss`
- `PreviewImage`

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `checkpoint` = `flux1-dev-fp8.safetensors`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`BasicGuider`、`FluxGuidance`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`VAELoader`、`LoraTagLoader`、`BasicScheduler`、`ModelSamplingFlux`、`Int`、`EmptyLatentImage`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`DualCLIPLoader`、`ConcatStringSingle`、`ImpactWildcardProcessor`、`RH_Prompter`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
