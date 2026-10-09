---
key: 图片生成/图生图/Qwen image 2.1文生_编辑_抠图_透明图像_2105237147488972801.json
name: Qwen image 2.1文生_编辑_抠图_透明图像_2105237147488972801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1文生_编辑_抠图_透明图像_2105237147488972801.json
hash: 7e830f00e58ae92f
coverage: 0.785714
learned_at: 2026-10-09 22:09:17
nodes: [TextEncodeQwenImage21, ComfySwitchNode, LoadImage, LoadImage, Image Comparer (rgthree), KSampler, SaveImage, VOSR2ModelLoader, Change Channel Count, VOSR2Upscale, SaveImage, LoadImage, QwenImage21Cache, VAEDecode, QwenPERewriteT8, easy showAnything, EmptyLatentImage, Fast Groups Bypasser (rgthree), PrimitiveBoolean, PrimitiveBoolean, SaveImageAdvanced, LoadImage, ResolutionSelector, CR Text, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: [CR Text, Change Channel Count]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19940424, "steps": 50, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Change Channel Count` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen image 2.1文生_编辑_抠图_透明图像_2105237147488972801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2105237147488972801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `VOSR2ModelLoader`
- `Change Channel Count`
- `VOSR2Upscale`
- `SaveImage`
- `LoadImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `QwenPERewriteT8`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `SaveImageAdvanced`
- `LoadImage`
- `ResolutionSelector`
- `CR Text`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `19940424`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`TextEncodeQwenImage21`、`LoadImage`、`KSampler`、`SaveImage`、`VOSR2ModelLoader`、`VOSR2Upscale`、`QwenImage21Cache`、`VAEDecode`、`QwenPERewriteT8`、`EmptyLatentImage`、`PrimitiveBoolean`、`SaveImageAdvanced`、`ResolutionSelector`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`

**缺卡**（2）：`CR Text`、`Change Channel Count`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Change Channel Count` 知识库中没有该节点类型的任何知识
