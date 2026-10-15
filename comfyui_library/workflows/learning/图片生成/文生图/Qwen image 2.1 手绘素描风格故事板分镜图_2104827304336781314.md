---
key: 图片生成/文生图/Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314.json
name: Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314.json
hash: 37ba621a8ad9ab57
coverage: 0.244444
learned_at: 2026-10-10 20:58:56
nodes: [CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy promptConcat, easy setNode, easy setNode, easy textIndexSwitch, easy setNode, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy textIndexSwitch, easy textIndexSwitch, CR Prompt Text, easy getNode, easy getNode, easy getNode, easy promptConcat, CLIPLoader, VAELoader, CR Prompt Text, UNETLoader, KSampler, easy seed, EmptyLatentImage, ResolutionSelector, TextEncodeQwenImage21, PreviewAny, SaveImageAdvanced, PreviewImage, VAEDecode, SaveImage, CR Prompt Text, INTConstant]
patterns: []
missing: [easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, easy textIndexSwitch, easy textIndexSwitch, easy textIndexSwitch, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy promptConcat, easy promptConcat, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
discoveries: [次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy textIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy textIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 手绘素描风格故事板分镜图_2104827304336781314.json`

## 结构

**节点**（45 个）：
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy promptConcat`
- `easy setNode`
- `easy setNode`
- `easy textIndexSwitch`
- `easy setNode`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy textIndexSwitch`
- `easy textIndexSwitch`
- `CR Prompt Text`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy promptConcat`
- `CLIPLoader`
- `VAELoader`
- `CR Prompt Text`
- `UNETLoader`
- `KSampler`
- `easy seed`
- `EmptyLatentImage`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `SaveImageAdvanced`
- `PreviewImage`
- `VAEDecode`
- `SaveImage`
- `CR Prompt Text`
- `INTConstant`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `0`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **24%**（11/45）

**有卡**：`CR Prompt Text`、`easy promptConcat`、`easy setNode`、`easy textIndexSwitch`

**缺卡**（32）：`easy getNode`、`easy getNode`、`easy getNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy textIndexSwitch`、`easy textIndexSwitch`、`easy textIndexSwitch`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`easy promptConcat`、`easy promptConcat`、`easy seed`

## 学习发现

- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
