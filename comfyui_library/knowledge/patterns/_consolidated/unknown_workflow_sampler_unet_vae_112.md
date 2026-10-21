---
name: unknown_workflow_sampler_unet_vae_112
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.814
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json, 图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json, 图片生成/文生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json, 图片生成/文生图/Qwen Image 2.1_2102977844501639169.json, 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo-6步LORA快速出圖_2103865932690059265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_112

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json、图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json、图片生成/文生图/Qwen Image 2.1 ｜生图及编辑_2101865008786395137.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 6/7 个有
- `LoadImage` —— 4/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `QwenImage21Cache` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `SaveImageAdvanced` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `PixaromaRunTimer` —— 1/7 个有
- `PixaromaSeed` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1536 | 7 | 84% |
| 采样步数 | 40 | 6 - 50 | 7 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 7 | 34% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，7 个样本，取值集中（一致性 84%）
- 采样步数 中位数 40，观测区间 6 - 50，7 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
