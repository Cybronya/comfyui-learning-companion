---
name: text_to_image_lora_sampler_clip_163
type: Text To Image
frequency: 10
level: strong
coverage: 0.8364
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MOSS image 日系摄影风格文生图｜胶片质感直出2K超省心_2114955174295986178.json, 图片生成/反推提示词/MOSS image提示增强反推风格参考｜文生图全能流_2114038286766403585.json, 图片生成/反推提示词/Moss image SFT高质量加速V2 文生图反推处理工具_2113418743924744193.json, 图片生成/反推提示词/Moss-image三模式文生图，Sft+Fixed组合反推提示词出图_2112601764338946050.json, 图片生成/反推提示词/Moss全流程文生图 提示词优化反推图像生成工具_2113381718588739585.json, 图片生成/图生图/FLUX 3 Image Klein图像编辑，图片换背景图生图_2111961472422203393.json, 图片生成/图生图/FLUX 3 Image Klein图像编辑｜换背景抠图一站式处理_2111754100328189953.json, 图片生成/图生图/FLUX 3 Image Klein官方版 图像编辑换背景处理工具_2113355640738508801.json, 图片生成/图生图/Flux3-klein常规图像编辑PUP增强版｜图生图精修更稳_2111740631423995905.json, 图片生成/图生图/MOSS Image布局控制图像设计 SFT双模式图生图工具_2113052080075268097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_163

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/MOSS image 日系摄影风格文生图｜胶片质感直出2K超省心_2114955174295986178.json、图片生成/反推提示词/MOSS image提示增强反推风格参考｜文生图全能流_2114038286766403585.json、图片生成/反推提示词/Moss image SFT高质量加速V2 文生图反推处理工具_2113418743924744193.json、图片生成/反推提示词/Moss-image三模式文生图，Sft+Fixed组合反推提示词出图_2112601764338946050.json、图片生成/反推提示词/Moss全流程文生图 提示词优化反推图像生成工具_2113381718588739585.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/10 个有
- `PreviewAny` —— 9/10 个有
- `TextGenerate` —— 9/10 个有
- `solarL_SaveImagesToZip` —— 9/10 个有
- `LoadImage` —— 8/10 个有
- `PrimitiveBoolean` —— 6/10 个有
- `ResolutionSelector` —— 6/10 个有
- `BatchImagesNode` —— 4/10 个有
- `ReferenceMultiLatent` —— 4/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `SkipLayerGuidanceDiTSimple` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `CreateBoundingBoxes` —— 1/10 个有
- `ImageCompare` —— 1/10 个有
- `MOSSImageBlockCacheT8` —— 1/10 个有
- `MOSSImageLayoutPrompt` —— 1/10 个有
- `MOSSImagePromptEnhancerT8` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `孤海图像缩放按像素` —— 1/10 个有

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
