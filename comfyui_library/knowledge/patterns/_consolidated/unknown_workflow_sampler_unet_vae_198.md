---
name: unknown_workflow_sampler_unet_vae_198
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.67
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen2.1图生图工作流_2101875984147509250.json, 图片生成/图生图/Qwen_image_2.1_图生_2101865996205248513.json, 图片生成/图生图/qwen image 2.1多图编辑_2101719348938362882.json, 图片生成/图生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json, 图片生成/文生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_198

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen2.1图生图工作流_2101875984147509250.json、图片生成/图生图/Qwen_image_2.1_图生_2101865996205248513.json、图片生成/图生图/qwen image 2.1多图编辑_2101719348938362882.json、图片生成/图生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json、图片生成/文生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `easy int` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SaveImageAdvanced` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `GH_ImageVideoComparer` —— 1/5 个有
- `MmuuaiGroupBypass` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 25 | 25 - 40 | 5 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
