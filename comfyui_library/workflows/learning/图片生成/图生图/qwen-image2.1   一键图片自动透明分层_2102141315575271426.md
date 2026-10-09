---
key: 图片生成/图生图/qwen-image2.1   一键图片自动透明分层_2102141315575271426.json
name: qwen-image2.1   一键图片自动透明分层_2102141315575271426.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image2.1   一键图片自动透明分层_2102141315575271426.json
hash: 3cdf5051ceb97da2
coverage: 0.55
learned_at: 2026-10-09 22:19:27
nodes: [easy forLoopEnd, SaveImage, CLIPLoader, VAELoader, TextEncodeQwenImage21, VAEDecode, easy forLoopEnd, KSampler, UNETLoader, PreviewAny, easy forLoopStart, Text Load Line From File, SaveImage, QwenImage21Cache, PreviewAny, PrimitiveStringMultiline, RHLLMChatNode, PreviewAny, LoadImage, CR Text]
patterns: []
missing: [CR Text, Text Load Line From File, easy forLoopEnd, easy forLoopEnd, easy forLoopStart]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 52269850447356, "steps": 25}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/qwen-image2.1   一键图片自动透明分层_2102141315575271426.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102141315575271426.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `easy forLoopEnd`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `PreviewAny`
- `easy forLoopStart`
- `Text Load Line From File`
- `SaveImage`
- `QwenImage21Cache`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RHLLMChatNode`
- `PreviewAny`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `52269850447356`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **55%**（11/20）

**有卡**：`SaveImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`VAEDecode`、`KSampler`、`UNETLoader`、`QwenImage21Cache`、`RHLLMChatNode`、`LoadImage`

**缺卡**（5）：`CR Text`、`Text Load Line From File`、`easy forLoopEnd`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
