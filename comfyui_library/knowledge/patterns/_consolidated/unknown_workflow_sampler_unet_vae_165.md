---
name: unknown_workflow_sampler_unet_vae_165
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.877857
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json, 图片生成/文生图/qwen image  edit 2.1_2101931566393024514.json, 图片生成/文生图/qwen image 2.1 文_图省图_2108227375078141954.json, 图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json, 图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json, 图片生成/文生图/qwen2.1文生图_2104275580962304002.json, 图片生成/文生图/图像编辑（多图）-qwen image 2.1_2101936015538737153.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_165

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json、图片生成/文生图/qwen image  edit 2.1_2101931566393024514.json、图片生成/文生图/qwen image 2.1 文_图省图_2108227375078141954.json、图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json、图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `QwenImage21Cache` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `TextEncodeQwenImage21` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `SaveImageAdvanced` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `JjkShowText` —— 1/7 个有
- `QwenImagePromptOptimizer` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `TextEncodeQwenImage21GH` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 944 - 1024 | 7 | 97% |
| 高度 | 1024 | 1024 - 1672 | 7 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 944 - 1024，7 个样本，取值集中（一致性 97%）
- 高度 中位数 1024，观测区间 1024 - 1672，7 个样本
