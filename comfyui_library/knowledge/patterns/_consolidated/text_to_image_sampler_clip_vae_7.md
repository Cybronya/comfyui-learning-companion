---
name: text_to_image_sampler_clip_vae_7
type: Text To Image
frequency: 11
level: moderate
coverage: 0.892818
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/16.tonnie-nunchaku文生图_1997621361398976513.json, 图片生成/文生图/1912954176630943746.json, 图片生成/文生图/1912954209854259202.json, 图片生成/文生图/1914963069880205314.json, 图片生成/文生图/1919938265468567553.json, 图片生成/文生图/1921302462970658818.json, 图片生成/文生图/1922920426165473282.json, 图片生成/文生图/1981699548944965633.json, 图片生成/文生图/FLUX + LoRA 文生图工作流_2087432058120523777.json, 图片生成/文生图/FLUX + 加速LoRA 文生图工作流_2039621959402659841.json, 视频生成/图生视频/1947265490784784385.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_7

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/16.tonnie-nunchaku文生图_1997621361398976513.json、图片生成/文生图/1912954176630943746.json、图片生成/文生图/1912954209854259202.json、图片生成/文生图/1914963069880205314.json、图片生成/文生图/1919938265468567553.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 9/11 个有
- `FluxGuidance` —— 9/11 个有
- `PreviewImage` —— 8/11 个有
- `UNETLoader` —— 8/11 个有
- `LoraLoader` —— 5/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `CheckpointLoaderSimple` —— 2/11 个有
- `FluxKontextImageScale` —— 1/11 个有
- `Int` —— 1/11 个有
- `Kontext Inpainting Conditioning` —— 1/11 个有
- `LoadImage` —— 1/11 个有
- `NunchakuFluxDiTLoader` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 800 - 1536 | 11 | 76% |
| 高度 | 1200 | 768 - 1536 | 11 | 80% |
| 采样步数 | 28 | 8 - 35 | 11 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 11 | 0% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 1 | 0.6 - 1 | 5 | 82% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 800 - 1536，11 个样本
- 高度 中位数 1200，观测区间 768 - 1536，11 个样本，取值集中（一致性 80%）
- 采样步数 中位数 28，观测区间 8 - 35，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，11 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.6 - 1，5 个样本，取值集中（一致性 82%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
