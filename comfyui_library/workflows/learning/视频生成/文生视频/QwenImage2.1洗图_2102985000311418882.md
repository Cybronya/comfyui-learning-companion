---
key: 视频生成/文生视频/QwenImage2.1洗图_2102985000311418882.json
name: QwenImage2.1洗图_2102985000311418882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/QwenImage2.1洗图_2102985000311418882.json
hash: ad516363f95209f8
coverage: 0.777778
learned_at: 2026-10-11 22:12:46
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImage21, JWStringConcat, easy showAnything, JWString, RHLLMChatNode, KSampler, LoadImage, VAEDecode, Image Comparer (rgthree), SaveImage]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 266040665031946, "steps": 25, "width": 1024}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/QwenImage2.1洗图_2102985000311418882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/QwenImage2.1洗图_2102985000311418882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `JWStringConcat`
- `easy showAnything`
- `JWString`
- `RHLLMChatNode`
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `266040665031946`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`GetImageSize`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`JWStringConcat`、`JWString`、`RHLLMChatNode`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`

**缺卡**（2）：`MathExpression|pysssss`、`MathExpression|pysssss`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
