---
name: text_to_image_lora_sampler_clip_323
type: Text To Image
frequency: 6
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/泠月luna Krea2 turbo 单采_2084111094850867201.json, 图片生成/文生图/溶图lora基础版_2043624892586795010.json, 图片生成/文生图/燕如嫣-凡人_2004712644147904514.json, 图片生成/文生图/精致简约的传统的中国水彩画_1988883409260916737.json, 图片生成/文生图/视频生成-生成人物图片_2012034993660370945.json, 图片生成/文生图/超写实人像生成 Magic-Wan-Image V2_1990394619835944962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_323

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/泠月luna Krea2 turbo 单采_2084111094850867201.json、图片生成/文生图/溶图lora基础版_2043624892586795010.json、图片生成/文生图/燕如嫣-凡人_2004712644147904514.json、图片生成/文生图/精致简约的传统的中国水彩画_1988883409260916737.json、图片生成/文生图/视频生成-生成人物图片_2012034993660370945.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `ResolutionStdSelector` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 30 | 6 | 46% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 8 | 6 | 10% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | normal | - | 6 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 976 | 512 - 1104 | 6 | 76% |
| 高度 | 1420 | 512 - 1664 | 6 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 30，6 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 8，6 个样本，取值分散，一致性仅 10%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 normal，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 976，观测区间 512 - 1104，6 个样本
- 高度 中位数 1420，观测区间 512 - 1664，6 个样本
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
