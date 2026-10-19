---
key: 图片生成/文生图/(Qc_Lora)Z-ImageLora_text_1996391726472380417.json
name: (Qc_Lora)Z-ImageLora_text_1996391726472380417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/(Qc_Lora)Z-ImageLora_text_1996391726472380417.json
hash: c55ac0b989f58fb7
coverage: 0.758621
learned_at: 2026-10-19 21:32:23
nodes: [Float, Float, PrimitiveNode, Note, Note, Note, JoinStringMulti, CR Math Operation, easy convertAnything, SimpleMath+, EmptyLatentImage, easy forLoopStart, SaveImage, easy forLoopEnd, CR Image Grid Panel, easy batchAnything, ConditioningZeroOut, VAELoader, UNETLoader, GoogleTranslateCLIPTextEncodeNode, CLIPLoader, VAEDecode, LoraLoaderModelOnly, MuyeTextEditOutput, KSampler, Note, Note, AddLabel, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m_sde", "scheduler": "sgm_uniform", "seed": 451393420513315, "steps": 20, "width": 1024}
---

# 图片生成/文生图/(Qc_Lora)Z-ImageLora_text_1996391726472380417.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/(Qc_Lora)Z-ImageLora_text_1996391726472380417.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Float`
- `Float`
- `PrimitiveNode`
- `Note`
- `Note`
- `Note`
- `JoinStringMulti`
- `CR Math Operation`
- `easy convertAnything`
- `SimpleMath+`
- `EmptyLatentImage` ★核心
- `easy forLoopStart`
- `SaveImage`
- `easy forLoopEnd`
- `CR Image Grid Panel`
- `easy batchAnything`
- `ConditioningZeroOut`
- `VAELoader`
- `UNETLoader` ★核心
- `GoogleTranslateCLIPTextEncodeNode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `MuyeTextEditOutput`
- `KSampler` ★核心
- `Note`
- `Note`
- `AddLabel`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `451393420513315`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **76%**（22/29）

**有卡**：`Float`、`JoinStringMulti`、`CR Math Operation`、`easy convertAnything`、`SimpleMath+`、`EmptyLatentImage`、`easy forLoopStart`、`SaveImage`、`easy forLoopEnd`、`CR Image Grid Panel`、`easy batchAnything`、`ConditioningZeroOut`、`VAELoader`、`UNETLoader`、`GoogleTranslateCLIPTextEncodeNode`、`CLIPLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`MuyeTextEditOutput`、`KSampler`、`AddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、SaveImage、EmptyLatentImage
