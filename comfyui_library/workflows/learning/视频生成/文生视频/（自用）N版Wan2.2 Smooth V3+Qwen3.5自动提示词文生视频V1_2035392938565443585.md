---
key: 视频生成/文生视频/（自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035392938565443585.json
name: （自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035392938565443585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035392938565443585.json
hash: 90a306f11c9b84bf
coverage: 0.785714
learned_at: 2026-10-11 03:48:41
nodes: [EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, Seed (rgthree), llama_cpp_model_loader, llama_cpp_parameters, VAEDecode, LoraLoaderModelOnly, easy cleanGpuUsed, ShellAgentPluginOutputText, UNETLoader, CLIPTextEncode, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, JWInteger, PathchSageAttentionKJ, JWInteger, JWInteger, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, easy showAnything, easy showAnything, easy anythingIndexSwitch, llama_cpp_instruct_adv, LoadImage, UNETLoader, UNETLoader, CR Text, CR Prompt Text, TT_img_enc, SaveImage, TT_img_enc_v2, SaveImage, SaveImage, DuckHideNode, Reroute, VHS_VideoCombine, ImageFromBatch+]
patterns: []
missing: [CR Text, ImageFromBatch+, easy anythingIndexSwitch, easy cleanGpuUsed, CR Prompt Text, Seed (rgthree)]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035392938565443585.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035392938565443585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `llama_cpp_model_loader`
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
- `easy anythingIndexSwitch`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `CR Prompt Text`
- `TT_img_enc`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `SaveImage`
- `DuckHideNode`
- `Reroute`
- `VHS_VideoCombine`
- `ImageFromBatch+`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`VAEDecode`、`ShellAgentPluginOutputText`、`UNETLoader`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`JWInteger`、`ModelSamplingSD3`、`llama_cpp_instruct_adv`、`LoadImage`、`TT_img_enc`、`SaveImage`、`TT_img_enc_v2`、`DuckHideNode`、`VHS_VideoCombine`

**缺卡**（6）：`CR Text`、`ImageFromBatch+`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
