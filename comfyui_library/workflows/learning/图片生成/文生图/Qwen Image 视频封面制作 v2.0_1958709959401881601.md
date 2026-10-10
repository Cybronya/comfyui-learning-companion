---
key: Qwen Image 视频封面制作 v2.0_1958709959401881601.json
name: Qwen Image 视频封面制作 v2.0_1958709959401881601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 视频封面制作 v2.0_1958709959401881601.json
hash: 988486a42dc0af8f
coverage: 0.536585
learned_at: 2026-10-10 20:58:55
nodes: [LoadImage, TextCombinerTwo, VAELoader, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, easy showAnything, RH_LLMAPI_NODE, JjkText, TextCombinerTwo, VAEDecode, easy showAnything, JjkText, TextCombinerTwo, TextCombinerSix, JjkText, JjkText, JjkText, TextCombinerTwo, TextCombinerTwo, JjkText, JjkText, TextCombinerSix, JjkText, JjkText, ModelSamplingAuraFlow, SaveImage, EmptySD3LatentImage, LimitNumber, EmptySD3LatentImage, PrimitiveInt, Note, easy seed, EmptySD3LatentImage, ImpactSwitch, KSampler, JjkText, JjkText, JjkText, JjkText]
patterns: []
missing: [easy seed]
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 43418218178449, "steps": 20}
discoveries: [次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# Qwen Image 视频封面制作 v2.0_1958709959401881601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 视频封面制作 v2.0_1958709959401881601.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `LoadImage`
- `TextCombinerTwo`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `JjkText`
- `TextCombinerTwo`
- `VAEDecode` ★核心
- `easy showAnything`
- `JjkText`
- `TextCombinerTwo`
- `TextCombinerSix`
- `JjkText`
- `JjkText`
- `JjkText`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `JjkText`
- `TextCombinerSix`
- `JjkText`
- `JjkText`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `EmptySD3LatentImage`
- `LimitNumber`
- `EmptySD3LatentImage`
- `PrimitiveInt`
- `Note`
- `easy seed`
- `EmptySD3LatentImage`
- `ImpactSwitch`
- `KSampler` ★核心
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`

## 关键参数

- `seed` = `43418218178449`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **54%**（22/41）

**有卡**：`LoadImage`、`TextCombinerTwo`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`RH_LLMAPI_NODE`、`VAEDecode`、`TextCombinerSix`、`ModelSamplingAuraFlow`、`SaveImage`、`EmptySD3LatentImage`、`LimitNumber`、`KSampler`

**缺卡**（1）：`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SaveImage

## 学习发现

- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
