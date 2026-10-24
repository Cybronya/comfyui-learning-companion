---
name: unknown_workflow_lora_sampler_unet_184
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.90125
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveStringMultiline, ProcessString, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/主图裂变-人物写真专用，抖音小红书涨粉（相同场景版）_2034540677446508545.json, 图片生成/图生图/主图裂变模特人物专用-相同场景版_2028710405786312705.json, 图片生成/图生图/套图_2001178928289021954.json, 图片生成/文生图/一键生成健身房对镜拍抖音小红书涨粉_2039945938139090945.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_184

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/主图裂变-人物写真专用，抖音小红书涨粉（相同场景版）_2034540677446508545.json、图片生成/图生图/主图裂变模特人物专用-相同场景版_2028710405786312705.json、图片生成/图生图/套图_2001178928289021954.json、图片生成/文生图/一键生成健身房对镜拍抖音小红书涨粉_2039945938139090945.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `ProcessString`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 3/4 个有
- `Textbox` —— 3/4 个有
- `ImageLoader` —— 2/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `LoadImageFromUrl` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
