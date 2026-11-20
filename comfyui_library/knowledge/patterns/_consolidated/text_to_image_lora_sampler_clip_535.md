---
name: text_to_image_lora_sampler_clip_535
type: Text To Image
frequency: 3
level: strong
coverage: 0.839
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, EmptySD3LatentImage, GetNode, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超强换装三迁移｜换装姿态人物迁移一致性精准还原_2112908559548768258.json, 数字人/数字人/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100267474842378242.json, 视频生成/图生视频/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100661143726542849.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_535

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/超强换装三迁移｜换装姿态人物迁移一致性精准还原_2112908559548768258.json、数字人/数字人/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100267474842378242.json、视频生成/图生视频/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100661143726542849.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Krea2EditGroundedEncode` —— 2/3 个有
- `Krea2EditModelPatch` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `GroundingDinoModelLoader_SDPose` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `SDPoseOODLoader` —— 1/3 个有
- `SDPoseOODProcessor` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `YOLOModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
