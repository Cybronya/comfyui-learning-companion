---
name: text_to_image_lora_sampler_clip_64
type: Text To Image
frequency: 16
level: strong
coverage: 0.853
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux3-klein指定位置修改，局部重绘图生图方案_2111947609521868801.json, 图片生成/图生图/Flux3_klein图像编辑，图生图动作迁移数字人微调样样通_2112681484900462593.json, 图片生成/图生图/MiniMax H3提示词增强器｜Qwen3.8-27B智能优化_2096315918623272961.json, 图片生成/图生图/flux3_klein 图片编辑｜写实美少女修图利器_2112443453094318082.json, 图片生成/图生图/flux3_klein图片编辑，美少女写实风图生图微调_2112632993977294850.json, 图片生成/图生图/flux3_klein多参考图生图｜多图素材一起喂出图更稳_2111292500743909378.json, 图片生成/文生图/(文生图 Flux3 )Flux3-Klein Text-to-Image，工作流直出_2111584553310711810.json, 图片生成/文生图/Flux3 Image Klein distill t2i加速，文生图极速出片_2111567165089476610.json, 图片生成/文生图/Flux3 kelin图像编辑实测，文生图图生图对比_2111593382610030593.json, 图片生成/文生图/Flux3 kelin图像编辑提示词优化，文生图图生图_2111587094111014914.json, 图片生成/文生图/Flux3-Klein Text-to-Image文生图工作流｜英文全称也能跑_2111343130200068097.json, 图片生成/文生图/Flux3-Klein Text-to-Image，文生图工作流直出_2111547115834011649.json, 图片生成/文生图/Flux3-klein指定位置精准生成，文生图创意利器_2111946145101606913.json, 图片生成/文生图/flux3 t2v蒸馏版本，文生图反推提示词图生图_2111896835517411329.json, 图片生成/文生图/flux3_image_klein多图编辑，文生图图生图双修_2111532002741673986.json, 图片生成/文生图/flux3_image_klein多图编辑｜文生图图生图双模式自由切换_2111289103454138369.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Flux3-klein指定位置修改，局部重绘图生图方案_2111947609521868801.json、图片生成/图生图/Flux3_klein图像编辑，图生图动作迁移数字人微调样样通_2112681484900462593.json、图片生成/图生图/MiniMax H3提示词增强器｜Qwen3.8-27B智能优化_2096315918623272961.json、图片生成/图生图/flux3_klein 图片编辑｜写实美少女修图利器_2112443453094318082.json、图片生成/图生图/flux3_klein图片编辑，美少女写实风图生图微调_2112632993977294850.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 15/16 个有
- `PreviewAny` —— 13/16 个有
- `PrimitiveStringMultiline` —— 13/16 个有
- `TextGenerate` —— 13/16 个有
- `EmptyFlux2LatentImage` —— 12/16 个有
- `LoadImage` —— 10/16 个有
- `ReferenceMultiLatent` —— 9/16 个有
- `ComfySwitchNode` —— 7/16 个有
- `ResolutionSelector` —— 7/16 个有
- `BatchImagesNode` —— 6/16 个有
- `Ideogram4PromptBuilderKJ` —— 4/16 个有
- `Text` —— 4/16 个有
- `ConditioningZeroOut` —— 3/16 个有
- `Image Comparer (rgthree)` —— 3/16 个有
- `CreateBoundingBoxes` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `PreviewImage` —— 2/16 个有
- `ImageCompare` —— 1/16 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
