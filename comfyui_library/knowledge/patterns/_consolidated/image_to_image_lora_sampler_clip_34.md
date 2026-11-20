---
name: image_to_image_lora_sampler_clip_34
type: Image To Image
frequency: 9
level: strong
coverage: 0.884
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux_Krea真人洗图_1958462222928343041.json, 图片生成/图生图/Flux_Krea真人洗图_2072206265215971330.json, 图片生成/图生图/喜怒哀乐表情包_1949755739474714626.json, 平台全量/Kontext一键除水印（去除文字水印和LOGO）_2041154384377155585.json, 平台全量/kontext_dev线稿上色_1947578269946339330.json, 平台全量/万物秒变毛绒绒_1968950005413396481.json, 平台全量/工作流项目篇12-Kontext老照片修复(Fluxkontext全自动修复）_2016845222692524033.json, 平台全量/照片修复，主题迁移工作流_1981293117741629442.json, 平台全量/终极水印马赛克消除器 超快超强无敌的kontext_1938542985967493121.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux_Krea真人洗图_1958462222928343041.json、图片生成/图生图/Flux_Krea真人洗图_2072206265215971330.json、图片生成/图生图/喜怒哀乐表情包_1949755739474714626.json、平台全量/Kontext一键除水印（去除文字水印和LOGO）_2041154384377155585.json、平台全量/kontext_dev线稿上色_1947578269946339330.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `ReferenceLatent` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `FluxKontextImageScale` —— 4/9 个有
- `ImageConcanate` —— 4/9 个有
- `RepeatLatentBatch` —— 4/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `DisplayText` —— 2/9 个有
- `ImageResizeKJ` —— 2/9 个有
- `Qwen2.5VL` —— 2/9 个有
- `WD14Tagger|pysssss` —— 2/9 个有
- `ImageScaleByAspectRatio_UTK` —— 1/9 个有
- `ImageScaleRestore_UTK` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 9 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 0.7 - 1 | 9 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，9 个样本，取值集中（一致性 87%）
