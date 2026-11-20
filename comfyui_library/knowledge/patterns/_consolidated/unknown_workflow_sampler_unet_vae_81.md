---
name: unknown_workflow_sampler_unet_vae_81
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.863
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1_2102977844501639169.json, 图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json, 图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 汉服美学_2110739133755912194.json, 图片生成/文生图/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2114257373773778946.json, 图片生成/文生图/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2115284763119546370.json, 图片生成/文生图/Qwen-Image-2.1-Turbo_汉服美学_2114258449633726466.json, 图片生成/文生图/Qwen-Image-2.1-Turbo_汉服美学_2115285022793097218.json, 数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json, 视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json, 视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json, 视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json, 视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_81

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1_2102977844501639169.json、图片生成/文生图/Qwen Image 2.1去除ai感_2101954709987872770.json、图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json、图片生成/文生图/Qwen-Image-2.1-Turbo 汉服美学_2110739133755912194.json、图片生成/文生图/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2114257373773778946.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 12/13 个有
- `CR Prompt Text` —— 10/13 个有
- `LoadImage` —— 8/13 个有
- `QwenPERewriteT8` —— 7/13 个有
- `easy showAnything` —— 7/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `PreviewImage` —— 6/13 个有
- `easy cleanGpuUsed` —— 6/13 个有
- `Color Grading JK` —— 5/13 个有
- `EmptyImage` —— 4/13 个有
- `AIO_Preprocessor` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `ImageStitch` —— 1/13 个有
- `Lora Loader Stack (rgthree)` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 7 - 50 | 13 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 13 | 44% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 13 | 100% |
| 高度 | 1024 | 1024 - 1536 | 13 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 7 - 50，13 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，13 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，13 个样本，取值集中（一致性 87%）
