---
key: 视频生成/文生视频/（N sfw版）Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035617850320228353.json
name: （N sfw版）Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035617850320228353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（N sfw版）Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035617850320228353.json
hash: 05d9d8e5eecbb34d
coverage: 0.909091
learned_at: 2026-10-15 22:49:11
nodes: [EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, Seed (rgthree), llama_cpp_parameters, VAEDecode, LoraLoaderModelOnly, easy cleanGpuUsed, ShellAgentPluginOutputText, UNETLoader, CLIPTextEncode, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, JWInteger, PathchSageAttentionKJ, JWInteger, JWInteger, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, easy showAnything, easy showAnything, llama_cpp_instruct_adv, UNETLoader, UNETLoader, CR Text, Reroute, VHS_VideoCombine, ImageFromBatch+, DuckHideNode, SaveImage, TT_img_enc_v2, SaveImage, llama_cpp_model_loader, easy anythingIndexSwitch, Int, TT_img_enc, Note, SaveImage, CR Prompt Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/（N sfw版）Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035617850320228353.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（N sfw版）Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035617850320228353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `llama_cpp_parameters`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `ShellAgentPluginOutputText`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `PathchSageAttentionKJ`
- `JWInteger`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `Reroute`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `DuckHideNode`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `llama_cpp_model_loader`
- `easy anythingIndexSwitch`
- `Int`
- `TT_img_enc`
- `Note`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Seed (rgthree)`、`llama_cpp_parameters`、`VAEDecode`、`easy cleanGpuUsed`、`ShellAgentPluginOutputText`、`UNETLoader`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`JWInteger`、`ModelSamplingSD3`、`llama_cpp_instruct_adv`、`CR Text`、`VHS_VideoCombine`、`ImageFromBatch+`、`DuckHideNode`、`SaveImage`、`TT_img_enc_v2`、`llama_cpp_model_loader`、`easy anythingIndexSwitch`、`Int`、`TT_img_enc`、`CR Prompt Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader
