---
name: text_to_image_sampler_clip_unet_39
type: Text To Image
frequency: 13
level: moderate
coverage: 0.818154
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-lmage+官方版文生图（支持中文字体）_2016410390061654017.json, 图片生成/图生图/Z-IMAGE文生图_图生图洗图小能手_1997999499509399553.json, 图片生成/文生图/Description to Image _ Z-IMAGE_1993955579181940738.json, 图片生成/文生图/Qwen-lmage 官方极速版（支持中文字体）_1954723873654763521.json, 图片生成/文生图/Qwen-lmage 官方版文生图  支持中文字体_1990708737994350594.json, 图片生成/文生图/Qwen-lmage 官方版文生图（支持中文字体）_1952902120161931266.json, 图片生成/文生图/Qwen-lmage 官方版文生图（支持中文字体）_1952909468277346306.json, 图片生成/文生图/Qwen-lmage 官方版文生图（支持中文字体）_1958426605657997313.json, 图片生成/文生图/Qwen-lmage 官方版文生图（支持中文字体）_1963795542739603457.json, 图片生成/文生图/Qwen-lmage 文生图 支持中文字体_2063400027611033601.json, 图片生成/文生图/Qwen-lmage 文生图_2073042188497416194.json, 图片生成/文生图/Z-IMAGE文生图_洗图小钢炮（开源王者）_1994224941826588674.json, 图片生成/文生图/文生图（支持中文字体）_1997683813411172354.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen-lmage+官方版文生图（支持中文字体）_2016410390061654017.json、图片生成/图生图/Z-IMAGE文生图_图生图洗图小能手_1997999499509399553.json、图片生成/文生图/Description to Image _ Z-IMAGE_1993955579181940738.json、图片生成/文生图/Qwen-lmage 官方极速版（支持中文字体）_1954723873654763521.json、图片生成/文生图/Qwen-lmage 官方版文生图  支持中文字体_1990708737994350594.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 12/13 个有
- `CR SDXL Aspect Ratio` —— 10/13 个有
- `ModelSamplingAuraFlow` —— 10/13 个有
- `Textbox` —— 10/13 个有
- `Int` —— 9/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `Text Multiline` —— 2/13 个有
- `easy int` —— 2/13 个有
- `AddLabel` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 13 | 71% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 13 | 66% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 512 | 512 - 1024 | 13 | 69% |
| 高度 | 512 | 512 - 1536 | 13 | 45% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1024，13 个样本
- 高度 中位数 512，观测区间 512 - 1536，13 个样本，取值分散，一致性仅 45%
