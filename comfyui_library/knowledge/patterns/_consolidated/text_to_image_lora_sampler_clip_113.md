---
name: text_to_image_lora_sampler_clip_113
type: Text To Image
frequency: 13
level: strong
coverage: 0.912923
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098986502435991553.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2099662369931751426.json, 图片生成/文生图/MOSS文生图2K极速版工作流，美少女写实风一键生成高清图_2117104532936286209.json, 图片生成/文生图/MOSS文生图2K极速版文生图｜美少女写实风出图不限量_2114275926564491266.json, 图片生成/文生图/MOSS文生图2K极速版，人物更真实皮肤质感自然高清直出_2114452341444403202.json, 图片生成/文生图/MOSS文生图2K极速版，美少女写实风格一键直出高清图片_2114484676936159233.json, 图片生成/文生图/MOSS文生图2K极速版，美少女写实风格一键直出高清图片_2116818940981760002.json, 图片生成/文生图/MOSS文生图2K极速版｜美少女写实文生图秒出_2114049430289731586.json, 图片生成/文生图/MOSS文生图2K极速版｜美少女写实风格快速出图体验_2113579003356471297.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2103558268332363777.json, 图片生成/文生图/Qwen Image 2.1文生图标准版 高质量画面稳定出图_2105033394219474945.json, 图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json, 图片生成/文生图/Qwen2.1_BF16官方文生图工作流｜海报制作字体设计一次到位_2104058681204764674.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098986502435991553.json、图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2099662369931751426.json、图片生成/文生图/MOSS文生图2K极速版工作流，美少女写实风一键生成高清图_2117104532936286209.json、图片生成/文生图/MOSS文生图2K极速版文生图｜美少女写实风出图不限量_2114275926564491266.json、图片生成/文生图/MOSS文生图2K极速版，人物更真实皮肤质感自然高清直出_2114452341444403202.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
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
- `ResolutionSelector` —— 11/13 个有
- `PreviewImage` —— 9/13 个有
- `CR Text` —— 8/13 个有
- `孤海注释` —— 8/13 个有
- `EmptyFlux2LatentImage` —— 7/13 个有
- `TextEncodeQwenImage21` —— 4/13 个有
- `PathchSageAttentionKJ` —— 3/13 个有
- `EmptyImage` —— 2/13 个有
- `ModelSamplingAuraFlow` —— 2/13 个有
- `QwenImage21Cache` —— 2/13 个有
- `easy loraStack` —— 2/13 个有
- `easy loraStackApply` —— 2/13 个有
- `SaveImageAdvanced` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（22/13 个样本）：Steps较低可能导致细节不足
