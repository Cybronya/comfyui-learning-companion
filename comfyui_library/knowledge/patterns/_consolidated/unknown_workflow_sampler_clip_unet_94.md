---
name: unknown_workflow_sampler_clip_unet_94
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.932727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, Qwen3_VQA, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image 洗海报_1996173832136409090.json, 图片生成/图生图/Z-image_zimage图生图_超真实_提示词反推_洗图_2039230075119341569.json, 图片生成/图生图/z-image图像反推+高清增强_1996478328385191937.json, 图片生成/图生图/图生图_超真实_Z-image_zimage_2021100118765735937.json, 图片生成/图生图/提示词反推 洗图 图生图 Z-image zimage_2041781839127388162.json, 图片生成/图生图/提示词反推 洗图 图生图 Z-image zimage_2042084929978245121.json, 图片生成/图生图/提示词反推 洗图 图生图 Z-image zimage_2095381225857966082.json, 图片生成/图生图/提示词反推 洗图 图生图 qwen3 Z-image zimage_2043979370460614658.json, 图片生成/图生图/提示词反推_图生图_超真实_无AI感_Z-image_zimage_2021051506253893634.json, 图片生成/图生图/洗图 反推  提示词 图生图 Z-image zimage_2043316670013378562.json, 图片生成/文生图/Z image base万能真实渲染电商图_2029159843000487937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_94

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Z-Image 洗海报_1996173832136409090.json、图片生成/图生图/Z-image_zimage图生图_超真实_提示词反推_洗图_2039230075119341569.json、图片生成/图生图/z-image图像反推+高清增强_1996478328385191937.json、图片生成/图生图/图生图_超真实_Z-image_zimage_2021100118765735937.json、图片生成/图生图/提示词反推 洗图 图生图 Z-image zimage_2041781839127388162.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 10/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `LayerUtility: PurgeVRAM V2` —— 2/11 个有
- `SeedVR2` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `GetImageSizeAndCount` —— 1/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有
- `QwenVisionNode` —— 1/11 个有
- `SeedVR2BlockSwap` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 9 - 50 | 11 | 59% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 11 | 67% |
| 采样算法 | res_multistep | - | 11 | 82% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 9 - 50，11 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，11 个样本
- 采样算法 最常用 res_multistep，11 个样本，一致性 82%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
