---
key: 图片生成/文生图/Qwen Hyperdetailed Colored Pencil lora_1992568129347973121.json
name: Qwen Hyperdetailed Colored Pencil lora_1992568129347973121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Hyperdetailed Colored Pencil lora_1992568129347973121.json
hash: 85c82255be62cdd9
coverage: 0.8
learned_at: 2026-10-19 20:34:18
nodes: [SaveImage, Note, VAEDecode, KSampler, VAELoader, CLIPLoader, LoraLoaderModelOnly, ConditioningZeroOut, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, MuyeTextEditOutput, EmptySD3LatentImage, GetImageSize+, UNETLoader, PreviewAny, CLIPTextEncode, PreviewImage, LoadImage, ShowText|pysssss, MultiTextConcatenate]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 425324, "steps": 26}
---

# 图片生成/文生图/Qwen Hyperdetailed Colored Pencil lora_1992568129347973121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Hyperdetailed Colored Pencil lora_1992568129347973121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `SaveImage`
- `Note`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `MuyeTextEditOutput`
- `EmptySD3LatentImage`
- `GetImageSize+`
- `UNETLoader` ★核心
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LoadImage`
- `ShowText|pysssss`
- `MultiTextConcatenate`

## 关键参数

- `seed` = `425324`
- `steps` = `26`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`MuyeTextEditOutput`、`EmptySD3LatentImage`、`GetImageSize+`、`UNETLoader`、`CLIPTextEncode`、`LoadImage`、`MultiTextConcatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage
