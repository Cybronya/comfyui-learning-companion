---
name: unknown_workflow_lora_sampler_clip_76
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.853833
common_nodes: [AdaptiveLongestEdge_EditUtils, CLIPLoader, CLIPTextEncode, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Flux2 Klein 4B一致性lora 不偏色 不偏移_2033051077326671873.json, 图片生成/图生图/Flux2 Klein 9B 单图编辑_一致性_无偏移_2030877169433448450.json, 图片生成/图生图/Flux2 Klein kv_去除AI痕迹_2059503497468538881.json, 图片生成/图生图/Flux2任意画风快速转成高真实感照片 动漫 _ 插画转真人 _ 实景 草图 _ 线稿 → 写实效果_2021170999294693378.json, 图片生成/图生图/去除背景-klein_2042797681554235394.json, 图片生成/图生图/各种动漫风格转真实人物（Flux2 Klein 9B Anything2Real A ）_2018858828191768577.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 4B一致性lora 不偏色 不偏移_2033051077326671873.json、图片生成/图生图/Flux2 Klein 9B 单图编辑_一致性_无偏移_2030877169433448450.json、图片生成/图生图/Flux2 Klein kv_去除AI痕迹_2059503497468538881.json、图片生成/图生图/Flux2任意画风快速转成高真实感照片 动漫 _ 插画转真人 _ 实景 草图 _ 线稿 → 写实效果_2021170999294693378.json、图片生成/图生图/去除背景-klein_2042797681554235394.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CropWithPadInfo_EditUtils` —— 5/6 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `VAEDecode` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `VAEDecodeTiled` —— 2/6 个有
- `easy imageSave` —— 2/6 个有
- `string_util_StrConcat` —— 2/6 个有
- `Float` —— 1/6 个有
- `Int` —— 1/6 个有
- `RMBG` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 20 | 6 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 20，6 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
