---
key: 视频生成/图生视频/Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）对镜自拍_2041411103518887938.json
name: Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）对镜自拍_2041411103518887938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041411103518887938.json
hash: ed521fba862956f5
coverage: 0.737705
learned_at: 2026-10-15 22:36:19
nodes: [Note, Note, ImageScaleBy, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), PainterI2V, KSamplerAdvanced, CLIPTextEncode, Note, Reroute, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageFromBatch+, RunningHub Deepcleaner, VHS_VideoCombine, MathExpression|pysssss, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, ShellAgentPluginOutputText, UNETLoader, UNETLoader, easy showAnything, easy cleanGpuUsed, easy anythingIndexSwitch, CR Prompt Text, VHS_VideoCombine, JWInteger, Note, Seed (rgthree), Note, Note, Note, VAEDecode, CR Text, LoadImage, CR Prompt Text, easy showAnything, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）对镜自拍_2041411103518887938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041411103518887938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `Note`
- `Note`
- `ImageScaleBy`
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
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Float`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageFromBatch+`
- `RunningHub Deepcleaner`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `ShellAgentPluginOutputText`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `easy cleanGpuUsed`
- `easy anythingIndexSwitch`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `Seed (rgthree)`
- `Note`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `CR Text`
- `LoadImage`
- `CR Prompt Text`
- `easy showAnything`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（45/61）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`PainterI2V`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`ImageFromBatch+`、`RunningHub Deepcleaner`、`VHS_VideoCombine`、`MathExpression|pysssss`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ShellAgentPluginOutputText`、`UNETLoader`、`easy anythingIndexSwitch`、`CR Prompt Text`、`JWInteger`、`Seed (rgthree)`、`VAEDecode`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
