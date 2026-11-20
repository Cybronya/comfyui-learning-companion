---
key: 平台全量/多人场景融合-千问Edit图像编辑换主体换人物1.0_1970711332947456002.json
name: 多人场景融合-千问Edit图像编辑换主体换人物1.0_1970711332947456002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/多人场景融合-千问Edit图像编辑换主体换人物1.0_1970711332947456002.json
hash: fb30fe5336e10008
coverage: 0.9375
learned_at: 2026-11-14 01:57:24
nodes: [ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, SaveImage, VAELoader, KSampler, SDVN QwenEdit TextEncoder Plus, CLIPLoader, UNETLoader, Text Multiline, Note]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 472741976245928, "steps": 20}
---

# 平台全量/多人场景融合-千问Edit图像编辑换主体换人物1.0_1970711332947456002.json

> 来源文件 `comfyui_library/workflows/平台全量/多人场景融合-千问Edit图像编辑换主体换人物1.0_1970711332947456002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `VAELoader`
- `KSampler` ★核心
- `SDVN QwenEdit TextEncoder Plus`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Text Multiline`
- `Note`

## 关键参数

- `seed` = `472741976245928`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ConditioningZeroOut`、`LoraLoaderModelOnly`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`SaveImage`、`VAELoader`、`KSampler`、`SDVN QwenEdit TextEncoder Plus`、`CLIPLoader`、`UNETLoader`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
