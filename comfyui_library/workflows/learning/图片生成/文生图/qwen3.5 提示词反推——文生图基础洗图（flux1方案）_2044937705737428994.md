---
key: 图片生成/文生图/qwen3.5 提示词反推——文生图基础洗图（flux1方案）_2044937705737428994.json
name: qwen3.5 提示词反推——文生图基础洗图（flux1方案）_2044937705737428994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen3.5 提示词反推——文生图基础洗图（flux1方案）_2044937705737428994.json
hash: 68d7ba5b2f4145fb
coverage: 0.769231
learned_at: 2026-10-21 02:57:36
nodes: [VAELoader, NunchakuFluxLoraLoader, KSamplerSelect, Fast Groups Bypasser (rgthree), EmptyLatentImage, NunchakuFluxDiTLoader, VAEDecode, BasicScheduler, SamplerCustomAdvanced, RandomNoise, BasicGuider, DualCLIPLoader, Note, llama_cpp_parameters, easy saveText, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, SaveImage, PreviewAny, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, llama_cpp_model_loader, CLIPTextEncode, llama_cpp_instruct_adv, Reroute]
patterns: []
missing: []
parameters: {"batch_size": 4, "height": 1384, "width": 1024}
---

# 图片生成/文生图/qwen3.5 提示词反推——文生图基础洗图（flux1方案）_2044937705737428994.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen3.5 提示词反推——文生图基础洗图（flux1方案）_2044937705737428994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `VAELoader`
- `NunchakuFluxLoraLoader` ★核心
- `KSamplerSelect` ★核心
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `NunchakuFluxDiTLoader`
- `VAEDecode` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `DualCLIPLoader`
- `Note`
- `llama_cpp_parameters`
- `easy saveText`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `SaveImage`
- `PreviewAny`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `llama_cpp_model_loader`
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `Reroute`

## 关键参数

- `width` = `1024`
- `height` = `1384`
- `batch_size` = `4`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`VAELoader`、`NunchakuFluxLoraLoader`、`KSamplerSelect`、`EmptyLatentImage`、`NunchakuFluxDiTLoader`、`VAEDecode`、`BasicScheduler`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`DualCLIPLoader`、`llama_cpp_parameters`、`easy saveText`、`SaveImage`、`LoadImage`、`llama_cpp_model_loader`、`CLIPTextEncode`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、KSamplerSelect、SamplerCustomAdvanced、NunchakuFluxLoraLoader
