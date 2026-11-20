---
name: unknown_workflow_upscale_lora_sampler_48
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7078
common_nodes: [CLIPLoader, ComfyMathExpression, GetImageSize, GetNode, Image Comparer (rgthree), Image Remove Alpha JK, ImagePadForOutpaint, ImageScaleToMaxDimension, ImageUpscaleWithModel, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewImage, QwenImage21Cache, SamplerCustom, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy int, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Repair and Enlarge修复放大+qwen_image_2.1_turbo_2114160830857179137.json, 平台全量/修复放大 qwen_image_2.1_turbo_2113196563131617281.json, 平台全量/无损放大 qwen_image_2.1_2109578396257841154.json, 视频生成/图生视频/Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115302133112328194.json, 视频生成/图生视频/Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115311006116302850.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Repair and Enlarge修复放大+qwen_image_2.1_turbo_2114160830857179137.json、平台全量/修复放大 qwen_image_2.1_turbo_2113196563131617281.json、平台全量/无损放大 qwen_image_2.1_2109578396257841154.json、视频生成/图生视频/Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115302133112328194.json、视频生成/图生视频/Repair_and_Enlarge修复放大+qwen_image_2.1_turbo_2115311006116302850.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `Image Remove Alpha JK`
- `ImagePadForOutpaint`
- `ImageScaleToMaxDimension`
- `ImageUpscaleWithModel`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `QwenImage21Cache`
- `SamplerCustom`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 3/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/5 个有
- `easy imageInsetCrop` —— 3/5 个有
- `Bounded Image Crop` —— 2/5 个有
- `Image Bounds` —— 2/5 个有
- `Inset Image Bounds` —— 2/5 个有
- `忽略多组孤海` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
