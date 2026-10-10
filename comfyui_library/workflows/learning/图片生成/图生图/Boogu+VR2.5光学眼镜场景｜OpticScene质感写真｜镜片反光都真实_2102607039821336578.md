---
key: 图片生成/图生图/Boogu+VR2.5光学眼镜场景｜OpticScene质感写真｜镜片反光都真实_2102607039821336578.json
name: Boogu+VR2.5光学眼镜场景｜OpticScene质感写真｜镜片反光都真实_2102607039821336578
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Boogu+VR2.5光学眼镜场景｜OpticScene质感写真｜镜片反光都真实_2102607039821336578.json
hash: 642386051e14ac31
coverage: 0.90625
learned_at: 2026-10-10 20:48:02
nodes: [VAELoader, SamplerCustom, DF_Get_image_size, ImageScaleToTotalPixels, KSamplerSelect, ModelSamplingAuraFlow, BasicScheduler, SeedVR2LoadDiTModel, TextEncodeBooguEdit, UNETLoader, CLIPLoader, LoraLoaderModelOnly, SaveImage, SeedVR2LoadVAEModel, LoadImage, EmptyLatentImage, CR Prompt Text, SaveImage, VAEDecode, SeedVR2VideoUpscaler, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Boogu+VR2.5光学眼镜场景｜OpticScene质感写真｜镜片反光都真实_2102607039821336578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Boogu+VR2.5光学眼镜场景｜OpticScene质感写真｜镜片反光都真实_2102607039821336578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `VAELoader`
- `SamplerCustom` ★核心
- `DF_Get_image_size`
- `ImageScaleToTotalPixels`
- `KSamplerSelect` ★核心
- `ModelSamplingAuraFlow`
- `BasicScheduler`
- `SeedVR2LoadDiTModel`
- `TextEncodeBooguEdit`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `SaveImage`
- `VAEDecode` ★核心
- `SeedVR2VideoUpscaler`
- `PrimitiveInt`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **91%**（58/64）

**有卡**：`VAELoader`、`SamplerCustom`、`DF_Get_image_size`、`ImageScaleToTotalPixels`、`KSamplerSelect`、`ModelSamplingAuraFlow`、`BasicScheduler`、`SeedVR2LoadDiTModel`、`TextEncodeBooguEdit`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`SaveImage`、`SeedVR2LoadVAEModel`、`LoadImage`、`EmptyLatentImage`、`VAEDecode`、`SeedVR2VideoUpscaler`、`CLIPTextEncode`、`KSampler`、`solarL_SaveImagesToZip`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
