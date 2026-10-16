---
key: 视频生成/图生视频/wan2.2-i2v-base64输入-base64txt输出-默认jio lora_2000330882630156290.json
name: wan2.2-i2v-base64输入-base64txt输出-默认jio lora_2000330882630156290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2000330882630156290.json
hash: 373b96edf569bdd7
coverage: 0.769231
learned_at: 2026-10-15 22:33:40
nodes: [ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, INTConstant, Note, Note, WanImageToVideo, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, easy showAnything, easy seed, VAEDecode, ImpactImageBatchToImageList, easy imageToBase64, StringListToString, ShowText|pysssss, Text Concatenate, Note, Text Multiline, CLIPTextEncode, Note, easy loadImageBase64, INTConstant, Note, LoraLoaderModelOnly, Note, Note, easy saveText]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-i2v-base64输入-base64txt输出-默认jio lora_2000330882630156290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000330882630156290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `WanImageToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `easy showAnything`
- `easy seed`
- `VAEDecode` ★核心
- `ImpactImageBatchToImageList`
- `easy imageToBase64`
- `StringListToString`
- `ShowText|pysssss`
- `Text Concatenate`
- `Note`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `Note`
- `easy loadImageBase64`
- `INTConstant`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `easy saveText`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`INTConstant`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`easy seed`、`VAEDecode`、`ImpactImageBatchToImageList`、`easy imageToBase64`、`StringListToString`、`Text Concatenate`、`Text Multiline`、`easy loadImageBase64`、`easy saveText`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、easy seed
