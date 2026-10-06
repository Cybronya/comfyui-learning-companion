---
key: 图片生成/图生图/Qwen Image 2.1 透明图层抠图    手动标记改图专属工作流_2107175001689513986.json
name: Qwen Image 2.1 透明图层抠图    手动标记改图专属工作流_2107175001689513986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 透明图层抠图    手动标记改图专属工作流_2107175001689513986.json
hash: 9cef4429cb7f1874
coverage: 0.826087
learned_at: 2026-10-07 02:41:23
nodes: [PathchSageAttentionKJ, QwenImage21Cache, ModelAttentionBackend, TextEncodeQwenImage21, LoadImage, LoadImage, MarkdownNote, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SaveImageAdvanced, LoadImage, KSampler, VAELoader, VAEDecode, SaveImage, CR Prompt Text, PixaromaLabel, PixaromaLabel, PixaromaLabel, PixaromaLabel, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 150905874367980, "steps": 40}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen Image 2.1 透明图层抠图    手动标记改图专属工作流_2107175001689513986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 透明图层抠图    手动标记改图专属工作流_2107175001689513986.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SaveImageAdvanced`
- `LoadImage`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `CR Prompt Text`
- `PixaromaLabel`
- `PixaromaLabel`
- `PixaromaLabel`
- `PixaromaLabel`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `150905874367980`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`PathchSageAttentionKJ`、`QwenImage21Cache`、`ModelAttentionBackend`、`TextEncodeQwenImage21`、`LoadImage`、`CLIPLoader`、`SaveImageAdvanced`、`KSampler`、`VAELoader`、`VAEDecode`、`SaveImage`、`PixaromaLabel`、`UNETLoader`、`LoraLoaderModelOnly`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
