---
name: unknown_workflow_sampler_clip_unet_114
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.867
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, PreviewImage, RandomNoise, SamplerCustomAdvanced, SamplerEulerAncestral, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2512两步出图_2017532037657272322.json, 图片生成/文生图/Base+Turbo分段渲染_2017271994244403202.json, 图片生成/文生图/Krea2 RAW-Turbo 高低噪采样_2074460408995471362.json, 图片生成/文生图/Krea2+RAW-Turbo 高低噪采样_2096849477477945346.json, 图片生成/文生图/Z-Image Base+ControlNet+Turbo高低噪_2022635998764601346.json, 图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试_2023370355200495617.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/2512两步出图_2017532037657272322.json、图片生成/文生图/Base+Turbo分段渲染_2017271994244403202.json、图片生成/文生图/Krea2 RAW-Turbo 高低噪采样_2074460408995471362.json、图片生成/文生图/Krea2+RAW-Turbo 高低噪采样_2096849477477945346.json、图片生成/文生图/Z-Image Base+ControlNet+Turbo高低噪_2022635998764601346.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SplitSigmas` —— 5/6 个有
- `VAEEncode` —— 5/6 个有
- `DetailDaemonSamplerNode` —— 4/6 个有
- `EmptyLatentImage` —— 4/6 个有
- `ImageScaleBy` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `easy int` —— 4/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `ImageLoader` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `LatentUpscaleBy` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `ModelPatchLoader` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `ZImageFunControlnet` —— 2/6 个有
- `image_scale_pixel_v2` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `ImageBatchMulti` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RunningHub_ZImageI2L_Loader` —— 1/6 个有
- `RunningHub_ZImageI2L_LoraGenerator` —— 1/6 个有
- `RunningHub_ZImageI2L_Saver` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 4 | 67% |
| 高度 | 748 | 472 - 1024 | 4 | 63% |
| LoRA 模型强度 | 1.1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，4 个样本
- 高度 中位数 748，观测区间 472 - 1024，4 个样本
