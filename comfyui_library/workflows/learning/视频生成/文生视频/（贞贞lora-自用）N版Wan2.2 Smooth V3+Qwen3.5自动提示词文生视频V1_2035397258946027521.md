---
key: 视频生成/文生视频/（贞贞lora-自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035397258946027521.json
name: （贞贞lora-自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035397258946027521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（贞贞lora-自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035397258946027521.json
hash: db90cb6e8e48fada
coverage: 0.931818
learned_at: 2026-10-15 22:49:12
nodes: [EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, CLIPTextEncode, Seed (rgthree), llama_cpp_model_loader, llama_cpp_parameters, VAEDecode, easy cleanGpuUsed, ShellAgentPluginOutputText, UNETLoader, CLIPTextEncode, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, JWInteger, JWInteger, JWInteger, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, easy showAnything, llama_cpp_instruct_adv, LoadImage, UNETLoader, UNETLoader, CR Text, TT_img_enc, SaveImage, TT_img_enc_v2, SaveImage, SaveImage, DuckHideNode, Reroute, ImageFromBatch+, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, easy anythingIndexSwitch, ConcatTextOfUtils, easy showAnything, CR Prompt Text, VHS_VideoCombine, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/（贞贞lora-自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035397258946027521.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（贞贞lora-自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035397258946027521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ShellAgentPluginOutputText`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `TT_img_enc`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `SaveImage`
- `DuckHideNode`
- `Reroute`
- `ImageFromBatch+`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy anythingIndexSwitch`
- `ConcatTextOfUtils`
- `easy showAnything`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`Seed (rgthree)`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`VAEDecode`、`easy cleanGpuUsed`、`ShellAgentPluginOutputText`、`UNETLoader`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`JWInteger`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`llama_cpp_instruct_adv`、`LoadImage`、`CR Text`、`TT_img_enc`、`SaveImage`、`TT_img_enc_v2`、`DuckHideNode`、`ImageFromBatch+`、`easy anythingIndexSwitch`、`ConcatTextOfUtils`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader
