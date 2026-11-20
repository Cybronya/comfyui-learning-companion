---
name: unknown_workflow_sampler_unet_vae_193
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 1
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json, 图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json, 图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json, 图片生成/图生图/Qwen2.1-图生图16参考_2115240696591503362.json, 图片生成/图生图/Qwen2.1-图生图16参考_2115314444816445442.json, 图片生成/图生图/Qwen2.1-图生图16参考提速版_2115478113609142274.json, 图片生成/图生图/image_qwen_image_2.1 角色表_2112852975646494721.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_193

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json、图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json、图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json、图片生成/图生图/Qwen2.1-图生图16参考_2115240696591503362.json、图片生成/图生图/Qwen2.1-图生图16参考_2115314444816445442.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 6/7 个有
- `EmptyLatentImage` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `ImageCompare` —— 2/7 个有
- `WujiCleaner` —— 2/7 个有
- `WujiUpscaler2` —— 2/7 个有
- `QwenImage21SageAttentionT8` —— 1/7 个有
- `easy promptLine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 7 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 29% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.7 - 1 | 7 | 85% |
| 宽度 | 1920 | 1024 - 1920 | 5 | 76% |
| 高度 | 1080 | 720 - 1080 | 5 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，7 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，7 个样本，取值集中（一致性 85%）
- 宽度 中位数 1920，观测区间 1024 - 1920，5 个样本
- 高度 中位数 1080，观测区间 720 - 1080，5 个样本，取值集中（一致性 86%）
