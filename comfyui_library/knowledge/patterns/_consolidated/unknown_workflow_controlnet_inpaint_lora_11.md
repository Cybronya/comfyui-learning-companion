---
name: unknown_workflow_controlnet_inpaint_lora_11
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.822
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncodeFlux, ControlNetInpaintingAliMamaApply, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, GrowMaskWithBlur, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX局部重绘工作流_1969941961505447937.json, 平台全量/Photoshop创意填充Inpaint_1875182805771866113.json, 平台全量/Turn into Venom using flux_1853031428136050689.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/FLUX局部重绘工作流_1969941961505447937.json、平台全量/Photoshop创意填充Inpaint_1875182805771866113.json、平台全量/Turn into Venom using flux_1853031428136050689.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncodeFlux`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `GrowMaskWithBlur`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageCompositeMasked` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `DF_Image_scale_to_side` —— 1/3 个有
- `Get Image Size` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `GoogleTranslateTextNode` —— 1/3 个有
- `LayerMask: PersonMaskUltra V2` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `SeargePromptText` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有
- `easy prompt` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
