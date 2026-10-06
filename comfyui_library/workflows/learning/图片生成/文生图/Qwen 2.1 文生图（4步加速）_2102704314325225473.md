---
key: 图片生成/文生图/Qwen 2.1 文生图（4步加速）_2102704314325225473.json
name: Qwen 2.1 文生图（4步加速）_2102704314325225473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen 2.1 文生图（4步加速）_2102704314325225473.json
hash: 667bf4f4393811ba
coverage: 0.75
learned_at: 2026-10-07 02:13:13
nodes: [TextEncodeQwenImage21, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, SaveImage, EmptyLatentImage, QwenImage21Cache, VAEDecode, easy cleanGpuUsed, CR Prompt Text, ResolutionSelector, QwenPERewriteT8, easy showAnything, ComfySwitchNode, KSampler]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 410785944010461, "steps": 8, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen 2.1 文生图（4步加速）_2102704314325225473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen 2.1 文生图（4步加速）_2102704314325225473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CR Prompt Text`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `easy showAnything`
- `ComfySwitchNode`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `410785944010461`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`ResolutionSelector`、`QwenPERewriteT8`、`KSampler`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
