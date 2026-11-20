---
key: 平台全量/批量生成极致真实人像 QWEN+Z image turbo提升美学质感 cosplay角色扮演  自_2033388995471745025.json
name: 批量生成极致真实人像 QWEN+Z image turbo提升美学质感 cosplay角色扮演  自_2033388995471745025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/批量生成极致真实人像 QWEN+Z image turbo提升美学质感 cosplay角色扮演  自_2033388995471745025.json
hash: 471d3d35e3be2cbc
coverage: 0.96875
learned_at: 2026-11-14 02:05:43
nodes: [ConditioningZeroOut, VAEEncode, ConditioningZeroOut, VAEDecode, ModelSamplingAuraFlow, VAEDecode, EmptyLatentImage, ModelSamplingAuraFlow, KSamplerAdvanced, CLIPLoader, KSamplerAdvanced, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, JDCN_StringToList, ProcessString, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, SaveImage, CR Text Replace, PreviewImage, CR Text, easy int, easy int, CR Text, RH_LLMAPI_NODE, VAELoader, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1920, "sampler_name": 1, "scheduler": "dpmpp_2m", "seed": "enable", "steps": "randomize", "width": 1080}
---

# 平台全量/批量生成极致真实人像 QWEN+Z image turbo提升美学质感 cosplay角色扮演  自_2033388995471745025.json

> 来源文件 `comfyui_library/workflows/平台全量/批量生成极致真实人像 QWEN+Z image turbo提升美学质感 cosplay角色扮演  自_2033388995471745025.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `JDCN_StringToList`
- `ProcessString`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SaveImage`
- `CR Text Replace`
- `PreviewImage`
- `CR Text`
- `easy int`
- `easy int`
- `CR Text`
- `RH_LLMAPI_NODE`
- `VAELoader`
- `CR Text`

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_2m`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`ConditioningZeroOut`、`VAEEncode`、`VAEDecode`、`ModelSamplingAuraFlow`、`EmptyLatentImage`、`KSamplerAdvanced`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`JDCN_StringToList`、`ProcessString`、`PathchSageAttentionKJ`、`SaveImage`、`CR Text Replace`、`CR Text`、`easy int`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader
