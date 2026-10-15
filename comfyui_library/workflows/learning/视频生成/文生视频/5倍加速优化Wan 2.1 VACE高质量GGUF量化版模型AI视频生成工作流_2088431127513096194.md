---
key: 视频生成/文生视频/5倍加速优化Wan 2.1 VACE高质量GGUF量化版模型AI视频生成工作流_2088431127513096194.json
name: 5倍加速优化Wan 2.1 VACE高质量GGUF量化版模型AI视频生成工作流_2088431127513096194
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/5倍加速优化Wan 2.1 VACE高质量GGUF量化版模型AI视频生成工作流_2088431127513096194.json
hash: ae41217652281fb3
coverage: 0.835294
learned_at: 2026-10-15 22:43:52
nodes: [Any Switch (rgthree), ModelPatchTorchSettings, PathchSageAttentionKJ, UnetLoaderGGUF, CLIPLoader, ClipLoaderGGUF, RH_Translator, easy textSwitch, CLIPTextEncode, CLIPTextEncode, SetNode, PrimitiveInt, ImageUpscaleWithModel, UpscaleModelLoader, RIFE VFI, RIFE VFI, SetNode, LoraLoaderVanilla, SaveAnimatedWEBP, VHS_VideoCombine, ModelSamplingSD3, easy clearCacheAll, easy cleanGpuUsed, GetNode, GetNode, easy clearCacheAll, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, WanVaceToVideo, easy clearCacheAll, easy clearCacheAll, KSampler, SetNode, GetNode, CR Text, VHS_LoadVideo, DisplayText_Zho, DisplayText_Zho, Fast Groups Bypasser (rgthree), VAELoader, VAEDecode, Primitive integer [Crystools], TrimVideoLatent, RH_Captioner, LoadImage, ImageResize+, VHS_VideoCombine, VHS_VideoCombine, DWPreprocessor, ImpactSwitch, VHS_VideoCombine, VRAM_Debug, VRAM_Debug, ImageResize+, Canny, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "lora_name": "Wan21_CausVid_14B_T2V_lora_rank32-1.safetensors", "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "strength_clip": 1, "strength_model": 1, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/5倍加速优化Wan 2.1 VACE高质量GGUF量化版模型AI视频生成工作流_2088431127513096194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/5倍加速优化Wan 2.1 VACE高质量GGUF量化版模型AI视频生成工作流_2088431127513096194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `Any Switch (rgthree)`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `ClipLoaderGGUF`
- `RH_Translator`
- `easy textSwitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `PrimitiveInt`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `RIFE VFI`
- `RIFE VFI`
- `SetNode`
- `LoraLoaderVanilla` ★核心
- `SaveAnimatedWEBP`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `WanVaceToVideo`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `KSampler` ★核心
- `SetNode`
- `GetNode`
- `CR Text`
- `VHS_LoadVideo`
- `DisplayText_Zho`
- `DisplayText_Zho`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `VAEDecode` ★核心
- `Primitive integer [Crystools]`
- `TrimVideoLatent`
- `RH_Captioner`
- `LoadImage`
- `ImageResize+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `VRAM_Debug`
- `ImageResize+`
- `Canny`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `lora_name` = `Wan21_CausVid_14B_T2V_lora_rank32-1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（71/85）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`CLIPLoader`、`ClipLoaderGGUF`、`RH_Translator`、`easy textSwitch`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`RIFE VFI`、`LoraLoaderVanilla`、`SaveAnimatedWEBP`、`VHS_VideoCombine`、`ModelSamplingSD3`、`easy clearCacheAll`、`easy cleanGpuUsed`、`WanVaceToVideo`、`KSampler`、`CR Text`、`VHS_LoadVideo`、`DisplayText_Zho`、`VAELoader`、`VAEDecode`、`Primitive integer [Crystools]`、`TrimVideoLatent`、`RH_Captioner`、`LoadImage`、`ImageResize+`、`DWPreprocessor`、`VRAM_Debug`、`Canny`、`LoraLoaderModelOnly`、`UNETLoader`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
