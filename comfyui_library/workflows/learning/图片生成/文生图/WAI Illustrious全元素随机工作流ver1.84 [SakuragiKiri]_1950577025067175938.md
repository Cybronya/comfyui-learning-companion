---
key: 图片生成/文生图/WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938.json
name: WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938.json
hash: beea109969d75240
coverage: 0.705128
learned_at: 2026-10-15 22:27:34
nodes: [Reroute, Reroute, Reroute, Reroute, Int, Int, Int, Int, Int, Reroute, Int, Int, Int, Int, StringConcatenate, easy textSwitch, easy textSwitch, easy textSwitch, CLIPSetLastLayer, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, workflow>MainLoad, Int, JjkText, JjkConcat, JjkText, CLIPTextEncode, easy textSwitch, easy textSwitch, easy textSwitch, JjkConcat, StringConcatenate, StringConcatenate, CR Split String, CR Split String, JjkText, StringConcatenate, JjkText, Reroute, JjkText, StringConcatenate, JjkText, Reroute, Int, easy textSwitch, ImpactStringSelector, easy showAnything, JjkText, easy textSwitch, easy textSwitch, easy textSwitch, JjkText, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, KSampler, easy loraStackApply, easy loraStack, JjkText, JjkText, TextRandomMultiline, CLIPTextEncode, math_calculate, PrimitiveFloat, JjkText, SaveImage, JjkConcat, JjkConcat, PrimitiveString, JjkText, JjkText]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 1062863783454195, "steps": 20}
---

# 图片生成/文生图/WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Reroute`
- `Int`
- `Int`
- `Int`
- `Int`
- `StringConcatenate`
- `easy textSwitch`
- `easy textSwitch`
- `easy textSwitch`
- `CLIPSetLastLayer`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `workflow>MainLoad`
- `Int`
- `JjkText`
- `JjkConcat`
- `JjkText`
- `CLIPTextEncode` ★核心
- `easy textSwitch`
- `easy textSwitch`
- `easy textSwitch`
- `JjkConcat`
- `StringConcatenate`
- `StringConcatenate`
- `CR Split String`
- `CR Split String`
- `JjkText`
- `StringConcatenate`
- `JjkText`
- `Reroute`
- `JjkText`
- `StringConcatenate`
- `JjkText`
- `Reroute`
- `Int`
- `easy textSwitch`
- `ImpactStringSelector`
- `easy showAnything`
- `JjkText`
- `easy textSwitch`
- `easy textSwitch`
- `easy textSwitch`
- `JjkText`
- `TextRandomMultiline`
- `TextRandomMultiline`
- `TextRandomMultiline`
- `TextRandomMultiline`
- `TextRandomMultiline`
- `TextRandomMultiline`
- `TextRandomMultiline`
- `TextRandomMultiline`
- `KSampler` ★核心
- `easy loraStackApply`
- `easy loraStack`
- `JjkText`
- `JjkText`
- `TextRandomMultiline`
- `CLIPTextEncode` ★核心
- `math_calculate`
- `PrimitiveFloat`
- `JjkText`
- `SaveImage`
- `JjkConcat`
- `JjkConcat`
- `PrimitiveString`
- `JjkText`
- `JjkText`

## 关键参数

- `seed` = `1062863783454195`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **71%**（55/78）

**有卡**：`Int`、`StringConcatenate`、`easy textSwitch`、`CLIPSetLastLayer`、`VAEDecode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`workflow>MainLoad`、`JjkConcat`、`CLIPTextEncode`、`CR Split String`、`ImpactStringSelector`、`TextRandomMultiline`、`KSampler`、`easy loraStackApply`、`easy loraStack`、`math_calculate`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、easy loraStack、easy loraStackApply、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader
