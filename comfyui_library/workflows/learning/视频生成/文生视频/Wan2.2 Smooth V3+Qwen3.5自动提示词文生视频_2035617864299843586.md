---
key: 视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2035617864299843586.json
name: Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2035617864299843586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2035617864299843586.json
hash: dd02a4dba1c497e6
coverage: 0.764706
learned_at: 2026-10-11 03:48:38
nodes: [EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, Seed (rgthree), llama_cpp_parameters, CR Text, VAEDecode, LoraLoaderModelOnly, easy cleanGpuUsed, ShellAgentPluginOutputText, llama_cpp_instruct_adv, UNETLoader, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, UNETLoader, ImageFromBatch+, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, easy showAnything, easy showAnything, easy anythingIndexSwitch, llama_cpp_model_loader, JWInteger, JWInteger, JWInteger, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: [CR Text, ImageFromBatch+, easy anythingIndexSwitch, easy cleanGpuUsed, CR Prompt Text, Seed (rgthree)]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2035617864299843586.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2035617864299843586.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
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
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `llama_cpp_model_loader`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`llama_cpp_parameters`、`VAEDecode`、`ShellAgentPluginOutputText`、`llama_cpp_instruct_adv`、`UNETLoader`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`ModelSamplingSD3`、`llama_cpp_model_loader`、`JWInteger`、`VHS_VideoCombine`

**缺卡**（6）：`CR Text`、`ImageFromBatch+`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
