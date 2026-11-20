---
name: text_to_image_lora_sampler_clip_202
type: Text To Image
frequency: 9
level: strong
coverage: 0.886667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2局部重绘PS版工作流｜提示词反推写实图生图_2097491218342178818.json, 图片生成/图生图/LEON 产品精修｜图生图商品图一键出高级感 商详必备_2097581380665438210.json, 图片生成/图生图/LEON 无损放大｜细节恢复加肌理强化 图生图画质起飞_2097573526676000770.json, 图片生成/图生图/Qwen Image 2.1图像编辑最新版 透明抠图换背景工具_2113383323958595585.json, 图片生成/图生图/Qwen image 2.1一键模特换装｜服装迁移试衣黑科技｜电商换装省成本_2112088875962290178.json, 图片生成/图生图/Qwen-Image-2.1一键抠图，产品换背景透明底直出_2111571619721338881.json, 图片生成/图生图/Qwen-image2.1图像高清修复，老图翻新细节重建_2112296348044316674.json, 图片生成/图生图/Qwen-image2.1服装迁移，图生图款式面料高还原_2112294809196126209.json, 图片生成/图生图/Qwen-image2.1角色多角度lora，图生图同一角色随心转面_2112301019328761857.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_202

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Krea2局部重绘PS版工作流｜提示词反推写实图生图_2097491218342178818.json、图片生成/图生图/LEON 产品精修｜图生图商品图一键出高级感 商详必备_2097581380665438210.json、图片生成/图生图/LEON 无损放大｜细节恢复加肌理强化 图生图画质起飞_2097573526676000770.json、图片生成/图生图/Qwen Image 2.1图像编辑最新版 透明抠图换背景工具_2113383323958595585.json、图片生成/图生图/Qwen image 2.1一键模特换装｜服装迁移试衣黑科技｜电商换装省成本_2112088875962290178.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 6/9 个有
- `Int` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `RHHiddenNodes` —— 4/9 个有
- `QwenImage21Cache` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `GoogleTranslator` —— 1/9 个有
- `KSamplerAdvanced` —— 1/9 个有
- `TextInput_` —— 1/9 个有
- `VAEEncode` —— 1/9 个有
- `ttN int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
