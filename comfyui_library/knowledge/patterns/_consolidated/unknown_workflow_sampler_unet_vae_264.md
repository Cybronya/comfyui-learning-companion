---
name: unknown_workflow_sampler_unet_vae_264
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.846333
common_nodes: [BasicScheduler, CLIPLoader, EmptyLatentImage, KSamplerSelect, ModelSamplingAuraFlow, PreviewImage, SamplerCustom, SaveImage, Text, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/boogu-edit 产品详情页-海报设计_2069237677500747778.json, 图片生成/图生图/boogu_edit+Qwen3.5-完美洗图_2069637206297374722.json, 图片生成/图生图/商业产品详情页海报设计-boogu-edit_2069396750527451137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_264

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/boogu-edit 产品详情页-海报设计_2069237677500747778.json、图片生成/图生图/boogu_edit+Qwen3.5-完美洗图_2069637206297374722.json、图片生成/图生图/商业产品详情页海报设计-boogu-edit_2069396750527451137.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `Text`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MultiTextConcatenate` —— 2/3 个有
- `PreviewTextNode` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `CustomAddLabel` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageLoader` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PDRatioSelector` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
