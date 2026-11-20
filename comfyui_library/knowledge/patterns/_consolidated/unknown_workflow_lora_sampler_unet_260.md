---
name: unknown_workflow_lora_sampler_unet_260
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.982333
common_nodes: [CLIPLoader, DF_Text_Box, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, SaveImage, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物放置_2103016656669863938.json, 图片生成/图生图/纠正透视_2103011758184161282.json, 平台全量/qwen image 2.1 溶图_2106220761554968578.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_260

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万物放置_2103016656669863938.json、图片生成/图生图/纠正透视_2103011758184161282.json、平台全量/qwen image 2.1 溶图_2106220761554968578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `DF_Text_Box`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `SaveImage`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `RestoreQwenImage21GH` —— 2/3 个有
- `DetailTransfer` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
