---
key: 图片生成/图生图/Qwen2.1人像写真宫格图组图故事板分镜 多姿态批量出图方案_2109002353771892738.json
name: Qwen2.1人像写真宫格图组图故事板分镜 多姿态批量出图方案_2109002353771892738
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1人像写真宫格图组图故事板分镜 多姿态批量出图方案_2109002353771892738.json
hash: 28622e5a796de570
coverage: 0.835294
learned_at: 2026-10-23 11:19:07
nodes: [ProcessString, llama_cpp_instruct_adv, ComfySwitchNode, CLIPLoader, SeedVR2Conditioning, VAELoader, INTConstant, ComfySwitchNode, HfImageToRGB, VAEEncodeTiled, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, VAEDecode, llama_cpp_parameters, JDCN_StringToList, LoraLoaderModelOnly, ShunjingAIShade, EmptyLatentImage, PrimitiveInt, SeedVR2Preprocess, DapaoBatchImageGrid, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, UNETLoader, VAEDecodeTiled, llama_cpp_model_loader, LayerUtility: PurgeVRAM V2, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: PurgeVRAM V2, EmptyLatentImage, LoadImage, KSampler, UNETLoader, QwenImage21Cache, VAELoader, KSampler, VAEDecode, SaveImage, SaveImage, easy showAnything, CR Text Concatenate, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, LoadImage, RHHiddenNodes, TextEncodeQwenImage21, TextEncodeQwenImage21, RHHiddenNodes, PrimitiveStringMultiline, 图像缩放V2_孤海, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1人像写真宫格图组图故事板分镜 多姿态批量出图方案_2109002353771892738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1人像写真宫格图组图故事板分镜 多姿态批量出图方案_2109002353771892738.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `ProcessString`
- `llama_cpp_instruct_adv`
- `ComfySwitchNode`
- `CLIPLoader`
- `SeedVR2Conditioning`
- `VAELoader`
- `INTConstant`
- `ComfySwitchNode`
- `HfImageToRGB`
- `VAEEncodeTiled` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `llama_cpp_parameters`
- `JDCN_StringToList`
- `LoraLoaderModelOnly` ★核心
- `ShunjingAIShade`
- `EmptyLatentImage` ★核心
- `PrimitiveInt`
- `SeedVR2Preprocess`
- `DapaoBatchImageGrid`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `UNETLoader` ★核心
- `VAEDecodeTiled` ★核心
- `llama_cpp_model_loader`
- `LayerUtility: PurgeVRAM V2`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM V2`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `easy showAnything`
- `CR Text Concatenate`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `RHHiddenNodes`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `RHHiddenNodes`
- `PrimitiveStringMultiline`
- `图像缩放V2_孤海`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **84%**（71/85）

**有卡**：`ProcessString`、`llama_cpp_instruct_adv`、`CLIPLoader`、`SeedVR2Conditioning`、`VAELoader`、`INTConstant`、`HfImageToRGB`、`VAEEncodeTiled`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`VAEDecode`、`llama_cpp_parameters`、`JDCN_StringToList`、`ShunjingAIShade`、`EmptyLatentImage`、`SeedVR2Preprocess`、`DapaoBatchImageGrid`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropByMask V2`、`UNETLoader`、`VAEDecodeTiled`、`llama_cpp_model_loader`、`LayerUtility: PurgeVRAM V2`、`KSampler`、`LoadImage`、`QwenImage21Cache`、`SaveImage`、`CR Text Concatenate`、`RHHiddenNodes`、`TextEncodeQwenImage21`、`图像缩放V2_孤海`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
