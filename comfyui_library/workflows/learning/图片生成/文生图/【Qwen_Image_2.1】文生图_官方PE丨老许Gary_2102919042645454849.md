---
key: 【Qwen_Image_2.1】文生图_官方PE丨老许Gary_2102919042645454849.json
name: 【Qwen_Image_2.1】文生图_官方PE丨老许Gary_2102919042645454849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Qwen_Image_2.1】文生图_官方PE丨老许Gary_2102919042645454849.json
hash: 7ba7f3343e91b677
coverage: 0.6875
learned_at: 2026-10-10 20:59:30
nodes: [TextEncodeQwenImage21, KSampler, UNETLoader, CLIPLoader, VAELoader, SaveImage, CLIPLoader, EmptyLatentImage, TextGenerate, VAEDecode, PreviewImage, ResolutionSelector, PreviewAny, MarkdownNote, CR Prompt Text, CR Prompt Text]
patterns: []
missing: [CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 710732336843834, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 【Qwen_Image_2.1】文生图_官方PE丨老许Gary_2102919042645454849.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Qwen_Image_2.1】文生图_官方PE丨老许Gary_2102919042645454849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `TextGenerate`
- `VAEDecode` ★核心
- `PreviewImage`
- `ResolutionSelector`
- `PreviewAny`
- `MarkdownNote`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `710732336843834`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（11/16）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`EmptyLatentImage`、`TextGenerate`、`VAEDecode`、`ResolutionSelector`

**缺卡**（2）：`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
