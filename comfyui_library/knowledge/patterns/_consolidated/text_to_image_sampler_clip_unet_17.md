---
name: text_to_image_sampler_clip_unet_17
type: Text To Image
frequency: 18
level: weak
coverage: 0.908444
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/API - FLux文生图_2066848618040086529.json, 图片生成/文生图/API - FLux文生图_2091105641225080833.json, 图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json, 图片生成/文生图/Boogu_Turbo 文生图_2069444653648273409.json, 图片生成/文生图/Boogu_Turbo_文生图工作流_2069274849616416770.json, 图片生成/文生图/Boogu文生图标准版_2068941708238352385.json, 图片生成/文生图/FLUX 2 文生图_1993572229503975426.json, 图片生成/文生图/FLUX 2 电商文生图场景图_2043508628937777153.json, 图片生成/文生图/FLux文生图API工作流｜高质量图像生成_2095581101854121986.json, 图片生成/文生图/Flux3-klein文生图PUP增强版｜提示词强化出图更细腻_2111742110876659714.json, 图片生成/文生图/Flux3-klein文生图PUP增强，创意形象高清直出_2111907847557697538.json, 图片生成/文生图/MOSS Sft 角色设计文生图｜NB级角色创意直出_2112375262431244289.json, 图片生成/文生图/MOSS sft Comfyui官方流｜原汁原味官方文生图_2112425060618297345.json, 图片生成/文生图/MOSS 文生图新秀｜数字人全能助手一键出图_2112373662857908225.json, 图片生成/文生图/flux3-image-klein文生图，高清创意形象直出_2111580915750236161.json, 图片生成/文生图/flux3_image_klein文生图，创意形象高效直出_2111545656975384578.json, 图片生成/文生图/flux3_image_klein文生图｜学AI曹同学同款直出流_2111340043469156354.json, 图片生成/文生图/自动词优化版Moss-image Sft文生图｜描述更省心_2112412795026370562.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/API - FLux文生图_2066848618040086529.json、图片生成/文生图/API - FLux文生图_2091105641225080833.json、图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json、图片生成/文生图/Boogu_Turbo 文生图_2069444653648273409.json、图片生成/文生图/Boogu_Turbo_文生图工作流_2069274849616416770.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 16/18 个有
- `PrimitiveStringMultiline` —— 13/18 个有
- `ConditioningZeroOut` —— 10/18 个有
- `JjkText` —— 10/18 个有
- `LoraLoaderModelOnly` —— 10/18 个有
- `solarL_SaveImagesToZip` —— 10/18 个有
- `孤海注释` —— 10/18 个有
- `EmptyFlux2LatentImage` —— 9/18 个有
- `TextGenerate` —— 9/18 个有
- `PreviewAny` —— 7/18 个有
- `ResolutionSelector` —— 7/18 个有
- `FluxGuidance` —— 5/18 个有
- `DualCLIPLoader` —— 3/18 个有
- `LoraLoader` —— 3/18 个有
- `SkipLayerGuidanceDiTSimple` —— 3/18 个有
- `easy int` —— 3/18 个有
- `FastGroupsBypassSwitch` —— 2/18 个有
- `PreviewImage` —— 2/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1536 | 18 | 0% |
| 高度 | 80 | 80 - 1920 | 18 | 0% |
| 采样步数 | 4 | 4 - 50 | 18 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 18 | 49% |
| 采样算法 | er_sde | - | 18 | 56% |
| 调度器 | beta | - | 18 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1536，18 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，18 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 50，18 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，18 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 er_sde，18 个样本，一致性 56%
- 调度器 最常用 beta，18 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（17/18 个样本）：Steps较低可能导致细节不足
