---
key: 平台全量/CG神幻漫剧角色设计（CG Fantasy Character Design）_2030574519403945985.json
name: CG神幻漫剧角色设计（CG Fantasy Character Design）_2030574519403945985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/CG神幻漫剧角色设计（CG Fantasy Character Design）_2030574519403945985.json
hash: f7e3ae93ee9becc3
coverage: 0.941176
learned_at: 2026-11-14 00:21:35
nodes: [KSamplerSelect, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, CR SDXL Aspect Ratio, RandomNoise, SaveImage, CLIPTextEncode, LoraLoaderModelOnly, CFGGuider, CLIPLoader, VAELoader, PreviewImage, UNETLoader, Flux2Scheduler, CLIPTextEncode, CR Text]
patterns: []
missing: []
---

# 平台全量/CG神幻漫剧角色设计（CG Fantasy Character Design）_2030574519403945985.json

> 来源文件 `comfyui_library/workflows/平台全量/CG神幻漫剧角色设计（CG Fantasy Character Design）_2030574519403945985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CR SDXL Aspect Ratio`
- `RandomNoise`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `UNETLoader` ★核心
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `CR Text`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`KSamplerSelect`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`CR SDXL Aspect Ratio`、`RandomNoise`、`SaveImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CFGGuider`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`Flux2Scheduler`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、CFGGuider、KSamplerSelect
