---
key: 图片生成/文生图/Qwen Image 视频封面制作 v3.0_1970924112187138049.json
name: Qwen Image 视频封面制作 v3.0_1970924112187138049.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 视频封面制作 v3.0_1970924112187138049.json
hash: 8cefa9a251d1c861
coverage: 0.558824
learned_at: 2026-10-09 02:01:39
nodes: [LoadImage, VAELoader, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, VAEDecode, ModelSamplingAuraFlow, SaveImage, EmptySD3LatentImage, LimitNumber, EmptySD3LatentImage, ImpactSwitch, JjkText, TextCombinerTwo, Note, TextCombinerTwo, TextCombinerTwo, TextCombinerSix, JjkText, JjkText, EmptySD3LatentImage, PrimitiveInt, easy seed, JjkText, JjkText, RH_LLMAPI_NODE, JjkText, KSampler, JjkText, easy showAnything, Note, JjkText, JjkText]
patterns: []
missing: [easy seed]
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 43418218178449, "steps": 30}
discoveries: [次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 视频封面制作 v3.0_1970924112187138049.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1970924112187138049.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoadImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `EmptySD3LatentImage`
- `LimitNumber`
- `EmptySD3LatentImage`
- `ImpactSwitch`
- `JjkText`
- `TextCombinerTwo`
- `Note`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `TextCombinerSix`
- `JjkText`
- `JjkText`
- `EmptySD3LatentImage`
- `PrimitiveInt`
- `easy seed`
- `JjkText`
- `JjkText`
- `RH_LLMAPI_NODE`
- `JjkText`
- `KSampler` ★核心
- `JjkText`
- `easy showAnything`
- `Note`
- `JjkText`
- `JjkText`

## 关键参数

- `seed` = `43418218178449`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **56%**（19/34）

**有卡**：`LoadImage`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`ModelSamplingAuraFlow`、`SaveImage`、`EmptySD3LatentImage`、`LimitNumber`、`TextCombinerTwo`、`TextCombinerSix`、`RH_LLMAPI_NODE`、`KSampler`

**缺卡**（1）：`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SaveImage

## 学习发现

- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
