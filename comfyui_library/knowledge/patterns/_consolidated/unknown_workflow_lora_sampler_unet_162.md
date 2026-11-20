---
name: unknown_workflow_lora_sampler_unet_162
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7162
common_nodes: [CFGGuider, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2114888581553672194.json, 图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2115616178910617601.json, 图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2115664213535449090.json, 图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json, 图片生成/文生图/Moss + QwenImage2.1 文生+图片编辑_2112165438787510273.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_162

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2114888581553672194.json、图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2115616178910617601.json、图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2115664213535449090.json、图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json、图片生成/文生图/Moss + QwenImage2.1 文生+图片编辑_2112165438787510273.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 4/5 个有
- `CLIPTextEncode` —— 4/5 个有
- `JsonExtractString` —— 4/5 个有
- `SkipLayerGuidanceDiTSimple` —— 4/5 个有
- `easy isNone` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `BatchImagesNode` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `QwenImage21Cache` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
