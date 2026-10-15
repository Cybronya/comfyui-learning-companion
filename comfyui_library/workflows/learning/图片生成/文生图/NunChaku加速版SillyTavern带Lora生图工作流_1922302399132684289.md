---
key: 图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json
name: NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json
hash: c7d2b9fa3aae76f3
coverage: 0.619048
learned_at: 2026-10-10 20:58:47
nodes: [EmptyLatentImage, KSamplerSelect, VAELoader, RandomNoise, Note Plus (mtb), BasicGuider, BasicScheduler, SamplerCustomAdvanced, VAEDecode, CR Combine Prompt, NunchakuTextEncoderLoader, CLIPTextEncode, SaveImage, easy showAnything, NunchakuFluxDiTLoader, LoraLoaderModelOnly, CR Prompt Text, CR Prompt Text, Note, Note, Note]
patterns: []
missing: [Note Plus (mtb), CR Combine Prompt, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
discoveries: [次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Combine Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json`

## 结构

**节点**（21 个）：
- `EmptyLatentImage`
- `KSamplerSelect`
- `VAELoader`
- `RandomNoise`
- `Note Plus (mtb)`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `CR Combine Prompt`
- `NunchakuTextEncoderLoader`
- `CLIPTextEncode`
- `SaveImage`
- `easy showAnything`
- `NunchakuFluxDiTLoader`
- `LoraLoaderModelOnly`
- `CR Prompt Text`
- `CR Prompt Text`
- `Note`
- `Note`
- `Note`

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `width` = `1024`

## 知识

覆盖率 **62%**（13/21）

**有卡**：`EmptyLatentImage`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`Note Plus (mtb)`、`BasicGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`CR Combine Prompt`、`NunchakuTextEncoderLoader`、`CLIPTextEncode`、`SaveImage`

**缺卡**（4）：`Note Plus (mtb)`、`CR Combine Prompt`、`CR Prompt Text`、`CR Prompt Text`

## 学习发现

- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Combine Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
