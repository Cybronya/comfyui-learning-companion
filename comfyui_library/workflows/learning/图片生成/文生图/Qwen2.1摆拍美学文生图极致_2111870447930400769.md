---
key: 图片生成/文生图/Qwen2.1摆拍美学文生图极致_2111870447930400769.json
name: Qwen2.1摆拍美学文生图极致_2111870447930400769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1摆拍美学文生图极致_2111870447930400769.json
hash: e7b826e2b8b38b51
coverage: 0.814815
learned_at: 2026-10-21 02:54:44
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, CR Text, llama_cpp_instruct_adv, JDCN_StringToList, ProcessString, llama_cpp_model_loader, CR Text Replace, PrimitiveInt, llama_cpp_parameters, CR Text, LoadImage, SaveImage, QwenImage21Cache, Note, Note, ResolutionSelector, Note, Note, CR Text, CR Text, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 589160589172486, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen2.1摆拍美学文生图极致_2111870447930400769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1摆拍美学文生图极致_2111870447930400769.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CR Text`
- `llama_cpp_instruct_adv`
- `JDCN_StringToList`
- `ProcessString`
- `llama_cpp_model_loader`
- `CR Text Replace`
- `PrimitiveInt`
- `llama_cpp_parameters`
- `CR Text`
- `LoadImage`
- `SaveImage`
- `QwenImage21Cache`
- `Note`
- `Note`
- `ResolutionSelector`
- `Note`
- `Note`
- `CR Text`
- `CR Text`
- `CR Text`

## 关键参数

- `seed` = `589160589172486`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`CR Text`、`llama_cpp_instruct_adv`、`JDCN_StringToList`、`ProcessString`、`llama_cpp_model_loader`、`CR Text Replace`、`llama_cpp_parameters`、`LoadImage`、`SaveImage`、`QwenImage21Cache`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
