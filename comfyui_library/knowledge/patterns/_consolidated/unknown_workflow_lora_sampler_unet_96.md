---
name: unknown_workflow_lora_sampler_unet_96
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.905375
common_nodes: [CLIPLoader, GetImageSize+, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, ResizeImagesByLongerEdge, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/klein打光_2104814681612439553.json, 图片生成/图生图/一键光影重塑Klein图生图打光_2099330958804738049.json, 图片生成/图生图/一键光影重塑Klein图生图打光_2099667794504802306.json, 图片生成/图生图/一键场景打光--Klein 9B，光影重塑_2069702134005850114.json, 图片生成/图生图/专用LoRA9B一键光影重塑Klein图生图打光其它电商产品_2082647320872710146.json, 图片生成/图生图/专用LoRA9B一键光影重塑Klein图生图打光其它电商产品_2082655520359542786.json, 图片生成/图生图/图生图-人和场景_2077213095818252289.json, 图片生成/图生图/线稿_2072222648926556161.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_96

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/klein打光_2104814681612439553.json、图片生成/图生图/一键光影重塑Klein图生图打光_2099330958804738049.json、图片生成/图生图/一键光影重塑Klein图生图打光_2099667794504802306.json、图片生成/图生图/一键场景打光--Klein 9B，光影重塑_2069702134005850114.json、图片生成/图生图/专用LoRA9B一键光影重塑Klein图生图打光其它电商产品_2082647320872710146.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `ResizeImagesByLongerEdge`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkShowText` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 10 | 8 | 71% |
| Prompt 约束强度(CFG) | 0.7 | 0.7 - 1 | 8 | 85% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 0.7，观测区间 0.7 - 1，8 个样本，取值集中（一致性 85%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.7，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
