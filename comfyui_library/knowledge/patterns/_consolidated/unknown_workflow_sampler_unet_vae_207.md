---
name: unknown_workflow_sampler_unet_vae_207
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.847
common_nodes: [BasicScheduler, CLIPLoader, CR Prompt Text, DF_Get_image_size, EmptyLatentImage, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed, CR Prompt Text]
members: [图片生成/图生图/2093310369640046593.json, 图片生成/图生图/2100503999580565506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_207

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2093310369640046593.json、图片生成/图生图/2100503999580565506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `DF_Get_image_size`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、CR Prompt Text
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
