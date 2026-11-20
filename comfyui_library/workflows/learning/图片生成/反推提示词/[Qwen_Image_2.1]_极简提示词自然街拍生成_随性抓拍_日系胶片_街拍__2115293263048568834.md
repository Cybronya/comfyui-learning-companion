---
key: 图片生成/反推提示词/[Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2115293263048568834.json
name: [Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2115293263048568834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/[Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2115293263048568834.json
hash: fc2937ef8ebfd71a
coverage: 0.761905
learned_at: 2026-10-30 17:49:08
nodes: [EmptyLatentImage, Seed (rgthree), ResolutionSelector, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, CLIPLoader, CLIPLoader, CLIPLoader, VAEDecode, Text, RHLLMChatNode, PreviewAny, TextEncodeQwenImage21, KSampler, SaveImage, PreviewImage, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 662800525719862, "steps": 40, "width": 1024}
---

# 图片生成/反推提示词/[Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2115293263048568834.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/[Qwen_Image_2.1]_极简提示词自然街拍生成_随性抓拍_日系胶片_街拍__2115293263048568834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Text`
- `RHLLMChatNode`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `662800525719862`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`EmptyLatentImage`、`Seed (rgthree)`、`ResolutionSelector`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`Text`、`RHLLMChatNode`、`TextEncodeQwenImage21`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
