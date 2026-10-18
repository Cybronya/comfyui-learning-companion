---
key: 视频生成/图生视频/Wan2.2图生视频、自动生成视频脚本_2041400574976991233.json
name: Wan2.2图生视频、自动生成视频脚本_2041400574976991233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频、自动生成视频脚本_2041400574976991233.json
hash: 60ce90ae97fdfb5e
coverage: 0.789474
learned_at: 2026-10-15 22:36:19
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, CLIPTextEncode, Reroute, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageFromBatch+, RunningHub Deepcleaner, llama_cpp_model_loader, llama_cpp_parameters, ShellAgentPluginOutputText, easy cleanGpuUsed, llama_cpp_instruct_adv, UNETLoader, UNETLoader, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, JWInteger, JWInteger, CR Prompt Text, CR Text, CR Prompt Text, easy anythingIndexSwitch, Seed (rgthree), MathExpression|pysssss, Float, easy showAnything, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2图生视频、自动生成视频脚本_2041400574976991233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041400574976991233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
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
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ShellAgentPluginOutputText`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `CR Text`
- `CR Prompt Text`
- `easy anythingIndexSwitch`
- `Seed (rgthree)`
- `MathExpression|pysssss`
- `Float`
- `easy showAnything`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（45/57）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ShellAgentPluginOutputText`、`llama_cpp_instruct_adv`、`UNETLoader`、`VHS_VideoCombine`、`JWInteger`、`CR Prompt Text`、`CR Text`、`easy anythingIndexSwitch`、`Seed (rgthree)`、`MathExpression|pysssss`、`Float`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
