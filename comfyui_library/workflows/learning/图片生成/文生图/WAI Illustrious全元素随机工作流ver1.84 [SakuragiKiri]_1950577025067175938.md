---
key: WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938.json
name: WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938.json
hash: beea109969d75240
coverage: 0.512821
learned_at: 2026-10-10 20:59:13
nodes: [Reroute, Reroute, Reroute, Reroute, Int, Int, Int, Int, Int, Reroute, Int, Int, Int, Int, StringConcatenate, easy textSwitch, easy textSwitch, easy textSwitch, CLIPSetLastLayer, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, workflow>MainLoad, Int, JjkText, JjkConcat, JjkText, CLIPTextEncode, easy textSwitch, easy textSwitch, easy textSwitch, JjkConcat, StringConcatenate, StringConcatenate, CR Split String, CR Split String, JjkText, StringConcatenate, JjkText, Reroute, JjkText, StringConcatenate, JjkText, Reroute, Int, easy textSwitch, ImpactStringSelector, easy showAnything, JjkText, easy textSwitch, easy textSwitch, easy textSwitch, JjkText, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, TextRandomMultiline, KSampler, easy loraStackApply, easy loraStack, JjkText, JjkText, TextRandomMultiline, CLIPTextEncode, math_calculate, PrimitiveFloat, JjkText, SaveImage, JjkConcat, JjkConcat, PrimitiveString, JjkText, JjkText]
patterns: []
missing: [CR Split String, CR Split String, easy textSwitch, easy textSwitch, easy textSwitch, easy textSwitch, easy textSwitch, easy textSwitch, easy textSwitch, easy textSwitch, easy textSwitch, easy textSwitch, workflow>MainLoad, easy loraStack, easy loraStackApply]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 1062863783454195, "steps": 20}
discoveries: [次要节点 `CR Split String` 知识库中没有该节点类型的任何知识, 次要节点 `CR Split String` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>MainLoad` 知识库中没有该节点类型的任何知识, 次要节点 `easy loraStack` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `easy loraStackApply` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938.json

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

覆盖率 **51%**（40/78）

**有卡**：`Int`、`StringConcatenate`、`CLIPSetLastLayer`、`VAEDecode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`JjkConcat`、`CLIPTextEncode`、`ImpactStringSelector`、`TextRandomMultiline`、`KSampler`、`math_calculate`、`SaveImage`

**缺卡**（15）：`CR Split String`、`CR Split String`、`easy textSwitch`、`easy textSwitch`、`easy textSwitch`、`easy textSwitch`、`easy textSwitch`、`easy textSwitch`、`easy textSwitch`、`easy textSwitch`、`easy textSwitch`、`easy textSwitch`、`workflow>MainLoad`、`easy loraStack`、`easy loraStackApply`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader、CLIPSetLastLayer、SaveImage

## 学习发现

- 次要节点 `CR Split String` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Split String` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>MainLoad` 知识库中没有该节点类型的任何知识
- 次要节点 `easy loraStack` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `easy loraStackApply` 仅有 LoRA 的通用知识，没有该节点自己的说明
