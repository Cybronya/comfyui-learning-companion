---
key: 平台全量/Qwen-Image +Lightning1.1 8极速生图_1955815094250868737.json
name: Qwen-Image +Lightning1.1 8极速生图_1955815094250868737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image +Lightning1.1 8极速生图_1955815094250868737.json
hash: bbab4be2d729e8cb
coverage: 0.833333
learned_at: 2026-11-14 00:51:28
nodes: [UNETLoader, UnetLoaderGGUF, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, RH_LLMAPI_NODE, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, SaveImage, TTP_text_mix, ImpactSwitch, ShowText|pysssss, PrimitiveStringMultiline, CR SDXL Aspect Ratio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 986498957992915, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-Image +Lightning1.1 8极速生图_1955815094250868737.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image +Lightning1.1 8极速生图_1955815094250868737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `TTP_text_mix`
- `ImpactSwitch`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `CR SDXL Aspect Ratio`

## 关键参数

- `seed` = `986498957992915`
- `steps` = `8`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`UNETLoader`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`PathchSageAttentionKJ`、`RH_LLMAPI_NODE`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`SaveImage`、`TTP_text_mix`、`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、CR SDXL Aspect Ratio

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
