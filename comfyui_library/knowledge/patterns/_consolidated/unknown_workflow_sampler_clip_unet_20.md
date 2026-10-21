---
name: unknown_workflow_sampler_clip_unet_20
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.973667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image生图_1997316490393227266.json, 图片生成/文生图/Z-image-base  文生图_2016315853096099842.json, 图片生成/文生图/Z-image-base  文生图工作流_2016356755948703746.json, 图片生成/文生图/Z-image-base  电影分镜、游戏美术、高端商业摄影_2017866317071650817.json, 图片生成/文生图/Z-image-base 文生图-高细节_2016335325617987585.json, 图片生成/文生图/Z-image-base 生图多样性_2016234401843122178.json, 图片生成/文生图/Z-image-base_2016195556967714818.json, 图片生成/文生图/Z-image-base_2018237442960138241.json, 图片生成/文生图/Z-image-base基础文生图+高清放大_2029451837371326465.json, 图片生成/文生图/qwen2512粗线条水墨_2082670662396760065.json, 图片生成/文生图/一键生成粗线条水彩画_2067418485902368769.json, 图片生成/文生图/动漫融合现实_2002300969109078017.json, 图片生成/文生图/动漫融合现实_2068864210045587458.json, 图片生成/文生图/粗线条插画_2016470143131459586.json, 图片生成/文生图/粗线条水彩_2021242555865763842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_20

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Z image生图_1997316490393227266.json、图片生成/文生图/Z-image-base  文生图_2016315853096099842.json、图片生成/文生图/Z-image-base  文生图工作流_2016356755948703746.json、图片生成/文生图/Z-image-base  电影分镜、游戏美术、高端商业摄影_2017866317071650817.json、图片生成/文生图/Z-image-base 文生图-高细节_2016335325617987585.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 14/15 个有
- `ModelSamplingAuraFlow` —— 14/15 个有
- `LoraLoaderModelOnly` —— 7/15 个有
- `SeedVR2` —— 5/15 个有
- `SeedVR2BlockSwap` —— 5/15 个有
- `LatentUpscaleBy` —— 4/15 个有
- `CR Text` —— 3/15 个有
- `CR SDXL Aspect Ratio` —— 1/15 个有
- `SeedVR2LoadDiTModel` —— 1/15 个有
- `SeedVR2LoadVAEModel` —— 1/15 个有
- `SeedVR2VideoUpscaler` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 50 | 15 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 15 | 48% |
| 采样算法 | res_multistep | - | 15 | 53% |
| 调度器 | simple | - | 15 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 50，15 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，15 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 res_multistep，15 个样本，一致性 53%
- 调度器 最常用 simple，15 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
