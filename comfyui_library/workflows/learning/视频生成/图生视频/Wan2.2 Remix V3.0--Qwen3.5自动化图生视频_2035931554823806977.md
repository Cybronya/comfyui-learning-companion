---
key: 视频生成/图生视频/Wan2.2 Remix V3.0--Qwen3.5自动化图生视频_2035931554823806977.json
name: Wan2.2 Remix V3.0--Qwen3.5自动化图生视频_2035931554823806977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2035931554823806977.json
hash: 38ce3db3e522ec45
coverage: 0.878049
learned_at: 2026-10-15 22:35:50
nodes: [Note, llama_cpp_parameters, llama_cpp_instruct_adv, ShellAgentPluginOutputText, easy cleanGpuUsed, LoadImage, CR Prompt Text, Note, JWInteger, JWInteger, Note, easy showAnything, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, llama_cpp_model_loader, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPLoader, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPVisionLoader, CLIPVisionEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJv2, ImageFromBatch+, LayerUtility: PurgeVRAM, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, RunningHub Deepcleaner, easy showAnything, easy anythingIndexSwitch, CR Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Remix V3.0--Qwen3.5自动化图生视频_2035931554823806977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035931554823806977.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
- `Note`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `ShellAgentPluginOutputText`
- `easy cleanGpuUsed`
- `LoadImage`
- `CR Prompt Text`
- `Note`
- `JWInteger`
- `JWInteger`
- `Note`
- `easy showAnything`
- `Float`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `llama_cpp_model_loader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `RunningHub Deepcleaner`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`ShellAgentPluginOutputText`、`easy cleanGpuUsed`、`LoadImage`、`CR Prompt Text`、`JWInteger`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`llama_cpp_model_loader`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`ImageResizeKJv2`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`VHS_VideoCombine`、`MathExpression|pysssss`、`RunningHub Deepcleaner`、`easy anythingIndexSwitch`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
