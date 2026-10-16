---
key: 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2036976880821215234.json
name: Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2036976880821215234.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036976880821215234.json
hash: 8f9d82d93aca259a
coverage: 0.741935
learned_at: 2026-10-15 22:35:53
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, VHS_VideoCombine, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, CLIPTextEncode, Note, Seed (rgthree), Reroute, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageFromBatch+, RunningHub Deepcleaner, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, ShellAgentPluginOutputText, easy showAnything, easy cleanGpuUsed, UNETLoader, UNETLoader, easy showAnything, JWInteger, Float, CR Prompt Text, CR Text, Int, JWInteger, easy anythingIndexSwitch, Note, CR Prompt Text, LoadImage, Note, Note, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2036976880821215234.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036976880821215234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `Note`
- `Note`
- `ImageScaleBy`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `Note`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `Pick From Batch (mtb)`
- `VAEDecode` ★核心
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Seed (rgthree)`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `JWInteger`
- `Float`
- `CR Prompt Text`
- `CR Text`
- `Int`
- `JWInteger`
- `easy anythingIndexSwitch`
- `Note`
- `CR Prompt Text`
- `LoadImage`
- `Note`
- `Note`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（46/62）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`VHS_VideoCombine`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`ShellAgentPluginOutputText`、`UNETLoader`、`JWInteger`、`Float`、`CR Prompt Text`、`CR Text`、`Int`、`easy anythingIndexSwitch`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
