---
key: 视频生成/图生视频/（N SFW）Dasiwa V10+Qwen3.5图生视频自动提示词工作流V1_2041143697240231938.json
name: （N SFW）Dasiwa V10+Qwen3.5图生视频自动提示词工作流V1_2041143697240231938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041143697240231938.json
hash: d20ed28c2ea0aa85
coverage: 0.764706
learned_at: 2026-10-15 22:36:18
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, KSamplerAdvanced, PathchSageAttentionKJ, CLIPTextEncode, UNETLoader, Note, Note, Note, Reroute, ImageFromBatch+, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, VHS_VideoCombine, SaveImage, SaveImage, RunningHub Deepcleaner, llama_cpp_model_loader, llama_cpp_parameters, ShellAgentPluginOutputText, llama_cpp_instruct_adv, easy showAnything, easy cleanGpuUsed, Seed (rgthree), easy showAnything, PathchSageAttentionKJ, UNETLoader, UNETLoader, CR Text, CR Prompt Text, easy anythingIndexSwitch, DuckHideNode, TT_img_enc_v2, TT_img_enc, Note, JWInteger, JWInteger, LoadImage, CR Prompt Text, SaveImage, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/（N SFW）Dasiwa V10+Qwen3.5图生视频自动提示词工作流V1_2041143697240231938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041143697240231938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
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
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Note`
- `Note`
- `Note`
- `Reroute`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Float`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `VHS_VideoCombine`
- `SaveImage`
- `SaveImage`
- `RunningHub Deepcleaner`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ShellAgentPluginOutputText`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `easy cleanGpuUsed`
- `Seed (rgthree)`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `CR Prompt Text`
- `easy anythingIndexSwitch`
- `DuckHideNode`
- `TT_img_enc_v2`
- `TT_img_enc`
- `Note`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `CR Prompt Text`
- `SaveImage`
- `CR Prompt Text`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（52/68）

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`VAEDecode`、`PathchSageAttentionKJ`、`UNETLoader`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`VHS_VideoCombine`、`RunningHub Deepcleaner`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ShellAgentPluginOutputText`、`llama_cpp_instruct_adv`、`Seed (rgthree)`、`CR Text`、`CR Prompt Text`、`easy anythingIndexSwitch`、`DuckHideNode`、`TT_img_enc_v2`、`TT_img_enc`、`JWInteger`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
