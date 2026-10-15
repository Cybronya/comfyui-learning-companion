---
key: 图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json
name: （贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json
hash: fe703fb0d0e8bd84
coverage: 0.763158
learned_at: 2026-10-10 21:23:19
nodes: [Note, CLIPLoader, VAELoader, Note, ResolutionSelector, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Note, VAEDecode, CR Prompt Text, QwenImage21SageAttentionT8, ConcatTextOfUtils, TextEncodeQwenImage21, LoadImage, CR Prompt Text, UNETLoader, EmptyLatentImage, SaveImage, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, SaveImage, easy cleanGpuUsed, LoadImage, KSampler, LoadImage, SaveImage, SaveImage, SaveImage, QwenPERewriteT8, easy showAnything, CR Prompt Text]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json`

## 结构

**节点**（38 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `ResolutionSelector`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `VAEDecode`
- `CR Prompt Text`
- `QwenImage21SageAttentionT8`
- `ConcatTextOfUtils`
- `TextEncodeQwenImage21`
- `LoadImage`
- `CR Prompt Text`
- `UNETLoader`
- `EmptyLatentImage`
- `SaveImage`
- `LoraLoaderModelOnly`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `SaveImage`
- `easy cleanGpuUsed`
- `LoadImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `QwenPERewriteT8`
- `easy showAnything`
- `CR Prompt Text`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `19960422`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **76%**（29/38）

**有卡**：`Note`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`ComfySwitchNode`、`LoadImage`、`VAEDecode`、`CR Prompt Text`、`QwenImage21SageAttentionT8`、`ConcatTextOfUtils`、`TextEncodeQwenImage21`、`UNETLoader`、`EmptyLatentImage`、`SaveImage`、`LoraLoaderModelOnly`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`easy cleanGpuUsed`

**缺卡**（4）：`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
