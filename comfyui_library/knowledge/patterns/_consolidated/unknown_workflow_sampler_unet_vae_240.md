---
name: unknown_workflow_sampler_unet_vae_240
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.923
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json, 图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json, 图片生成/图生图/Qwen2.1图像编辑_（无PE）_2103535325745336321.json, 图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_240

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json、图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json、图片生成/图生图/Qwen2.1图像编辑_（无PE）_2103535325745336321.json、图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `ImageCompare` —— 2/4 个有
- `WujiCleaner` —— 2/4 个有
- `WujiUpscaler2` —— 2/4 个有
- `QwenImage21SageAttentionT8` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 8 - 40 | 4 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 4 | 42% |
| 采样算法 | deis_2m | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 8 - 40，4 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，4 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 deis_2m，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
