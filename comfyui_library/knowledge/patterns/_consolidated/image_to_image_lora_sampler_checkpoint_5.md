---
name: image_to_image_lora_sampler_checkpoint_5
type: Image To Image
frequency: 5
level: strong
coverage: 0.8506
common_nodes: [CheckpointLoaderSimple, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Next Scene V2+QwenAIOV7.1 AI短剧电影分镜自动生成镜头风格一致_1981021578404184066.json, 图片生成/图生图/Qwen-Edit 图片编辑+提示词P图。超级好用的！多种玩法，可更改动作、天气等。_2031572247973994498.json, 图片生成/图生图/Qwen-Edit 图片编辑+提示词P图。超级好用的！多种玩法，可更改动作、天气等。_2041673205621989377.json, 图片生成/图生图/Qwen-Edit 图片编辑+提示词P图。超级好用的！多种玩法，可更改动作、天气等。_2073596247868530690.json, 图片生成/图生图/Qwen-Edit 图片编辑+提示词P图！艾橘溪_1958001259452182529.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Next Scene V2+QwenAIOV7.1 AI短剧电影分镜自动生成镜头风格一致_1981021578404184066.json、图片生成/图生图/Qwen-Edit 图片编辑+提示词P图。超级好用的！多种玩法，可更改动作、天气等。_2031572247973994498.json、图片生成/图生图/Qwen-Edit 图片编辑+提示词P图。超级好用的！多种玩法，可更改动作、天气等。_2041673205621989377.json、图片生成/图生图/Qwen-Edit 图片编辑+提示词P图。超级好用的！多种玩法，可更改动作、天气等。_2073596247868530690.json、图片生成/图生图/Qwen-Edit 图片编辑+提示词P图！艾橘溪_1958001259452182529.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `Int` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | sgm_uniform | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
