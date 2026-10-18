---
key: 视频生成/图生视频/Remix V3 + Qwen3.5多重对比I2V_2035642798367580161.json
name: Remix V3 + Qwen3.5多重对比I2V_2035642798367580161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Remix V3 + Qwen3.5多重对比I2V_2035642798367580161.json
hash: 821bdedcf468f72c
coverage: 0.752577
learned_at: 2026-10-15 22:35:49
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, KSamplerAdvanced, CLIPTextEncode, Note, Note, Seed (rgthree), Reroute, LayerUtility: PurgeVRAM, MathExpression|pysssss, Float, easy showAnything, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, PathchSageAttentionKJ, llama_cpp_model_loader, llama_cpp_parameters, ShellAgentPluginOutputText, easy showAnything, UNETLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, PainterI2V, KSamplerAdvanced, CLIPTextEncode, Reroute, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, ImageFromBatch+, ImageFromBatch+, easy cleanGpuUsed, easy cleanGpuUsed, AddLabel, llama_cpp_instruct_adv, CR Text, JWInteger, Note, easy cleanGpuUsed, ImageConcanate, RunningHub Deepcleaner, RunningHub Deepcleaner, AddLabel, ProcessString, JWInteger, VHS_VideoCombine, LoadImage, AddLabel]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Remix V3 + Qwen3.5多重对比I2V_2035642798367580161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035642798367580161.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
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
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Seed (rgthree)`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `Float`
- `easy showAnything`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageFromBatch+`
- `ImageFromBatch+`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `AddLabel`
- `llama_cpp_instruct_adv`
- `CR Text`
- `JWInteger`
- `Note`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `RunningHub Deepcleaner`
- `RunningHub Deepcleaner`
- `AddLabel`
- `ProcessString`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`
- `AddLabel`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（73/97）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`VAEDecode`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`PathchSageAttentionKJ`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ShellAgentPluginOutputText`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterI2V`、`ImageFromBatch+`、`AddLabel`、`llama_cpp_instruct_adv`、`CR Text`、`JWInteger`、`ImageConcanate`、`RunningHub Deepcleaner`、`ProcessString`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
