---
key: 图片生成/文生图/Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609.json
name: Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609.json
hash: 975a5ab0db87458a
coverage: 0.909091
learned_at: 2026-10-19 23:21:26
nodes: [VAELoader, ConditioningZeroOut, EmptyFlux2LatentImage, SamplerCustomAdvanced, KSamplerSelect, Ideogram4Scheduler, RandomNoise, ComfyNumberConvert, JsonExtractString, ComfyNumberConvert, StringReplace, JsonExtractString, ComfyNumberConvert, DualModelGuider, CFGOverride, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, JsonExtractString, JsonExtractString, CR Prompt Text, CR Prompt Text, VAEDecode, PreviewImage, PreviewAny, ImageBlend, CR Prompt Text, easy anythingIndexSwitch, SaveImage, SaveImage, Ideogram4PromptBuilderKJ, PrimitiveInt]
patterns: []
missing: []
---

# 图片生成/文生图/Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Ideogram4Scheduler`
- `RandomNoise`
- `ComfyNumberConvert`
- `JsonExtractString`
- `ComfyNumberConvert`
- `StringReplace`
- `JsonExtractString`
- `ComfyNumberConvert`
- `DualModelGuider`
- `CFGOverride`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `JsonExtractString`
- `JsonExtractString`
- `CR Prompt Text`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewAny`
- `ImageBlend`
- `CR Prompt Text`
- `easy anythingIndexSwitch`
- `SaveImage`
- `SaveImage`
- `Ideogram4PromptBuilderKJ`
- `PrimitiveInt`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`KSamplerSelect`、`Ideogram4Scheduler`、`RandomNoise`、`ComfyNumberConvert`、`JsonExtractString`、`StringReplace`、`DualModelGuider`、`CFGOverride`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`CR Prompt Text`、`VAEDecode`、`ImageBlend`、`easy anythingIndexSwitch`、`SaveImage`、`Ideogram4PromptBuilderKJ`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、KSamplerSelect、SamplerCustomAdvanced
