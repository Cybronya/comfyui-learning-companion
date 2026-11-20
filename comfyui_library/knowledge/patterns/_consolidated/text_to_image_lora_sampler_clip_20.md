---
name: text_to_image_lora_sampler_clip_20
type: Text To Image
frequency: 29
level: strong
coverage: 0.894552
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2风格参考迁移工作流 图生图风格化转换工具_2099218551642087426.json, 图片生成/图生图/MOSS一键洗图2K极速版 图生图写实美化处理工具_2114111554676420610.json, 图片生成/图生图/MOSS一键洗图2K极速版｜角色设计人像图生图快速提质_2113587567160549377.json, 图片生成/图生图/MOSS图生图2K极速洗图 一键美化写实处理工具_2114100330920243202.json, 图片生成/图生图/MOSS图生图2K极速版 风格化图像转换处理生成工具_2113026391880069122.json, 图片生成/图生图/MOSS图生图2K极速版｜图片转高清2K快速出图不等待_2113553613565022209.json, 图片生成/图生图/MOSS图生图2K极速版｜风格化图生图出图快效果在线_2112826244516634626.json, 图片生成/图生图/MOSS图生图一键洗图2K极速 美少女写实处理工具_2114095720641949698.json, 图片生成/图生图/MOSS图生图一键洗图2K极速版 人像写真图像处理工具_2113315474560872450.json, 图片生成/图生图/MOSS图生图一键洗图2K极速版，图生图画质修复秒出高清_2116817728932761601.json, 图片生成/图生图/MOSS图生图一键洗图2K极速版，照片画质修复增强秒级出高清大图_2114448959241539585.json, 图片生成/图生图/MOSS图生图一键洗图2K极速版｜人像写真洗图快速修片_2113585790298185729.json, 图片生成/图生图/MOSS图生图一键洗图2K极速版｜写实美少女洗图首选_2114036251681714178.json, 图片生成/图生图/MOSS图生图一键洗图2K极速版｜写实美少女画质重生_2113987037715066881.json, 图片生成/图生图/MOSS图生图一键洗图2K极速版｜美少女写实画质重塑_2113982025148485634.json, 图片生成/图生图/MOSS图生图一键洗图2K极速版｜角色设计画质重塑_2114043907049877505.json, 图片生成/图生图/MOSS图生图一键洗图极速版｜美少女写实画质升级_2114022561972572162.json, 图片生成/图生图/MOSS图生图洗图2K极速 一键洗图写实美少女工具_2113409093498138625.json, 图片生成/图生图/MOSS图生图洗图2K极速版｜写实美少女一键画质翻新_2114013316866727937.json, 图片生成/图生图/MOSS图生图洗图一键洗图2K极速版｜美少女写实画质飙升_2114293615211139073.json, 图片生成/图生图/Moss-image 8步加速文生图，图生图辅助提速不等待_2112701805070213121.json, 图片生成/图生图/Moss-image 文生图8步加速版｜图生图洗图更高效_2112404734073204738.json, 图片生成/图生图/Moss-image 文生图提示词增强｜一句话出好图_2112406284036296705.json, 图片生成/图生图/Moss-image提示词增强文生图，图生图辅助出图更省心_2112620573389049858.json, 图片生成/图生图/flux3_klein多参考图生图｜多图素材一起喂出图更稳_2111292500743909378.json, 图片生成/文生图/MOSS SFT 文生图Comfyui官方流｜海报制作利器_2112476243789697025.json, 图片生成/文生图/MOSS Sft 角色设计文生图｜NB级角色创意直出_2112375262431244289.json, 图片生成/文生图/MOSS图生图一键洗图2K极速版，图生图画质修复秒出高清_2114486344184590337.json, 图片生成/文生图/MOSS图生图一键洗图2K极速版｜文生图美少女写实全拿捏_2114232368759402498.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/Krea2风格参考迁移工作流 图生图风格化转换工具_2099218551642087426.json、图片生成/图生图/MOSS一键洗图2K极速版 图生图写实美化处理工具_2114111554676420610.json、图片生成/图生图/MOSS一键洗图2K极速版｜角色设计人像图生图快速提质_2113587567160549377.json、图片生成/图生图/MOSS图生图2K极速洗图 一键美化写实处理工具_2114100330920243202.json、图片生成/图生图/MOSS图生图2K极速版 风格化图像转换处理生成工具_2113026391880069122.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 29 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 28/29 个有
- `孤海注释` —— 28/29 个有
- `TextGenerate` —— 27/29 个有
- `LoadImage` —— 23/29 个有
- `ImageConcatMulti` —— 21/29 个有
- `PreviewImage` —— 9/29 个有
- `CR Prompt Text` —— 4/29 个有
- `SkipLayerGuidanceDiTSimple` —— 2/29 个有
- `FastGroupsBypassSwitch` —— 1/29 个有
- `FluxKontextImageScale` —— 1/29 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/29 个有
- `Krea2OstrisEditModelPatch` —— 1/29 个有
- `PreviewAny` —— 1/29 个有
- `ReferenceMultiLatent` —— 1/29 个有
- `TextEncodeKrea2OstrisEdit` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 29 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 29 | 100% |
| 采样算法 | er_sde | - | 29 | 100% |
| 调度器 | beta | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |
| 宽度 | 80 | 80 - 80 | 29 | 100% |
| 高度 | 80 | 80 - 80 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，29 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，29 个样本，一致性 100%
- 调度器 最常用 beta，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高发问题（30/29 个样本）：Steps较低可能导致细节不足
