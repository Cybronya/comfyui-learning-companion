---
key: 视频生成/文生视频/wan2.2文生视频丝滑二次元-无限生成-动作流畅-冲击力_2030710747524767745.json
name: wan2.2文生视频丝滑二次元-无限生成-动作流畅-冲击力_2030710747524767745
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频丝滑二次元-无限生成-动作流畅-冲击力_2030710747524767745.json
hash: 119ac9a0b6c10763
coverage: 0.835821
learned_at: 2026-10-15 22:47:36
nodes: [SaveImage, UnetLoaderGGUF, UnetLoaderGGUF, MarkdownNote, VAEDecodeTiled, CLIPTextEncode, LoraLoader, MarkdownNote, VAELoader, LoadImage, ImageAddNoise, LoraLoader, MarkdownNote, easy cleanGpuUsed, MarkdownNote, CLIPSetLastLayer, LoraLoader, LoraLoader, MarkdownNote, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, MarkdownNote, MarkdownNote, CLIPTextEncode, MarkdownNote, WanImageToVideo, EmptyLatentImage, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, CheckpointLoaderSimple, LoraLoader, RIFE VFI, VHS_VideoCombine, UNETLoader, UNETLoader, VAEDecodeTiled, CreateVideo, TT_img_enc_v2, UpscaleImageByUsingModel, SaveVideo, RIFE VFI, SaveImage, MarkdownNote, UpscaleModelLoader, TT_img_enc_v2, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, KSampler, CLIPTextEncode, MarkdownNote, SaveImage, CLIPTextEncode, easy promptConcat, KSampler, KSamplerAdvanced, KSamplerAdvanced, Int, Int, MathExpression|pysssss, Int, RH_Translator, Text, RH_Translator]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "smoothMixIllustrious_illustriousV5.safetensors", "denoise": "simple", "height": 1536, "lora_name": "Smooth_Booster_v2_illustrious.safetensors", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "strength_clip": 1, "strength_model": 0.5, "width": 1024}
---

# 视频生成/文生视频/wan2.2文生视频丝滑二次元-无限生成-动作流畅-冲击力_2030710747524767745.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频丝滑二次元-无限生成-动作流畅-冲击力_2030710747524767745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `SaveImage`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `MarkdownNote`
- `VAELoader`
- `LoadImage`
- `ImageAddNoise`
- `LoraLoader` ★核心
- `MarkdownNote`
- `easy cleanGpuUsed`
- `MarkdownNote`
- `CLIPSetLastLayer`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `MarkdownNote`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `WanImageToVideo`
- `EmptyLatentImage` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `TT_img_enc_v2`
- `UpscaleImageByUsingModel`
- `SaveVideo`
- `RIFE VFI`
- `SaveImage`
- `MarkdownNote`
- `UpscaleModelLoader`
- `TT_img_enc_v2`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `easy promptConcat`
- `KSampler` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Int`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `RH_Translator`
- `Text`
- `RH_Translator`

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `Smooth_Booster_v2_illustrious.safetensors`
- `strength_model` = `0.5`
- `strength_clip` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `smoothMixIllustrious_illustriousV5.safetensors`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（56/67）

**有卡**：`SaveImage`、`UnetLoaderGGUF`、`VAEDecodeTiled`、`CLIPTextEncode`、`LoraLoader`、`VAELoader`、`LoadImage`、`ImageAddNoise`、`easy cleanGpuUsed`、`CLIPSetLastLayer`、`VAEDecode`、`WanImageToVideo`、`EmptyLatentImage`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`RIFE VFI`、`VHS_VideoCombine`、`UNETLoader`、`CreateVideo`、`TT_img_enc_v2`、`UpscaleImageByUsingModel`、`SaveVideo`、`UpscaleModelLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`KSampler`、`easy promptConcat`、`KSamplerAdvanced`、`Int`、`MathExpression|pysssss`、`RH_Translator`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader
