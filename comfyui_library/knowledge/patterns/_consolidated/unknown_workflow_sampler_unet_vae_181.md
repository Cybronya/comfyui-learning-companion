---
name: unknown_workflow_sampler_unet_vae_181
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.847714
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/360环视视频制作_RunningHub版_2116874459687768065.json, 图片生成/图生图/Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089.json, 图片生成/图生图/Qwen image 2.1图片编辑-1_2112506837907099650.json, 图片生成/图生图/QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json, 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json, 图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json, 平台全量/360环视视频制作_RunningHub版_2117474158396395521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_181

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/360环视视频制作_RunningHub版_2116874459687768065.json、图片生成/图生图/Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089.json、图片生成/图生图/Qwen image 2.1图片编辑-1_2112506837907099650.json、图片生成/图生图/QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json、图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 5/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `忽略多组孤海` —— 3/7 个有
- `233740c6-9e7c-49e4-b037-ac2108d00af3` —— 2/7 个有
- `Any Switch (rgthree)` —— 2/7 个有
- `VHS_VideoCombine` —— 2/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1600 | 16 - 2048 | 7 | 51% |
| 高度 | 1152 | 928 - 2000 | 7 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1600，观测区间 16 - 2048，7 个样本
- 高度 中位数 1152，观测区间 928 - 2000，7 个样本
