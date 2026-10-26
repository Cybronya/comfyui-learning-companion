---
name: unknown_workflow_sampler_clip_unet_72
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.954308
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/zit超越真实_2060354934306066433.json, 图片生成/文生图/​动漫角色融合现实_2068958522259369986.json, 图片生成/文生图/① Z-Image Turbo · 8 步快速出稿_2101557565405622273.json, 图片生成/文生图/【提速2倍】Qwen-Image-Lightning 8步加速文生图v2_1953283718866792449.json, 图片生成/文生图/【老金驿站】4步Qwen2512极速lighiting出图工作流_2006643426929938433.json, 图片生成/文生图/【老金驿站】Z-imageBase真实系列Lora工作流_2037516112421720066.json, 图片生成/文生图/【老金驿站】Z-imageBase高质量稳定直出工作流_2016671045016625154.json, 图片生成/文生图/一键生成粗线条水彩画_2067418485902368769.json, 图片生成/文生图/动漫融合现实_2002300969109078017.json, 图片生成/文生图/动漫融合现实_2068864210045587458.json, 图片生成/文生图/文生图+LoRA+高清放大_2069642245782990849.json, 图片生成/文生图/粗线条插画_2016470143131459586.json, 图片生成/文生图/粗线条水彩_2021242555865763842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/zit超越真实_2060354934306066433.json、图片生成/文生图/​动漫角色融合现实_2068958522259369986.json、图片生成/文生图/① Z-Image Turbo · 8 步快速出稿_2101557565405622273.json、图片生成/文生图/【提速2倍】Qwen-Image-Lightning 8步加速文生图v2_1953283718866792449.json、图片生成/文生图/【老金驿站】4步Qwen2512极速lighiting出图工作流_2006643426929938433.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 12/13 个有
- `LoraLoaderModelOnly` —— 11/13 个有
- `SeedVR2` —— 7/13 个有
- `SeedVR2BlockSwap` —— 7/13 个有
- `CFGNorm` —— 4/13 个有
- `PreviewImage` —— 3/13 个有
- `easy cleanGpuUsed` —— 3/13 个有
- `LatentUpscaleBy` —— 2/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `ImageScaleToTotalPixels` —— 1/13 个有
- `MmuuaiGroupBypass` —— 1/13 个有
- `SeedVR2ExtraArgs` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 25 | 13 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 13 | 35% |
| 采样算法 | euler | - | 13 | 85% |
| 调度器 | simple | - | 13 | 38% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 25，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，13 个样本，一致性 85%
- 调度器 最常用 simple，13 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
