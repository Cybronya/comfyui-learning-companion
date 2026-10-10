---
key: ComfyUI进阶教程：运用In-Context LoRA精准控制角色一致性_1920491097255251969.json
name: ComfyUI进阶教程：运用In-Context LoRA精准控制角色一致性_1920491097255251969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ComfyUI进阶教程：运用In-Context LoRA精准控制角色一致性_1920491097255251969.json
hash: 41abd09c9dcbb038
coverage: 0.766667
learned_at: 2026-10-10 21:26:59
nodes: [DualCLIPLoader, TextInput_, TextInput_, TextInput_, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, SamplerCustomAdvanced, CR Text Concatenate, UNETLoader, CLIPTextEncode, VAELoader, KSamplerSelect, BasicGuider, RandomNoise, LoraLoader, Anything Everywhere3, VAEDecode, TextInput_, BasicScheduler, EmptyLatentImage, Text Concatenate (JPS), easy showAnything, TextInput_, TextInput_, TextInput_, TextInput_, TextInput_, LoraLoader, SaveImage]
patterns: [lora]
missing: [CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, Text Concatenate (JPS)]
parameters: {"batch_size": 1, "height": 1536, "lora_name": "粉色情人-000012.safetensors", "strength_clip": 1, "strength_model": 0.6, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识]
---

# ComfyUI进阶教程：运用In-Context LoRA精准控制角色一致性_1920491097255251969.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ComfyUI进阶教程：运用In-Context LoRA精准控制角色一致性_1920491097255251969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `DualCLIPLoader`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `SamplerCustomAdvanced` ★核心
- `CR Text Concatenate`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `LoraLoader` ★核心
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `TextInput_`
- `BasicScheduler`
- `EmptyLatentImage` ★核心
- `Text Concatenate (JPS)`
- `easy showAnything`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `LoraLoader` ★核心
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `粉色情人-000012.safetensors`
- `strength_model` = `0.6`
- `strength_clip` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`DualCLIPLoader`、`TextInput_`、`SamplerCustomAdvanced`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`LoraLoader`、`VAEDecode`、`BasicScheduler`、`EmptyLatentImage`、`SaveImage`

**缺卡**（5）：`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`Text Concatenate (JPS)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LoraLoader

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识
