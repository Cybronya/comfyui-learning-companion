---
name: unknown_workflow_controlnet_upscale_lora_7
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.901
common_nodes: [AIO_Preprocessor, APersonMaskGenerator, CLIPTextEncode, CR Apply LoRA Stack, CR Apply Multi-ControlNet, CR LoRA Stack, CR Multi-ControlNet Stack, CR Simple Image Compare, CheckpointLoaderSimple, ConstrainImage|pysssss, DetailerForEachDebugPipe, GrowMaskWithBlur, ImageCompositeMasked, ImageUpscaleWithModel, ImpactSimpleDetectorSEGS, LoadImage, MaskToSEGS, PreviewImage, SAMLoader, SEGSSwitch, SaveImage, ToBasicPipe, UltralyticsDetectorProvider, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键皮肤光泽感质感增强_1894267978274242561.json, 图片生成/图生图/一键纹身工作流_1894337929311879169.json, 平台全量/Oiled - Shiny - Sweaty_ Skin Enhance Workflow_1894204731424702466.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键皮肤光泽感质感增强_1894267978274242561.json、图片生成/图生图/一键纹身工作流_1894337929311879169.json、平台全量/Oiled - Shiny - Sweaty_ Skin Enhance Workflow_1894204731424702466.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `APersonMaskGenerator`
- `CLIPTextEncode`
- `CR Apply LoRA Stack`
- `CR Apply Multi-ControlNet`
- `CR LoRA Stack`
- `CR Multi-ControlNet Stack`
- `CR Simple Image Compare`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `DetailerForEachDebugPipe`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageUpscaleWithModel`
- `ImpactSimpleDetectorSEGS`
- `LoadImage`
- `MaskToSEGS`
- `PreviewImage`
- `SAMLoader`
- `SEGSSwitch`
- `SaveImage`
- `ToBasicPipe`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddMask` —— 1/3 个有
- `SegsToCombinedMask` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
