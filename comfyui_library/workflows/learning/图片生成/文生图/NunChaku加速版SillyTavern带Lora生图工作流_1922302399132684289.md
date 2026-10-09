---
key: 图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json
name: NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json
hash: c7d2b9fa3aae76f3
coverage: 0.619048
learned_at: 2026-10-07 22:22:28
nodes: [EmptyLatentImage, KSamplerSelect, VAELoader, RandomNoise, Note Plus (mtb), BasicGuider, BasicScheduler, SamplerCustomAdvanced, VAEDecode, CR Combine Prompt, NunchakuTextEncoderLoader, CLIPTextEncode, SaveImage, easy showAnything, NunchakuFluxDiTLoader, LoraLoaderModelOnly, CR Prompt Text, CR Prompt Text, Note, Note, Note]
patterns: []
missing: [Note Plus (mtb), CR Combine Prompt, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
discoveries: [次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Combine Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1922302399132684289.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `EmptyLatentImage` ★核心
- `KSamplerSelect` ★核心
- `VAELoader`
- `RandomNoise`
- `Note Plus (mtb)`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CR Combine Prompt`
- `NunchakuTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `easy showAnything`
- `NunchakuFluxDiTLoader`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `Note`
- `Note`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（13/21）

**有卡**：`EmptyLatentImage`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`BasicGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`NunchakuTextEncoderLoader`、`CLIPTextEncode`、`SaveImage`、`NunchakuFluxDiTLoader`、`LoraLoaderModelOnly`

**缺卡**（4）：`Note Plus (mtb)`、`CR Combine Prompt`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoader

## 学习发现

- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Combine Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
