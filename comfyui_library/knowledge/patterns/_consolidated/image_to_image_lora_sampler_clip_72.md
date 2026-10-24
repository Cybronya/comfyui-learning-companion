---
name: image_to_image_lora_sampler_clip_72
type: Image To Image
frequency: 4
level: weak
coverage: 0.955
common_nodes: [Bjornulf_TextToStringAndSeed, CLIPLoader, CLIPTextEncode, ImageConcanate, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PDIMAGE_LongerSize, PMRF, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Joy3反推提示词+Wan2.2图生图（洗图）_1951284309107879938.json, 图片生成/图生图/Wan2.2洗图(图生图)_1951288024074276865.json, 图片生成/图生图/Wan2.2超绝真实系图生图洗图工作流_1950509604289630210.json, 图片生成/图生图/🦖Wan2.2真实风格洗图（或转绘）（自用）_1950740958910550017.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Joy3反推提示词+Wan2.2图生图（洗图）_1951284309107879938.json、图片生成/图生图/Wan2.2洗图(图生图)_1951288024074276865.json、图片生成/图生图/Wan2.2超绝真实系图生图洗图工作流_1950509604289630210.json、图片生成/图生图/🦖Wan2.2真实风格洗图（或转绘）（自用）_1950740958910550017.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `Bjornulf_TextToStringAndSeed`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PDIMAGE_LongerSize`
- `PMRF`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/4 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 13 | 6 - 20 | 4 | 46% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 3.5 | 4 | 44% |
| 采样算法 | uni_pc | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.2 | 0.15 - 0.3 | 4 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 13，观测区间 6 - 20，4 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 uni_pc，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.15 - 0.3，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
