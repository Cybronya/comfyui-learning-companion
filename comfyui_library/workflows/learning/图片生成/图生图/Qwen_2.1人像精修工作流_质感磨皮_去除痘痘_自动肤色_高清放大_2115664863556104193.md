---
key: 图片生成/图生图/Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115664863556104193.json
name: Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115664863556104193
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115664863556104193.json
hash: 467da5f6bc412663
coverage: 0.802817
learned_at: 2026-10-30 17:51:12
nodes: [CLIPLoader, VAELoader, UNETLoader, TextEncodeQwenImage21, KSampler, QwenImage21Cache, SaveImageAdvanced, SeedVR2LoadVAEModel, Get Image Size, ImageScaleBy, easy imageScaleToNormPixels, GetImageSize+, CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, VAEDecode, KSamplerAdvanced, easy cleanGpuUsed, SaveImage, GetNode, CLIPLoader, UNETLoader, VAEEncode, VAELoader, easy cleanGpuUsed, SetNode, LoraLoaderModelOnly, GetNode, VAEDecode, SetNode, 孤海-浮点滑条, ComfySwitchNode, ImageScale, easy promptConcat, easy getNode, easy promptConcat, easy getNode, CR Prompt Text, easy textIndexSwitch, easy setNode, easy textIndexSwitch, easy setNode, CR Prompt Text, INTConstant, easy textIndexSwitch, PreviewAny, easy getNode, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, TTP_Image_Assy, 数学运算_孤海, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, easy showAnything, easy showAnything, ImageResize+, SetNode, EmptyLatentImage, CR Prompt Text, easy setNode, GetNode, GetNode, GetImageSize, easy int, SetNode, SetNode, CR Prompt Text, SetNode, LoadImage, RH_LLMAPI_NODE]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "beta57", "height": 1024, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1024}
---

# 图片生成/图生图/Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115664863556104193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_2.1人像精修工作流_质感磨皮_去除痘痘_自动肤色_高清放大_2115664863556104193.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `SeedVR2LoadVAEModel`
- `Get Image Size`
- `ImageScaleBy`
- `easy imageScaleToNormPixels`
- `GetImageSize+`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `GetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `easy cleanGpuUsed`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `孤海-浮点滑条`
- `ComfySwitchNode`
- `ImageScale`
- `easy promptConcat`
- `easy getNode`
- `easy promptConcat`
- `easy getNode`
- `CR Prompt Text`
- `easy textIndexSwitch`
- `easy setNode`
- `easy textIndexSwitch`
- `easy setNode`
- `CR Prompt Text`
- `INTConstant`
- `easy textIndexSwitch`
- `PreviewAny`
- `easy getNode`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `数学运算_孤海`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `easy showAnything`
- `easy showAnything`
- `ImageResize+`
- `SetNode`
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `easy setNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `easy int`
- `SetNode`
- `SetNode`
- `CR Prompt Text`
- `SetNode`
- `LoadImage`
- `RH_LLMAPI_NODE`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta57`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（57/71）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`KSampler`、`QwenImage21Cache`、`SaveImageAdvanced`、`SeedVR2LoadVAEModel`、`Get Image Size`、`ImageScaleBy`、`easy imageScaleToNormPixels`、`GetImageSize+`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`VAEDecode`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`SaveImage`、`VAEEncode`、`LoraLoaderModelOnly`、`孤海-浮点滑条`、`ImageScale`、`easy promptConcat`、`easy getNode`、`CR Prompt Text`、`easy textIndexSwitch`、`easy setNode`、`INTConstant`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`数学运算_孤海`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageResize+`、`EmptyLatentImage`、`GetImageSize`、`easy int`、`LoadImage`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage
