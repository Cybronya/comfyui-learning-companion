---
key: 图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json
name: 千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json
hash: bbb51dc1a6418ea1
coverage: 0.75
learned_at: 2026-10-10 20:59:38
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, EmptyLatentImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, ImageResize+, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SaveImage, easy imageSize, GetNode, Any Switch (rgthree), Image Comparer (rgthree), ComfySwitchNode, GetNode, ImageScaleBy, KSampler, UNETLoader, SetNode, ResolutionSelector, SetNode, VAEDecode, SaveImage, Image Comparer (rgthree), TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), VAELoader, TextEncodeQwenImage21, CLIPLoader, EmptyLatentImage, KSampler, SaveImage, VAEDecode, Int, UNETLoader, PrimitiveStringMultiline, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [ImageResize+, ImageResize+, easy imageSize, easy imageSize]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json`

## 结构

**节点**（76 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `EmptyLatentImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageSize`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `ImageResize+`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `easy imageSize`
- `GetNode`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `ComfySwitchNode`
- `GetNode`
- `ImageScaleBy`
- `KSampler`
- `UNETLoader`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `VAEDecode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `Int`
- `UNETLoader`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **75%**（57/76）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`EmptyLatentImage`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy imageSize`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`ImageResize+`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SaveImage`、`GetNode`、`Any Switch (rgthree)`、`Image Comparer (rgthree)`、`ComfySwitchNode`、`KSampler`、`UNETLoader`、`SetNode`、`ResolutionSelector`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`PrimitiveStringMultiline`、`Fast Groups Bypasser (rgthree)`、`Int`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（4）：`ImageResize+`、`ImageResize+`、`easy imageSize`、`easy imageSize`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
