---
key: 视频生成/图生视频/Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2041144753068183554.json
name: Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2041144753068183554.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2041144753068183554.json
hash: 667e4c703d3c7d0a
coverage: 0.737705
learned_at: 2026-10-15 22:36:18
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, CLIPTextEncode, Note, Note, Seed (rgthree), Reroute, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageFromBatch+, RunningHub Deepcleaner, llama_cpp_model_loader, llama_cpp_parameters, ShellAgentPluginOutputText, CR Prompt Text, CR Text, easy showAnything, easy cleanGpuUsed, llama_cpp_instruct_adv, UNETLoader, UNETLoader, easy showAnything, MathExpression|pysssss, easy anythingIndexSwitch, VHS_VideoCombine, VHS_VideoCombine, JWInteger, Note, Note, JWInteger, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2041144753068183554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041144753068183554.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
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
- `Pick From Batch (mtb)`
- `VAEDecode` ★核心
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Seed (rgthree)`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Float`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ShellAgentPluginOutputText`
- `CR Prompt Text`
- `CR Text`
- `easy showAnything`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `MathExpression|pysssss`
- `easy anythingIndexSwitch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `Note`
- `JWInteger`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（45/61）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ShellAgentPluginOutputText`、`CR Prompt Text`、`CR Text`、`llama_cpp_instruct_adv`、`UNETLoader`、`MathExpression|pysssss`、`easy anythingIndexSwitch`、`VHS_VideoCombine`、`JWInteger`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
