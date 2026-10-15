---
key: 图片生成/文生图/Qwen image2.1全能工作流_2103756014926516225.json
name: Qwen image2.1全能工作流_2103756014926516225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image2.1全能工作流_2103756014926516225.json
hash: 39b42f116154c65d
coverage: 0.561644
learned_at: 2026-10-15 22:27:07
nodes: [VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SaveImage, UNETLoader, CLIPLoader, VAELoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LoadImage, easy showAnything, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, QwenImage21Cache, TextEncodeQwenImage21, KSampler, LoadImage, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, GetNode, GetImageSize, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, CR Text, CR Text, CR Text, SetNode, LoadImage, SetNode, SetNode, GetNode, PreviewImage, CR Text, CR Text, AIO_Preprocessor, llama_cpp_parameters, LoadImage, llama_cpp_instruct_adv, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_model_loader, ki_宫格拼图简易版, PreviewImage, GetNode, Image Comparer (rgthree), CR Text Concatenate, easy showAnything, CR Text, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 901254853794380, "steps": 40, "width": 1920}
---

# 图片生成/文生图/Qwen image2.1全能工作流_2103756014926516225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image2.1全能工作流_2103756014926516225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetImageSize`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `CR Text`
- `CR Text`
- `AIO_Preprocessor`
- `llama_cpp_parameters`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `ki_宫格拼图简易版`
- `PreviewImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `CR Text Concatenate`
- `easy showAnything`
- `CR Text`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `901254853794380`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（41/73）

**有卡**：`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`GetImageSize`、`CR Text`、`AIO_Preprocessor`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`ki_宫格拼图简易版`、`CR Text Concatenate`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
