---
key: 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2062141489110667266.json
name: Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2062141489110667266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062141489110667266.json
hash: 003c6ab4dc7d2570
coverage: 0.741935
learned_at: 2026-10-15 22:39:01
nodes: [Note, Note, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, CLIPLoader, Note, KSamplerAdvanced, CLIPTextEncode, PreviewImage, Pick From Batch (mtb), PainterI2V, CLIPTextEncode, Note, Note, Note, Note, Seed (rgthree), LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, RunningHub Deepcleaner, VHS_VideoCombine, ShellAgentPluginOutputText, CR Prompt Text, easy showAnything, easy cleanGpuUsed, easy showAnything, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, easy anythingIndexSwitch, CR Text, UNETLoader, LoadImage, CR Prompt Text, JWInteger, UNETLoader, LoraLoaderModelOnly, Note, JWInteger, easy cleanGpuUsed, Reroute, KSamplerAdvanced, ImageScaleBy, ImageFromBatch+, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2062141489110667266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062141489110667266.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `Note`
- `Note`
- `Note`
- `ImageResizeKJv2`
- `SaveImage`
- `ColorMatch`
- `ImageScaleBy`
- `CLIPVisionEncode`
- `Note`
- `CLIPVisionLoader`
- `VAELoader`
- `Note`
- `Note`
- `CLIPLoader`
- `Note`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Pick From Batch (mtb)`
- `PainterI2V`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Seed (rgthree)`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Float`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `RunningHub Deepcleaner`
- `VHS_VideoCombine`
- `ShellAgentPluginOutputText`
- `CR Prompt Text`
- `easy showAnything`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `easy anythingIndexSwitch`
- `CR Text`
- `UNETLoader` ★核心
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `JWInteger`
- `easy cleanGpuUsed`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `ImageScaleBy`
- `ImageFromBatch+`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
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

**有卡**：`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`ImageScaleBy`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`PainterI2V`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`RunningHub Deepcleaner`、`VHS_VideoCombine`、`ShellAgentPluginOutputText`、`CR Prompt Text`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`easy anythingIndexSwitch`、`CR Text`、`UNETLoader`、`LoadImage`、`JWInteger`、`LoraLoaderModelOnly`、`ImageFromBatch+`、`VAEDecode`、`ModelSamplingSD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader
