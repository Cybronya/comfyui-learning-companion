---
key: 平台全量/3-效果炸裂 合规使用！QwenImage2.1换脸换头换人 精准万物迁移工作流-V1_2105196366719963137.json
name: 3-效果炸裂 合规使用！QwenImage2.1换脸换头换人 精准万物迁移工作流-V1_2105196366719963137
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/3-效果炸裂 合规使用！QwenImage2.1换脸换头换人 精准万物迁移工作流-V1_2105196366719963137.json
hash: e2ffb7ffaec57fbe
coverage: 0.529412
learned_at: 2026-11-14 00:11:44
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, EmptyLatentImage, GetNode, SetNode, Any Switch (rgthree), SetNode, SetNode, SetNode, SAM3_Detect, GrowMaskWithBlur, ShowText|pysssss, KSampler, CheckpointLoaderSimple, AILab_MaskExtractor, Seed (rgthree), ComfySwitchNode, Image Comparer (rgthree), GetNode, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, GetNode, Fast Groups Bypasser (rgthree), QwenImage21Cache, MarkdownNote, CLIPLoader, UNETLoader, VAELoader, GetNode, SetNode, GetNode, LoraLoaderModelOnly, PrimitiveStringMultiline, Note, CLIPTextEncode, LoadAndResizeImage, VOSR2ModelLoader, VOSR2Upscale, Image Comparer (rgthree), easy cleanGpuUsed, SeedVR2Conditioning, UNETLoader, VAELoader, SeedVR2Preprocess, SeedVR2PostProcessing, VAEEncodeTiled, KSampler, Image Comparer (rgthree), SaveImage, VAEDecodeTiled, ResizeImageMaskNode, SaveImage, Fast Groups Bypasser (rgthree), SetNode, LoadAndResizeImage, GetNode, GetNode, TextEncodeQwenImage21, PreviewImage, SetNode, GetNode, VAEDecode, SaveImage, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 1088, "sampler_name": "euler", "scheduler": "simple", "seed": 9527, "steps": 1, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/3-效果炸裂 合规使用！QwenImage2.1换脸换头换人 精准万物迁移工作流-V1_2105196366719963137.json

> 来源文件 `comfyui_library/workflows/平台全量/3-效果炸裂 合规使用！QwenImage2.1换脸换头换人 精准万物迁移工作流-V1_2105196366719963137.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SAM3_Detect`
- `GrowMaskWithBlur`
- `ShowText|pysssss`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `AILab_MaskExtractor`
- `Seed (rgthree)`
- `ComfySwitchNode`
- `Image Comparer (rgthree)`
- `GetNode`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `QwenImage21Cache`
- `MarkdownNote`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadAndResizeImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `SeedVR2Conditioning`
- `UNETLoader` ★核心
- `VAELoader`
- `SeedVR2Preprocess`
- `SeedVR2PostProcessing`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecodeTiled` ★核心
- `ResizeImageMaskNode`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `LoadAndResizeImage`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1088`
- `batch_size` = `1`
- `seed` = `9527`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **53%**（36/68）

**有卡**：`EmptyLatentImage`、`SAM3_Detect`、`GrowMaskWithBlur`、`KSampler`、`CheckpointLoaderSimple`、`AILab_MaskExtractor`、`Seed (rgthree)`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`QwenImage21Cache`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadAndResizeImage`、`VOSR2ModelLoader`、`VOSR2Upscale`、`easy cleanGpuUsed`、`SeedVR2Conditioning`、`SeedVR2Preprocess`、`SeedVR2PostProcessing`、`VAEEncodeTiled`、`SaveImage`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`TextEncodeQwenImage21`、`VAEDecode`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
