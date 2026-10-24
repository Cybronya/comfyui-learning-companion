---
name: image_to_image_sampler_clip_unet_14
type: Image To Image
frequency: 15
level: moderate
coverage: 0.911467
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image-Trubo动漫转真人基础版_2033198187133014018.json, 图片生成/图生图/Z-Image-Turbo 图生图编辑 _ 极简 10 节点，8 步出片_2086644646930903041.json, 图片生成/图生图/Z-Image-Turbo-人像去Ai味真实质感_1994013061161959425.json, 图片生成/图生图/Z-Image_ 图像反推生图_1999281406482280449.json, 图片生成/图生图/Z-Image图生图洗图_2046840416087052290.json, 图片生成/图生图/Z-Image图生图洗图_2094304765537771521.json, 图片生成/图生图/Z-Image图生图洗图_2101937229131243521.json, 图片生成/图生图/Z-Image图生图洗图_2105121490088841217.json, 图片生成/图生图/Z-Image图生图洗图_2105498770577387521.json, 图片生成/图生图/Z-Image图生图洗图_2112490094929203201.json, 图片生成/图生图/Z-Image超真实网红打造-洗图_1998985187780386817.json, 图片生成/图生图/Z-image + LoRA 图生图工作流_2059600757091033090.json, 图片生成/图生图/Z-image ControlNet 图生图工作流_2059610100196798465.json, 图片生成/图生图/Z-image ControlNet 图生图工作流_2091491515486003202.json, 图片生成/图生图/杰洛特Z-image，复刻微调长相（批量工作流）_2045054762495774722.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Z-Image-Trubo动漫转真人基础版_2033198187133014018.json、图片生成/图生图/Z-Image-Turbo 图生图编辑 _ 极简 10 节点，8 步出片_2086644646930903041.json、图片生成/图生图/Z-Image-Turbo-人像去Ai味真实质感_1994013061161959425.json、图片生成/图生图/Z-Image_ 图像反推生图_1999281406482280449.json、图片生成/图生图/Z-Image图生图洗图_2046840416087052290.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 14/15 个有
- `Image Comparer (rgthree)` —— 10/15 个有
- `LoraLoaderModelOnly` —— 10/15 个有
- `ConditioningZeroOut` —— 5/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/15 个有
- `PreviewImage` —— 5/15 个有
- `RepeatLatentBatch` —— 4/15 个有
- `AIO_Preprocessor` —— 3/15 个有
- `ModelPatchLoader` —— 3/15 个有
- `Qwen3_VQA` —— 3/15 个有
- `ZImageFunControlnet` —— 3/15 个有
- `easy showAnything` —— 3/15 个有
- `CLIPLoaderGGUF` —— 1/15 个有
- `Float` —— 1/15 个有
- `ImageResizeAdvanced` —— 1/15 个有
- `LayerUtility: PurgeVRAM V2` —— 1/15 个有
- `ModelSamplingAuraFlow` —— 1/15 个有
- `ShowText|pysssss` —— 1/15 个有
- `easy float` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 15 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 15 | 80% |
| 采样算法 | euler | - | 15 | 87% |
| 调度器 | simple | - | 15 | 87% |
| 重绘幅度 | 0.85 | 0.19 - 1 | 15 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，15 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 87%
- 调度器 最常用 simple，15 个样本，一致性 87%
- 重绘幅度 中位数 0.85，观测区间 0.19 - 1，15 个样本
- 高发问题（8/15 个样本）：Steps较低可能导致细节不足
