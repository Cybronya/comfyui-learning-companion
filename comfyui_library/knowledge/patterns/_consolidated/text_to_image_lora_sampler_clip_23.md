---
name: text_to_image_lora_sampler_clip_23
type: Text To Image
frequency: 25
level: strong
coverage: 0.86716
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(文生图 Flux3 )Flux3-Klein Text-to-Image，工作流直出_2111584553310711810.json, 图片生成/文生图/FLUX3 Image Klein文生图修复版，中文繁体招牌王_2111942921883840514.json, 图片生成/文生图/Flux 3_Image_Klein开源版文生图｜角色设计写真一把好手_2111303591293177858.json, 图片生成/文生图/Flux3 Image Klein distill t2i加速，文生图极速出片_2111567165089476610.json, 图片生成/文生图/Flux3 Klein提示词增强文生图 创意直出高效处理工具_2113710948639924225.json, 图片生成/文生图/Flux3 Klein文生图提示词增强 创意直出省心生成工具_2113709466570022914.json, 图片生成/文生图/Flux3 Klein文生图，人像写真海报制作全能出图_2112279255878033409.json, 图片生成/文生图/Flux3-Klein Text-to-Image文生图工作流｜英文全称也能跑_2111343130200068097.json, 图片生成/文生图/Flux3-Klein Text-to-Image，文生图工作流直出_2111547115834011649.json, 图片生成/文生图/Flux3-klein指定位置精准生成，文生图创意利器_2111946145101606913.json, 图片生成/文生图/Flux3-klein提示词增强文生图｜创意画面直出更轻松省事_2113539868348469249.json, 图片生成/文生图/Flux3-klein文生图带提示词增强｜一键自动扩写出好图_2111269274059890689.json, 图片生成/文生图/Flux3-klein文生图提示词增强版｜创意出图省心利器_2114028428172292098.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2111610313010401282.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2113183047603539969.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2113198789153615874.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2113543215390482434.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2113546638164848641.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2115241622115020801.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2115249244402708481.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2115343194643849217.json, 图片生成/文生图/Flux3-klein文生图提示词增强｜创意直出更省心_2114072279226347522.json, 图片生成/文生图/Flux3-klein文生图提示词自动增强｜创意直出省心出图_2113538281471303681.json, 图片生成/文生图/Flux3_Klein_t2i文生图｜人像写真海报制作全能｜文本直出高质量图片_2112046112122171393.json, 图片生成/文生图/Moss Image SFT文生图 监督微调高质量图像生成工具_2113687761625632770.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/(文生图 Flux3 )Flux3-Klein Text-to-Image，工作流直出_2111584553310711810.json、图片生成/文生图/FLUX3 Image Klein文生图修复版，中文繁体招牌王_2111942921883840514.json、图片生成/文生图/Flux 3_Image_Klein开源版文生图｜角色设计写真一把好手_2111303591293177858.json、图片生成/文生图/Flux3 Image Klein distill t2i加速，文生图极速出片_2111567165089476610.json、图片生成/文生图/Flux3 Klein提示词增强文生图 创意直出高效处理工具_2113710948639924225.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 25 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 24/25 个有
- `ResolutionSelector` —— 24/25 个有
- `TextGenerate` —— 23/25 个有
- `PreviewImage` —— 17/25 个有
- `孤海注释` —— 17/25 个有
- `CR Prompt Text` —— 15/25 个有
- `ConditioningZeroOut` —— 15/25 个有
- `easy showAnything` —— 15/25 个有
- `ComfySwitchNode` —— 7/25 个有
- `PreviewAny` —— 7/25 个有
- `Fast Groups Bypasser (rgthree)` —— 3/25 个有
- `Seed (rgthree)` —— 3/25 个有
- `ComfyMathExpression` —— 2/25 个有
- `Ideogram4PromptBuilderKJ` —— 2/25 个有
- `ModelSamplingFlux` —— 2/25 个有
- `PrimitiveFloat` —— 2/25 个有
- `SkipLayerGuidanceDiTSimple` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（33/25 个样本）：Steps较低可能导致细节不足
