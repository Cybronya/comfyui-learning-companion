---
name: unknown_workflow_sampler_unet_vae_378
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7695
common_nodes: [BatchImagesNode, CLIPLoader, CR Prompt Text, EmptyLatentImage, ImageResizeKJv2, KSampler, LoadImage, MuyeTextEditOutput, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, TTResolutionSelector, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything, 孤海注释]
problems: []
missing: []
members: [平台全量/Qwen Image 2.1好玩的Lora_2106688379445399554.json, 平台全量/Qwen Image 2.1角色资产生成_2106695488861986817.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_378

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Qwen Image 2.1好玩的Lora_2106688379445399554.json、平台全量/Qwen Image 2.1角色资产生成_2106695488861986817.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CR Prompt Text`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `MuyeTextEditOutput`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TTResolutionSelector`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 35 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
