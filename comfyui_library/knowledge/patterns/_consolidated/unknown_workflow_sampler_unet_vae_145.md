---
name: unknown_workflow_sampler_unet_vae_145
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.933143
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/boogu-edit-单图编辑_2068181907355029506.json, 图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json, 图片生成/图生图/小红书二图编辑(适用换装)_2034643139293618177.json, 图片生成/图生图/服装提取-上下_2038138778417635330.json, 图片生成/图生图/服装提取-前后上下_2038448443059871745.json, 图片生成/文生图/Qwen Edit 2509新旅游飞机_1991073540537524226.json, 图片生成/文生图/动作编辑器应用之四__FireRed文生图_2021382520541028354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_145

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/boogu-edit-单图编辑_2068181907355029506.json、图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json、图片生成/图生图/小红书二图编辑(适用换装)_2034643139293618177.json、图片生成/图生图/服装提取-上下_2038138778417635330.json、图片生成/图生图/服装提取-前后上下_2038448443059871745.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 6/7 个有
- `TextEncodeQwenImageEditPlus` —— 6/7 个有
- `CFGNorm` —— 5/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `GetImage` —— 1/7 个有
- `TextEncodeBooguEdit` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1280 | 7 | 71% |
| 高度 | 1024 | 512 - 1280 | 7 | 66% |
| 采样步数 | 8 | 4 - 30 | 7 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 7 | 36% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1280，7 个样本
- 高度 中位数 1024，观测区间 512 - 1280，7 个样本
- 采样步数 中位数 8，观测区间 4 - 30，7 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
