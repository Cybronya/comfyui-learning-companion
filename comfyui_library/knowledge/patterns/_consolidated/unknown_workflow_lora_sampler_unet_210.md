---
name: unknown_workflow_lora_sampler_unet_210
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.881667
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2-图像风格参考_2077246669674082306.json, 图片生成/图生图/image_krea2_turbo_int8_image_style_reference_2110364654659792898.json, 图片生成/图生图/【遇见AI】Krea2风格参考风格迁移的lora实现方法_2079861428944719874.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_210

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Krea2-图像风格参考_2077246669674082306.json、图片生成/图生图/image_krea2_turbo_int8_image_style_reference_2110364654659792898.json、图片生成/图生图/【遇见AI】Krea2风格参考风格迁移的lora实现方法_2079861428944719874.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `TextGenerate` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
