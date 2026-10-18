---
key: 视频生成/图生视频/Wan2.2 Smooth V3--Qwen3.5自动提示词--文生视频_2035656316517093377.json
name: Wan2.2 Smooth V3--Qwen3.5自动提示词--文生视频_2035656316517093377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Smooth V3--Qwen3.5自动提示词--文生视频_2035656316517093377.json
hash: e4fecf8281f5a8e0
coverage: 0.848485
learned_at: 2026-10-15 22:35:50
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, llama_cpp_model_loader, llama_cpp_parameters, CR Text, CLIPTextEncode, ModelSamplingSD3, easy showAnything, llama_cpp_instruct_adv, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, CR Prompt Text, JWInteger, JWInteger, JWInteger, Note, Note, Note, UNETLoader, easy showAnything, ShellAgentPluginOutputText, easy cleanGpuUsed, ModelSamplingSD3, EmptyHunyuanLatentVideo, KSamplerAdvanced, VAEDecode, ImageFromBatch+, KSamplerAdvanced, VHS_VideoCombine, easy anythingIndexSwitch]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Smooth V3--Qwen3.5自动提示词--文生视频_2035656316517093377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035656316517093377.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CR Text`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `easy showAnything`
- `ShellAgentPluginOutputText`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CR Text`、`ModelSamplingSD3`、`llama_cpp_instruct_adv`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`CR Prompt Text`、`JWInteger`、`ShellAgentPluginOutputText`、`easy cleanGpuUsed`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`VAEDecode`、`ImageFromBatch+`、`VHS_VideoCombine`、`easy anythingIndexSwitch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
