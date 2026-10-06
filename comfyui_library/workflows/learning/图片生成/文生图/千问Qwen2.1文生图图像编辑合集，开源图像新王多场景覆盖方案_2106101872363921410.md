---
key: 图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json
name: 千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json
hash: bbb51dc1a6418ea1
coverage: 0.618421
learned_at: 2026-10-06 21:51:51
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, EmptyLatentImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, ImageResize+, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SaveImage, easy imageSize, GetNode, Any Switch (rgthree), Image Comparer (rgthree), ComfySwitchNode, GetNode, ImageScaleBy, KSampler, UNETLoader, SetNode, ResolutionSelector, SetNode, VAEDecode, SaveImage, Image Comparer (rgthree), TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), VAELoader, TextEncodeQwenImage21, CLIPLoader, EmptyLatentImage, KSampler, SaveImage, VAEDecode, Int, UNETLoader, PrimitiveStringMultiline, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Fast Groups Bypasser (rgthree), ImageScaleBy, ImageScaleBy, Int, TTP_Image_Assy, TTP_Image_Tile_Batch, ImageResize+, ImageResize+, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Tile_image_size, easy imageSize, easy imageSize, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识, 次要节点 `Int` 知识库中没有该节点类型的任何知识, 次要节点 `TTP_Image_Assy` 知识库中没有该节点类型的任何知识, 次要节点 `TTP_Image_Tile_Batch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `TTP_Tile_image_size` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问Qwen2.1文生图图像编辑合集，开源图像新王多场景覆盖方案_2106101872363921410.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
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
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `VAEDecode` ★核心
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
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Int`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`
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

覆盖率 **62%**（47/76）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`UNETLoader`、`ResolutionSelector`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（15）：`Fast Groups Bypasser (rgthree)`、`ImageScaleBy`、`ImageScaleBy`、`Int`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`ImageResize+`、`ImageResize+`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TTP_Tile_image_size`、`easy imageSize`、`easy imageSize`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识
- 次要节点 `Int` 知识库中没有该节点类型的任何知识
- 次要节点 `TTP_Image_Assy` 知识库中没有该节点类型的任何知识
- 次要节点 `TTP_Image_Tile_Batch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `TTP_Tile_image_size` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
