---
name: text_to_image_lora_sampler_clip_156
type: Text To Image
frequency: 10
level: strong
coverage: 0.8786
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2风格参考迁移工作流 图生图风格化转换工具_2099218551642087426.json, 图片生成/图生图/MOSS图生图2K极速版｜风格化图生图出图快效果在线_2112826244516634626.json, 图片生成/图生图/Moss-image 8步加速文生图，图生图辅助提速不等待_2112701805070213121.json, 图片生成/图生图/Moss-image 文生图8步加速版｜图生图洗图更高效_2112404734073204738.json, 图片生成/图生图/Moss-image 文生图提示词增强｜一句话出好图_2112406284036296705.json, 图片生成/图生图/Moss-image提示词增强文生图，图生图辅助出图更省心_2112620573389049858.json, 图片生成/文生图/Flux 3_Image_Klein开源版文生图｜角色设计写真一把好手_2111303591293177858.json, 图片生成/文生图/Flux3-klein文生图带提示词增强｜一键自动扩写出好图_2111269274059890689.json, 图片生成/文生图/Flux3-klein文生图提示词增强，创意直出更省心_2111610313010401282.json, 图片生成/文生图/MOSS SFT 文生图Comfyui官方流｜海报制作利器_2112476243789697025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_156

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Krea2风格参考迁移工作流 图生图风格化转换工具_2099218551642087426.json、图片生成/图生图/MOSS图生图2K极速版｜风格化图生图出图快效果在线_2112826244516634626.json、图片生成/图生图/Moss-image 8步加速文生图，图生图辅助提速不等待_2112701805070213121.json、图片生成/图生图/Moss-image 文生图8步加速版｜图生图洗图更高效_2112404734073204738.json、图片生成/图生图/Moss-image 文生图提示词增强｜一句话出好图_2112406284036296705.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 9/10 个有
- `PreviewImage` —— 8/10 个有
- `TextGenerate` —— 8/10 个有
- `CR Prompt Text` —— 6/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `FluxKontextImageScale` —— 1/10 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `Krea2OstrisEditModelPatch` —— 1/10 个有
- `SkipLayerGuidanceDiTSimple` —— 1/10 个有
- `TextEncodeKrea2OstrisEdit` —— 1/10 个有

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
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
