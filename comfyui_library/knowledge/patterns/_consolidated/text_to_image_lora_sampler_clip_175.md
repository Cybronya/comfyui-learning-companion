---
name: text_to_image_lora_sampler_clip_175
type: Text To Image
frequency: 10
level: strong
coverage: 0.831
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(文生图 Flux3 )Flux3-Klein Text-to-Image，工作流直出_2111584553310711810.json, 图片生成/文生图/AI换装Qwen Image 2.1双图试穿智能提示词 服装展示方案_2108655915309289474.json, 图片生成/文生图/FLUX3 Image Klein文生图修复版，中文繁体招牌王_2111942921883840514.json, 图片生成/文生图/Flux3 Image Klein distill t2i加速，文生图极速出片_2111567165089476610.json, 图片生成/文生图/Flux3 Klein文生图，人像写真海报制作全能出图_2112279255878033409.json, 图片生成/文生图/Flux3-Klein Text-to-Image文生图工作流｜英文全称也能跑_2111343130200068097.json, 图片生成/文生图/Flux3-Klein Text-to-Image，文生图工作流直出_2111547115834011649.json, 图片生成/文生图/Flux3_Klein_t2i文生图｜人像写真海报制作全能｜文本直出高质量图片_2112046112122171393.json, 图片生成/文生图/Moss Image SFT文生图 监督微调高质量图像生成工具_2113687761625632770.json, 图片生成/文生图/flux3 t2v蒸馏版本，文生图反推提示词图生图_2111896835517411329.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_175

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/(文生图 Flux3 )Flux3-Klein Text-to-Image，工作流直出_2111584553310711810.json、图片生成/文生图/AI换装Qwen Image 2.1双图试穿智能提示词 服装展示方案_2108655915309289474.json、图片生成/文生图/FLUX3 Image Klein文生图修复版，中文繁体招牌王_2111942921883840514.json、图片生成/文生图/Flux3 Image Klein distill t2i加速，文生图极速出片_2111567165089476610.json、图片生成/文生图/Flux3 Klein文生图，人像写真海报制作全能出图_2112279255878033409.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `TextGenerate` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `EmptyFlux2LatentImage` —— 8/10 个有
- `PreviewAny` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `Seed (rgthree)` —— 3/10 个有
- `ComfyMathExpression` —— 2/10 个有
- `Ideogram4PromptBuilderKJ` —— 2/10 个有
- `ModelSamplingFlux` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `BatchImagesNode` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `QwenImage21Cache` —— 1/10 个有
- `SkipLayerGuidanceDiTSimple` —— 1/10 个有
- `TextEncodeQwenImage21` —— 1/10 个有

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
| Steps较低可能导致细节不足 | 12/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（12/10 个样本）：Steps较低可能导致细节不足
