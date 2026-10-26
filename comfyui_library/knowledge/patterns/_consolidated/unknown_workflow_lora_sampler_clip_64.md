---
name: unknown_workflow_lora_sampler_clip_64
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.866286
common_nodes: [AdaptiveLongestEdge_EditUtils, CLIPLoader, CLIPTextEncode, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/反推提示词/55qushubeijing_2051284332672761857.json, 图片生成/图生图/Flux2 Klein 4B一致性lora 不偏色 不偏移_2033051077326671873.json, 图片生成/图生图/Flux2 Klein 9B 单图编辑_一致性_无偏移_2030877169433448450.json, 图片生成/图生图/Flux2 Klein kv_去除AI痕迹_2059503497468538881.json, 图片生成/图生图/Flux2任意画风快速转成高真实感照片 动漫 _ 插画转真人 _ 实景 草图 _ 线稿 → 写实效果_2021170999294693378.json, 图片生成/图生图/去除背景-klein_2042797681554235394.json, 图片生成/图生图/各种动漫风格转真实人物（Flux2 Klein 9B Anything2Real A ）_2018858828191768577.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/55qushubeijing_2051284332672761857.json、图片生成/图生图/Flux2 Klein 4B一致性lora 不偏色 不偏移_2033051077326671873.json、图片生成/图生图/Flux2 Klein 9B 单图编辑_一致性_无偏移_2030877169433448450.json、图片生成/图生图/Flux2 Klein kv_去除AI痕迹_2059503497468538881.json、图片生成/图生图/Flux2任意画风快速转成高真实感照片 动漫 _ 插画转真人 _ 实景 草图 _ 线稿 → 写实效果_2021170999294693378.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `AdaptiveLongestEdge_EditUtils`
- `CLIPLoader`
- `CLIPTextEncode`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 6/7 个有
- `CropWithPadInfo_EditUtils` —— 5/7 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `SaveImage` —— 5/7 个有
- `VAEDecode` —— 5/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `RMBG` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `VAEDecodeTiled` —— 2/7 个有
- `easy imageSave` —— 2/7 个有
- `string_util_StrConcat` —— 2/7 个有
- `Float` —— 1/7 个有
- `Int` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 7 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，7 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
