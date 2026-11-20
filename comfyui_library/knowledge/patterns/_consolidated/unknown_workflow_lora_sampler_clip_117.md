---
name: unknown_workflow_lora_sampler_clip_117
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.320167
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ColorMatchV2, ComfyMathExpression, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, FluxKVCache, GetImageSize, GetNode, Image Comparer (rgthree), ImageMergeTileList, ImageScale, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, PrimitiveFloat, PrimitiveInt, ReferenceLatent, SamplerCustom, SaveImage, SetNode, SplitImageToTileList, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/细节不清晰重塑、放大-Klein 9B_2066683823601049601.json, 图片生成/图生图/细节不清晰重塑、放大-Klein_9B_2095767647412645890.json, 图片生成/图生图/细节不清晰重塑、放大-Klein_9B_2096061805943672833.json, 平台全量/Flux.2 Klein 9B-KV Tile Upscale：无需 ControlNet 的任意尺_2066503754844823553.json, 平台全量/利用图像混合 Image Blend 保留原图细节与一致性（分块放大工作流补充说明）_2067954834472525826.json, 平台全量/如何保留原图细节（颜色匹配 Color Match）_2067221150647799809.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_117

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/细节不清晰重塑、放大-Klein 9B_2066683823601049601.json、图片生成/图生图/细节不清晰重塑、放大-Klein_9B_2095767647412645890.json、图片生成/图生图/细节不清晰重塑、放大-Klein_9B_2096061805943672833.json、平台全量/Flux.2 Klein 9B-KV Tile Upscale：无需 ControlNet 的任意尺_2066503754844823553.json、平台全量/利用图像混合 Image Blend 保留原图细节与一致性（分块放大工作流补充说明）_2067954834472525826.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：32%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxKVCache`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageMergeTileList`
- `ImageScale`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ReferenceLatent`
- `SamplerCustom`
- `SaveImage`
- `SetNode`
- `SplitImageToTileList`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/6 个有
- `ResizeImageMaskNode` —— 2/6 个有
- `easy imageColorMatch` —— 2/6 个有
- `ImageBlend` —— 1/6 个有
- `ImageSharpen` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
