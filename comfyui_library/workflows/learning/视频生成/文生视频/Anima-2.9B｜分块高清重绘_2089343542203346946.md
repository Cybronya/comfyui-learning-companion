---
key: 视频生成/文生视频/Anima-2.9B｜分块高清重绘_2089343542203346946.json
name: Anima-2.9B｜分块高清重绘_2089343542203346946
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Anima-2.9B｜分块高清重绘_2089343542203346946.json
hash: 02969aee9e0007fb
coverage: 0.703704
learned_at: 2026-10-11 21:19:37
nodes: [Reroute, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleToTotalPixels, UNETLoader, PathchSageAttentionKJ, CLIPLoader, VAELoaderKJ, Image Comparer (rgthree), KepStringLiteral, Reroute, TTP_Image_Tile_Batch, easy imageListToImageBatch, TTP_Image_Assy, TTP_Tile_image_size, easy imageBatchToImageList, VAEDecodeTiled, SaveImage, WD14Tagger|pysssss, ShowText|pysssss, JWStringConcat, VAEEncode, CLIPTextEncode, CLIPTextEncode, Image Comparer (rgthree), KSampler, LoadImage]
patterns: [image_to_image]
missing: [WD14Tagger|pysssss, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 0.20000000000000004, "sampler_name": "res_multistep", "scheduler": "linear_quadratic", "seed": 440806743335793, "steps": 28}
discoveries: [次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/Anima-2.9B｜分块高清重绘_2089343542203346946.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Anima-2.9B｜分块高清重绘_2089343542203346946.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Reroute`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoaderKJ`
- `Image Comparer (rgthree)`
- `KepStringLiteral`
- `Reroute`
- `TTP_Image_Tile_Batch`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `WD14Tagger|pysssss`
- `ShowText|pysssss`
- `JWStringConcat`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `440806743335793`
- `steps` = `28`
- `cfg` = `5`
- `sampler_name` = `res_multistep`
- `scheduler` = `linear_quadratic`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoaderKJ`、`KepStringLiteral`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`VAEDecodeTiled`、`SaveImage`、`JWStringConcat`、`VAEEncode`、`CLIPTextEncode`、`KSampler`、`LoadImage`

**缺卡**（3）：`WD14Tagger|pysssss`、`easy imageBatchToImageList`、`easy imageListToImageBatch`

**用到的条目**：KSampler、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled、VAEEncode、VAELoaderKJ

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
