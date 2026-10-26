---
name: unknown_workflow_sampler_clip_unet_198
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.904857
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ModelSamplingAuraFlow, PreviewImage, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SamplerEulerAncestral, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2029507207917735938.json, 图片生成/文生图/2029507218332196866.json, 图片生成/文生图/2030979831659241473.json, 图片生成/文生图/2512两步出图_2017532037657272322.json, 图片生成/文生图/Base+Turbo分段渲染_2017271994244403202.json, 图片生成/文生图/Z-Image Base+ControlNet+Turbo高低噪_2022635998764601346.json, 图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试_2023370355200495617.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_198

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/2029507207917735938.json、图片生成/文生图/2029507218332196866.json、图片生成/文生图/2030979831659241473.json、图片生成/文生图/2512两步出图_2017532037657272322.json、图片生成/文生图/Base+Turbo分段渲染_2017271994244403202.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DetailDaemonSamplerNode` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `easy int` —— 6/7 个有
- `AIO_Preprocessor` —— 5/7 个有
- `EmptyLatentImage` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `ModelPatchLoader` —— 5/7 个有
- `SplitSigmas` —— 5/7 个有
- `VAEEncode` —— 5/7 个有
- `ZImageFunControlnet` —— 5/7 个有
- `image_scale_pixel_v2` —— 5/7 个有
- `ImageScaleBy` —— 4/7 个有
- `ImageLoader` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `ClipLoaderGGUF` —— 1/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `RunningHub_ZImageI2L_Loader` —— 1/7 个有
- `RunningHub_ZImageI2L_LoraGenerator` —— 1/7 个有
- `RunningHub_ZImageI2L_Saver` —— 1/7 个有
- `Seed Everywhere` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 472 | 472 - 472 | 5 | 100% |
| LoRA 模型强度 | 1.1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 472，观测区间 472 - 472，5 个样本，取值集中（一致性 100%）
