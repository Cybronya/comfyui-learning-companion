---
name: text_to_image_sampler_clip_unet_22
type: Text To Image
frequency: 17
level: moderate
coverage: 0.946412
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SuperZimage图片处理（4K文生图）_2041019748875509762.json, 图片生成/文生图/Text to Image _ Z-IMAGE_1993955627510726657.json, "图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json", "图片生成/文生图/Tutu's HiSilk Fishnet Z Image workflow_2070527636975210497.json", 图片生成/文生图/YJ-APP-Zimage-文生图-瑶光_2038252771387908097.json, 图片生成/文生图/Z image Art文生图_2019704255820599297.json, 图片生成/文生图/Z-Image Re-Turbo_2073289018476941314.json, 图片生成/文生图/Z-Image 超强文生图_1993850615438704641.json, 图片生成/文生图/Z-Image-De文生图(Z-Image脱蒸馏版-效果更好)_1997646136397729793.json, 图片生成/文生图/Z-Image-De文生图_1997873304331517954.json, 图片生成/文生图/Z-Image-Turbo + Lora 文生图_2008180292552495105.json, 图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2004613231027126274.json, 图片生成/文生图/Z-Image-Turbo文生图标准工作流_2091176473360166914.json, 图片生成/文生图/Z-image turbo基础生图工作流_2028382510350082049.json, 图片生成/文生图/Zimage图片处理（4K文生图）_2016847780504936449.json, 图片生成/文生图/Zimage文生图_1993848041241329666.json, 图片生成/文生图/橘猫和胖虎搞笑图片抖音超火_1987561612901068801.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/SuperZimage图片处理（4K文生图）_2041019748875509762.json、图片生成/文生图/Text to Image _ Z-IMAGE_1993955627510726657.json、图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json、图片生成/文生图/Tutu's HiSilk Fishnet Z Image workflow_2070527636975210497.json、图片生成/文生图/YJ-APP-Zimage-文生图-瑶光_2038252771387908097.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/17 个有
- `LoraLoaderModelOnly` —— 11/17 个有
- `ModelSamplingAuraFlow` —— 4/17 个有
- `PrimitiveInt` —— 3/17 个有
- `Textbox` —— 3/17 个有
- `CR SDXL Aspect Ratio` —— 2/17 个有
- `DyPE_FLUX` —— 2/17 个有
- `CR Text Concatenate` —— 1/17 个有
- `ResolutionSelector` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 20 | 15 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 15 | 70% |
| 采样算法 | euler | - | 15 | 80% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 1080 | 512 - 4096 | 17 | 40% |
| 高度 | 1920 | 512 - 2048 | 17 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 80%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 4096，17 个样本，取值分散，一致性仅 40%
- 高度 中位数 1920，观测区间 512 - 2048，17 个样本
