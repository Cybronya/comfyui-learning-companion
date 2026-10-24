---
name: unknown_workflow_controlnet_upscale_lora_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.903
common_nodes: [AIO_Preprocessor, APersonMaskGenerator, CLIPTextEncode, CR Apply LoRA Stack, CR Apply Multi-ControlNet, CR LoRA Stack, CR Multi-ControlNet Stack, CR Simple Image Compare, CheckpointLoaderSimple, ConstrainImage|pysssss, DetailerForEachDebugPipe, GrowMaskWithBlur, ImageCompositeMasked, ImageUpscaleWithModel, ImpactSimpleDetectorSEGS, LoadImage, MaskToSEGS, PreviewImage, SAMLoader, SEGSSwitch, SaveImage, ToBasicPipe, UltralyticsDetectorProvider, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键皮肤光泽感质感增强_1894267978274242561.json, 图片生成/图生图/一键纹身工作流_1894337929311879169.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键皮肤光泽感质感增强_1894267978274242561.json、图片生成/图生图/一键纹身工作流_1894337929311879169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
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
- `AddMask` —— 1/2 个有
- `SegsToCombinedMask` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
