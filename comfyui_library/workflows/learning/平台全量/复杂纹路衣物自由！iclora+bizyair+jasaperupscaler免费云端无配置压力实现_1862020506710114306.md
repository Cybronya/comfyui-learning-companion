---
key: 平台全量/复杂纹路衣物自由！iclora+bizyair+jasaperupscaler免费云端无配置压力实现_1862020506710114306.json
name: 复杂纹路衣物自由！iclora+bizyair+jasaperupscaler免费云端无配置压力实现_1862020506710114306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/复杂纹路衣物自由！iclora+bizyair+jasaperupscaler免费云端无配置压力实现_1862020506710114306.json
hash: dea78b359a455ef3
coverage: 0.87931
learned_at: 2026-11-14 01:57:15
nodes: [Replace Text _O, Text _O, ImageConcanate, Text _O, Replace Text _O, ImageConcanate, EmptyImage, easy compare, Text _O, TextInput_, RH_Captioner, ShowText|pysssss, ImageResizeKJ, ImageResizeKJ, Replace Text _O, Create Rect Mask, Create Rect Mask, LoadImage, PreviewImage, PreviewImage, Image To Mask, VAEEncodeForInpaint, VAEEncodeForInpaint, Image To Mask, ShowText|pysssss, GetImageSize+, DualCLIPLoader, UNETLoader, LoraLoader, LoraLoader, BasicGuider, BasicScheduler, RandomNoise, KSamplerSelect, Latent Input Switch, SamplerCustomAdvanced, PreviewImage, VAELoader, CLIPTextEncode, ControlNetLoader, ControlNetApplySD3, ImageResizeKJ, Create Rect Mask, Create Rect Mask, BasicGuider, easy imageSwitch, Image To Mask, PreviewImage, KSamplerSelect, ConditioningZeroOut, BasicScheduler, SamplerCustomAdvanced, VAEEncodeForInpaint, Image Comparer (rgthree), VAEDecode, SaveImage, VAEDecode, SaveImage]
patterns: [lora]
missing: []
parameters: {"controlnet_strength": 1, "lora_name": "(时尚写真) Pho Realistic-FLUX_V1.0.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/复杂纹路衣物自由！iclora+bizyair+jasaperupscaler免费云端无配置压力实现_1862020506710114306.json

> 来源文件 `comfyui_library/workflows/平台全量/复杂纹路衣物自由！iclora+bizyair+jasaperupscaler免费云端无配置压力实现_1862020506710114306.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `Replace Text _O`
- `Text _O`
- `ImageConcanate`
- `Text _O`
- `Replace Text _O`
- `ImageConcanate`
- `EmptyImage`
- `easy compare`
- `Text _O`
- `TextInput_`
- `RH_Captioner`
- `ShowText|pysssss`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `Replace Text _O`
- `Create Rect Mask`
- `Create Rect Mask`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `Image To Mask`
- `VAEEncodeForInpaint` ★核心
- `VAEEncodeForInpaint` ★核心
- `Image To Mask`
- `ShowText|pysssss`
- `GetImageSize+`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `BasicGuider`
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Latent Input Switch`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `ControlNetApplySD3` ★核心
- `ImageResizeKJ`
- `Create Rect Mask`
- `Create Rect Mask`
- `BasicGuider`
- `easy imageSwitch`
- `Image To Mask`
- `PreviewImage`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEEncodeForInpaint` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `(时尚写真) Pho Realistic-FLUX_V1.0.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **88%**（51/58）

**有卡**：`Replace Text _O`、`Text _O`、`ImageConcanate`、`EmptyImage`、`easy compare`、`TextInput_`、`RH_Captioner`、`ImageResizeKJ`、`Create Rect Mask`、`LoadImage`、`Image To Mask`、`VAEEncodeForInpaint`、`GetImageSize+`、`DualCLIPLoader`、`UNETLoader`、`LoraLoader`、`BasicGuider`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`Latent Input Switch`、`SamplerCustomAdvanced`、`VAELoader`、`CLIPTextEncode`、`ControlNetLoader`、`ControlNetApplySD3`、`easy imageSwitch`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、ControlNetApplySD3、ControlNetLoader
