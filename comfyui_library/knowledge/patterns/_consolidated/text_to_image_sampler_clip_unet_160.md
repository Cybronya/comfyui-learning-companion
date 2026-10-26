---
name: text_to_image_sampler_clip_unet_160
type: Text To Image
frequency: 4
level: weak
coverage: 0.9125
common_nodes: [BasicGuider, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰007.文生图-效果增强_2033731467355889665.json, 图片生成/文生图/F.1+ZIT - 极致逼真文生图_2007498725198929922.json, 图片生成/文生图/FLUX 文生图学习基础工作流 （用于学习）_2054899935157465089.json, 图片生成/文生图/LH-DMT版本-2.生图片类-034.Z-image 官方调度器出图效果增强_2016519410218962946.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_160

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰007.文生图-效果增强_2033731467355889665.json、图片生成/文生图/F.1+ZIT - 极致逼真文生图_2007498725198929922.json、图片生成/文生图/FLUX 文生图学习基础工作流 （用于学习）_2054899935157465089.json、图片生成/文生图/LH-DMT版本-2.生图片类-034.Z-image 官方调度器出图效果增强_2016519410218962946.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `BasicScheduler` —— 2/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `FlowMatchEulerDiscreteScheduler (Custom)` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `ModelSamplingFlux` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `easy int` —— 2/4 个有
- `CLIPTextEncodeFlux` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `DifferentialDiffusion` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 768 - 2048 | 4 | 60% |
| 高度 | 1984 | 1024 - 2048 | 4 | 76% |
| 采样步数 | 9.5 | 9 - 20 | 4 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 4 | 42% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 0.18 - 1 | 4 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1536，观测区间 768 - 2048，4 个样本
- 高度 中位数 1984，观测区间 1024 - 2048，4 个样本
- 采样步数 中位数 9.5，观测区间 9 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，4 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.18 - 1，4 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
