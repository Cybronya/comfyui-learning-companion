---
key: 图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json
name: Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json
hash: 1fa6c1ce49c22fa7
coverage: 0.909091
learned_at: 2026-10-19 23:41:57
nodes: [EmptyLatentImage, ConditioningZeroOut, VAELoader, VAEDecode, UNETLoader, Note, CLIPLoader, CLIPTextEncode, KSampler, SaveImage, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "height": 1920, "width": 1080}
discoveries: ["参数体检失败: '>' not supported between instances of 'str' and 'int'"]
---

# 图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `Note`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`EmptyLatentImage`、`ConditioningZeroOut`、`VAELoader`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 学习发现

- 参数体检失败: '>' not supported between instances of 'str' and 'int'
