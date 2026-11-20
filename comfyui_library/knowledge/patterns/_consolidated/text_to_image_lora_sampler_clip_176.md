---
name: text_to_image_lora_sampler_clip_176
type: Text To Image
frequency: 10
level: strong
coverage: 0.8507
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux3 kelin图像编辑实测，文生图图生图对比_2111593382610030593.json, 图片生成/文生图/Flux3 kelin图像编辑提示词优化，文生图图生图_2111587094111014914.json, 图片生成/文生图/Flux3-klein指定位置精准生成，文生图创意利器_2111946145101606913.json, 图片生成/文生图/Flux3-klein文生图PUP增强版｜提示词强化出图更细腻_2111742110876659714.json, 图片生成/文生图/Flux3-klein文生图PUP增强，创意形象高清直出_2111907847557697538.json, 图片生成/文生图/MOSS Sft 角色设计文生图｜NB级角色创意直出_2112375262431244289.json, 图片生成/文生图/Moss image SFT自动词优化文生图 提示词自动优化生成工具_2112985046939430913.json, 图片生成/文生图/flux3-image-klein文生图，高清创意形象直出_2111580915750236161.json, 图片生成/文生图/flux3图像编辑加反推提示词，文生图图生图三合一_2111889064533250049.json, 数字人/数字人/MOSS好用的文生图，搭配数字人封面图一并搞定_2112700258626138114.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_176

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Flux3 kelin图像编辑实测，文生图图生图对比_2111593382610030593.json、图片生成/文生图/Flux3 kelin图像编辑提示词优化，文生图图生图_2111587094111014914.json、图片生成/文生图/Flux3-klein指定位置精准生成，文生图创意利器_2111946145101606913.json、图片生成/文生图/Flux3-klein文生图PUP增强版｜提示词强化出图更细腻_2111742110876659714.json、图片生成/文生图/Flux3-klein文生图PUP增强，创意形象高清直出_2111907847557697538.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextGenerate` —— 8/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `ResolutionSelector` —— 4/10 个有
- `CreateBoundingBoxes` —— 3/10 个有
- `LoadImage` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `ReferenceMultiLatent` —— 3/10 个有
- `FastGroupsBypassSwitch` —— 2/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `SkipLayerGuidanceDiTSimple` —— 2/10 个有
- `Text` —— 2/10 个有
- `ACE_TextGoogleTranslate` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `Ideogram4PromptBuilderKJ` —— 1/10 个有
- `ImageCompare` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
