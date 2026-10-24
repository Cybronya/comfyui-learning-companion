---
name: unknown_workflow_clip_unet_vae
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.96372
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/002.Qwen编辑之王002.二次采样文生图_2034485126217863170.json, 图片生成/文生图/2030248533244256258.json, 图片生成/文生图/2030259700943560706.json, 图片生成/文生图/2030270553520607233.json, 图片生成/文生图/2030517261940822018.json, 图片生成/文生图/60.tonnie-Magic-Wan-Image文生图_2009063719375998977.json, 图片生成/文生图/Animate动漫出图Qwen工作流_2047157124668592129.json, 图片生成/文生图/Animate动漫出图Qwen工作流_2049757423077957634.json, 图片生成/文生图/Z-I-B道具快乐美女_2040453074061369345.json, 图片生成/文生图/Z-I-B长腿肉腿刺客美女_2056916021260410881.json, 图片生成/文生图/Z-image一键美女文生图_2023344603134431233.json, 图片生成/文生图/Z-image大码瑜伽裤模特_2054817937000804354.json, 图片生成/文生图/Z-image真实文生图_2027593525369507841.json, 图片生成/文生图/Z-image真实文生图_2096478812799328257.json, 图片生成/文生图/Z-image真实文生图无限制_2021242393848188929.json, 图片生成/文生图/Z-image韩国美少女写真_2040461723756400642.json, 图片生成/文生图/Z-image高中女生校服丝袜写真_2025507598744690689.json, 图片生成/文生图/qwen2512粗线条水墨_2082670662396760065.json, 图片生成/文生图/【老金驿站】Animate动漫出图Qwen工作流_1967848816110088193.json, 图片生成/文生图/一键生成可爱的小仙女_2029386005651922945.json, 图片生成/文生图/一键生成粗线条水彩画_2067418485902368769.json, 图片生成/文生图/动漫融合现实_2002300969109078017.json, 图片生成/文生图/动漫融合现实_2068864210045587458.json, 图片生成/文生图/粗线条插画_2016470143131459586.json, 图片生成/文生图/粗线条水彩_2021242555865763842.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/002.Qwen编辑之王002.二次采样文生图_2034485126217863170.json、图片生成/文生图/2030248533244256258.json、图片生成/文生图/2030259700943560706.json、图片生成/文生图/2030270553520607233.json、图片生成/文生图/2030517261940822018.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 24/25 个有
- `LoraLoaderModelOnly` —— 24/25 个有
- `CompressImages` —— 14/25 个有
- `SeedVR2` —— 5/25 个有
- `SeedVR2BlockSwap` —— 5/25 个有
- `LatentUpscaleBy` —— 4/25 个有
- `PathchSageAttentionKJ` —— 4/25 个有
- `CheckpointLoaderSimple` —— 1/25 个有
- `KSamplerAdvanced` —— 1/25 个有
- `easy promptLine` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 12 | 24 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 25 | 48% |
| 采样算法 | euler | - | 25 | 92% |
| 调度器 | simple | - | 25 | 72% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 12，24 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，25 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，25 个样本，一致性 92%
- 调度器 最常用 simple，25 个样本，一致性 72%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（18/25 个样本）：Steps较低可能导致细节不足
