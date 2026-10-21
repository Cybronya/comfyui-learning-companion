---
key: 图片生成/文生图/image_qwen_image_2.1多合一工作流_2101894726109712385.json
name: image_qwen_image_2.1多合一工作流_2101894726109712385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image_qwen_image_2.1多合一工作流_2101894726109712385.json
hash: b5afc21843848785
coverage: 0.929825
learned_at: 2026-10-20 01:51:47
nodes: [LoadImage, MarkdownNote, llama_cpp_unload_model, ResolutionSelector, CLIPLoader, VAELoader, UNETLoader, QwenImage21Cache, EmptyLatentImage, ComfySwitchNode, KSampler, SaveImageAdvanced, LoadImage, TextEncodeQwenImage21, ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, SaveImageAdvanced, KSampler, TextEncodeQwenImage21, CLIPLoader, LoadImage, LoadImage, UNETLoader, KSampler, VAELoader, QwenImage21Cache, ComfySwitchNode, ResolutionSelector, SaveImageAdvanced, EmptyLatentImage, CLIPLoader, UNETLoader, ResolutionSelector, ShowText|pysssss, EmptyLatentImage, VAELoader, KSampler, SaveImageAdvanced, 忽略多组孤海, TextEncodeQwenImage21, LayerUtility: PurgeVRAM V2, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, TextEncodeQwenImage21, VAEDecode, VAEDecode, VAEDecode, MuyeTextEditOutput, VAEDecode, SaveImage, SaveImage, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/image_qwen_image_2.1多合一工作流_2101894726109712385.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image_qwen_image_2.1多合一工作流_2101894726109712385.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（57 个）：
- `LoadImage`
- `MarkdownNote`
- `llama_cpp_unload_model`
- `ResolutionSelector`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `LoadImage`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `忽略多组孤海`
- `TextEncodeQwenImage21`
- `LayerUtility: PurgeVRAM V2`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `MuyeTextEditOutput`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（53/57）

**有卡**：`LoadImage`、`llama_cpp_unload_model`、`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`EmptyLatentImage`、`KSampler`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`忽略多组孤海`、`LayerUtility: PurgeVRAM V2`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`VAEDecode`、`MuyeTextEditOutput`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、SaveImage
