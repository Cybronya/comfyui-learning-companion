---
name: text_to_image_lora_sampler_clip_422
type: Text To Image
frequency: 4
level: strong
coverage: 0.9205
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, RH_Nano_Banana2_Image2Image, SaveImage, Text, Text Concatenate, TextBox1, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键生成对镜展示图-阿浩_2037097638784409602.json, 图片生成/图生图/一键生成电梯女装对镜自拍带货图片抖音小红书女装图文带货涨粉_2039909522357100545.json, 图片生成/图生图/换装强度拉满完全产品一致性_2039982905287516162.json, 图片生成/文生图/即梦（4.0-4.5-5.0）图生图_文生图_2029382803242098690.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_422

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键生成对镜展示图-阿浩_2037097638784409602.json、图片生成/图生图/一键生成电梯女装对镜自拍带货图片抖音小红书女装图文带货涨粉_2039909522357100545.json、图片生成/图生图/换装强度拉满完全产品一致性_2039982905287516162.json、图片生成/文生图/即梦（4.0-4.5-5.0）图生图_文生图_2029382803242098690.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `Text`
- `Text Concatenate`
- `TextBox1`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `Int` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `RH_Jimeng4_Image2Image` —— 2/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/4 个有
- `Repeater|pysssss` —— 2/4 个有
- `Label (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 4 | 100% |
| 高度 | 1344 | 1344 - 1344 | 4 | 100% |
| 采样步数 | 28 | 28 - 28 | 4 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 0.7 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1344，观测区间 1344 - 1344，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 28，观测区间 28 - 28，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 0.7，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
