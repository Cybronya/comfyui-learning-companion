---
key: 图片生成/图生图/Qwen_image2.1角色设定卡，1分钟出图！！！_2114261529620213762.json
name: Qwen_image2.1角色设定卡，1分钟出图！！！_2114261529620213762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image2.1角色设定卡，1分钟出图！！！_2114261529620213762.json
hash: f22ff265d807d880
coverage: 0.73913
learned_at: 2026-10-26 22:03:35
nodes: [EmptyLatentImage, VAELoader, VAEDecode, LoadImage, ResolutionSelector, llama_cpp_model_loader, LayerUtility: TextJoin, llama_cpp_parameters, PrimitiveStringMultiline, PrimitiveStringMultiline, TextEncodeQwenImage21, PreviewAny, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), Seed (rgthree), SaveImage, PrimitiveStringMultiline, UNETLoader, CLIPLoader, LoraLoaderModelOnly, KSampler, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 200857211120213, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen_image2.1角色设定卡，1分钟出图！！！_2114261529620213762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image2.1角色设定卡，1分钟出图！！！_2114261529620213762.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `EmptyLatentImage` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `LoadImage`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `LayerUtility: TextJoin`
- `llama_cpp_parameters`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `Seed (rgthree)`
- `SaveImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `200857211120213`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`EmptyLatentImage`、`VAELoader`、`VAEDecode`、`LoadImage`、`ResolutionSelector`、`llama_cpp_model_loader`、`LayerUtility: TextJoin`、`llama_cpp_parameters`、`TextEncodeQwenImage21`、`llama_cpp_instruct_adv`、`Seed (rgthree)`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
