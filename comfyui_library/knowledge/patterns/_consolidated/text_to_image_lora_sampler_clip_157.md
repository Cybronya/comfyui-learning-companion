---
name: text_to_image_lora_sampler_clip_157
type: Text To Image
frequency: 7
level: strong
coverage: 0.862
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, Note Plus (mtb), LayerUtility: ImageScaleByAspectRatio V2, Text Multiline]
members: [图片生成/反推提示词/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json, 图片生成/反推提示词/Krea2局部重绘PS版本，风格化反推提示词图生图精准区域编辑工具_2103567391509794817.json, 图片生成/图生图/2102089735173926914.json, 图片生成/图生图/2102091301226369025.json, 图片生成/图生图/2102459788658569217.json, 图片生成/图生图/2102461309957791745.json, 图片生成/图生图/2102468898800095234.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_157

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json、图片生成/反推提示词/Krea2局部重绘PS版本，风格化反推提示词图生图精准区域编辑工具_2103567391509794817.json、图片生成/图生图/2102089735173926914.json、图片生成/图生图/2102091301226369025.json、图片生成/图生图/2102459788658569217.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/7 个有
- `TextEncodeQwenImage21` —— 5/7 个有
- `QwenImage21Cache` —— 4/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `Int` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `ResolutionSelector` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `KSamplerAdvanced` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `RH_RhartImageG25FlareImageToImage` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `TextGenerateLTX2Prompt` —— 1/7 个有
- `VAEEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Note Plus (mtb)、LayerUtility: ImageScaleByAspectRatio V2、Text Multiline
