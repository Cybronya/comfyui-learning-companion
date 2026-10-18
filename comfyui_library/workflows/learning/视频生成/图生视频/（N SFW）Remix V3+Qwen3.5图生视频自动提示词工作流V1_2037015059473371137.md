---
key: 视频生成/图生视频/（N SFW）Remix V3+Qwen3.5图生视频自动提示词工作流V1_2037015059473371137.json
name: （N SFW）Remix V3+Qwen3.5图生视频自动提示词工作流V1_2037015059473371137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（N SFW）Remix V3+Qwen3.5图生视频自动提示词工作流V1_2037015059473371137.json
hash: f5f4af0e3910bf79
coverage: 0.764706
learned_at: 2026-10-15 22:35:54
nodes: [Note, Note, ImageScaleBy, Note, ImageResizeKJv2, SaveImage, ColorMatch, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, Note, CLIPVisionLoader, VAELoader, Note, Note, Note, CLIPLoader, Note, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, PreviewImage, ModelSamplingSD3, Pick From Batch (mtb), VAEDecode, KSamplerAdvanced, PathchSageAttentionKJ, CLIPTextEncode, UNETLoader, Note, Note, easy anythingIndexSwitch, Note, Reroute, ImageFromBatch+, LayerUtility: PurgeVRAM, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, VHS_VideoCombine, SaveImage, SaveImage, RunningHub Deepcleaner, llama_cpp_model_loader, llama_cpp_parameters, CR Text, ShellAgentPluginOutputText, easy showAnything, easy cleanGpuUsed, CR Prompt Text, Seed (rgthree), easy showAnything, UNETLoader, UNETLoader, PathchSageAttentionKJ, JWInteger, Note, LoadImage, JWInteger, DuckHideNode, TT_img_enc_v2, llama_cpp_instruct_adv, SaveImage, TT_img_enc, CR Prompt Text, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/（N SFW）Remix V3+Qwen3.5图生视频自动提示词工作流V1_2037015059473371137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037015059473371137.json`

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
- `easy anythingIndexSwitch`
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
- `CR Text`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `easy cleanGpuUsed`
- `CR Prompt Text`
- `Seed (rgthree)`
- `easy showAnything`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `JWInteger`
- `Note`
- `LoadImage`
- `JWInteger`
- `DuckHideNode`
- `TT_img_enc_v2`
- `llama_cpp_instruct_adv`
- `SaveImage`
- `TT_img_enc`
- `CR Prompt Text`
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

**有卡**：`ImageScaleBy`、`ImageResizeKJv2`、`SaveImage`、`ColorMatch`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Pick From Batch (mtb)`、`VAEDecode`、`PathchSageAttentionKJ`、`UNETLoader`、`easy anythingIndexSwitch`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`VHS_VideoCombine`、`RunningHub Deepcleaner`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CR Text`、`ShellAgentPluginOutputText`、`CR Prompt Text`、`Seed (rgthree)`、`JWInteger`、`LoadImage`、`DuckHideNode`、`TT_img_enc_v2`、`llama_cpp_instruct_adv`、`TT_img_enc`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
