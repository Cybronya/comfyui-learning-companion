---
key: 视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频工作流_2035941912657534978.json
name: Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频工作流_2035941912657534978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频工作流_2035941912657534978.json
hash: b433010dbe2d9b65
coverage: 0.941176
learned_at: 2026-10-15 22:47:10
nodes: [EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, Seed (rgthree), llama_cpp_model_loader, llama_cpp_parameters, CR Text, VAEDecode, LoraLoaderModelOnly, easy cleanGpuUsed, ShellAgentPluginOutputText, llama_cpp_instruct_adv, UNETLoader, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, UNETLoader, ImageFromBatch+, KSamplerAdvanced, KSamplerAdvanced, JWInteger, PathchSageAttentionKJ, JWInteger, JWInteger, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, LoraLoaderModelOnly, easy showAnything, easy showAnything, easy anythingIndexSwitch, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频工作流_2035941912657534978.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频工作流_2035941912657534978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CR Text`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `ShellAgentPluginOutputText`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `ImageFromBatch+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `PathchSageAttentionKJ`
- `JWInteger`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Seed (rgthree)`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CR Text`、`VAEDecode`、`easy cleanGpuUsed`、`ShellAgentPluginOutputText`、`llama_cpp_instruct_adv`、`UNETLoader`、`PathchSageAttentionKJ`、`ImageFromBatch+`、`KSamplerAdvanced`、`JWInteger`、`ModelSamplingSD3`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)
