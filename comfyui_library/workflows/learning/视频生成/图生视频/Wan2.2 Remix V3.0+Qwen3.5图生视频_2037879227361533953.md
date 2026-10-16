---
key: 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5图生视频_2037879227361533953.json
name: Wan2.2 Remix V3.0+Qwen3.5图生视频_2037879227361533953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037879227361533953.json
hash: 55305286a48dcf41
coverage: 0.737705
learned_at: 2026-10-15 22:35:59
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, VHS_VideoCombine, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, CLIPTextEncode, Note, Note, Note, Note, Seed (rgthree), Reroute, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Float, JWInteger, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageFromBatch+, RunningHub Deepcleaner, JWInteger, VHS_VideoCombine, easy anythingIndexSwitch, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, ShellAgentPluginOutputText, CR Prompt Text, CR Text, easy showAnything, easy cleanGpuUsed, UNETLoader, UNETLoader, easy showAnything, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5图生视频_2037879227361533953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037879227361533953.json`

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
- `VHS_VideoCombine`
- `Pick From Batch (mtb)`
- `VAEDecode` ★核心
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Seed (rgthree)`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Float`
- `JWInteger`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `JWInteger`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `ShellAgentPluginOutputText`
- `CR Prompt Text`
- `CR Text`
- `easy showAnything`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
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

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`VHS_VideoCombine`、`Pick From Batch (mtb)`、`VAEDecode`、`PainterI2V`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`JWInteger`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`easy anythingIndexSwitch`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`ShellAgentPluginOutputText`、`CR Prompt Text`、`CR Text`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
