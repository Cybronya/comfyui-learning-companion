---
name: text_to_image_lora_sampler_clip_64
type: Text To Image
frequency: 12
level: strong
coverage: 0.889583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2102218247461490690.json, 图片生成/图生图/2102563638816104449.json, 图片生成/文生图/BF16精度Qwen Image 2.1文生图，小字不崩高质量文字渲染工作流_2102872573246791681.json, 图片生成/文生图/BF16精度Qwen_Image_2.1文生图，小字不崩高质量文字渲染工作流_2105503929613250561.json, 图片生成/文生图/Qwen Image 2.1文生图 官方模板，原生2K高清文本到图像方案_2103550536535601154.json, 图片生成/文生图/Qwen Image 2.1文生图 高质量画面直出_2105349045723160578.json, 图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json, 图片生成/文生图/Qwen2.1_BF16官方文生图工作流｜海报制作字体设计一次到位_2104058681204764674.json, 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json, 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2105438700263006209.json, 图片生成/文生图/Qwen2.1文生图带提示词增强高清放大精干版，数字人文生图方案_2103559733838962690.json, 图片生成/文生图/Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2102218247461490690.json、图片生成/图生图/2102563638816104449.json、图片生成/文生图/BF16精度Qwen Image 2.1文生图，小字不崩高质量文字渲染工作流_2102872573246791681.json、图片生成/文生图/BF16精度Qwen_Image_2.1文生图，小字不崩高质量文字渲染工作流_2105503929613250561.json、图片生成/文生图/Qwen Image 2.1文生图 官方模板，原生2K高清文本到图像方案_2103550536535601154.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/12 个有
- `SaveImageAdvanced` —— 6/12 个有
- `TextGenerate` —— 6/12 个有
- `ConditioningZeroOut` —— 5/12 个有
- `StringConstantMultiline` —— 5/12 个有
- `PreviewImage` —— 4/12 个有
- `easy clearCacheAll` —— 4/12 个有
- `CR Prompt Text` —— 3/12 个有
- `EmptyImage` —— 2/12 个有
- `ImageScaleBy` —— 2/12 个有
- `SeedVR2LoadDiTModel` —— 2/12 个有
- `SeedVR2LoadVAEModel` —— 2/12 个有
- `SeedVR2VideoUpscaler` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
