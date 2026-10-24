---
name: unknown_workflow_sampler_unet_vae_96
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8777
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json, 图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json, 图片生成/图生图/角色三视图__2112738425802682369.json, 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json, 图片生成/文生图/Qwen Image 2.1_2102977844501639169.json, 图片生成/文生图/Qwen-Image-2.1-图生图_2101854452645978114.json, 图片生成/文生图/Qwen_image_2_1_多图编辑_2101885250807877634.json, 图片生成/文生图/qwen image  edit 2.1_2101931566393024514.json, 图片生成/文生图/qwen image 2.1文生图生_2101747084268498945.json, 图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_96

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json、图片生成/图生图/角色三视图_Qwen image 2.1_2107299006337601538.json、图片生成/图生图/角色三视图__2112738425802682369.json、图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json、图片生成/文生图/Qwen Image 2.1_2102977844501639169.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/10 个有
- `SaveImageAdvanced` —— 6/10 个有
- `ResolutionSelector` —— 5/10 个有
- `CR Text` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ImageScaleToTotalPixels` —— 2/10 个有
- `ImageStitch` —— 2/10 个有
- `LayerUtility: TextJoin` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1536 | 10 | 83% |
| 高度 | 1024 | 1024 - 2048 | 10 | 72% |
| 采样步数 | 25 | 25 - 50 | 10 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 10 | 40% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1536，10 个样本，取值集中（一致性 83%）
- 高度 中位数 1024，观测区间 1024 - 2048，10 个样本
- 采样步数 中位数 25，观测区间 25 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，10 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
