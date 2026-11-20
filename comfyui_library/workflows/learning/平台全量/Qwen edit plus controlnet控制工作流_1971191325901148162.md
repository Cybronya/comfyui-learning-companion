---
key: 平台全量/Qwen edit plus controlnet控制工作流_1971191325901148162.json
name: Qwen edit plus controlnet控制工作流_1971191325901148162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen edit plus controlnet控制工作流_1971191325901148162.json
hash: 8c9be816a1a144df
coverage: 1
learned_at: 2026-11-14 00:50:33
nodes: [UNETLoader, VAEDecode, LoadImage, ModelSamplingAuraFlow, CFGNorm, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPLoader, VAELoader, KSampler, ConditioningZeroOut, AIO_Preprocessor, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus_lrzjason]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 685744360080255, "steps": 10}
---

# 平台全量/Qwen edit plus controlnet控制工作流_1971191325901148162.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen edit plus controlnet控制工作流_1971191325901148162.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `AIO_Preprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus_lrzjason`

## 关键参数

- `seed` = `685744360080255`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`UNETLoader`、`VAEDecode`、`LoadImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`KSampler`、`ConditioningZeroOut`、`AIO_Preprocessor`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
