---
name: text_to_image_lora_sampler_clip_72
type: Text To Image
frequency: 12
level: strong
coverage: 0.887833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2102218247461490690.json, 图片生成/图生图/2102563638816104449.json, 图片生成/文生图/BF16精度Qwen Image 2.1文生图，小字不崩高质量文字渲染工作流_2102872573246791681.json, 图片生成/文生图/BF16精度Qwen_Image_2.1文生图，小字不崩高质量文字渲染工作流_2105503929613250561.json, 图片生成/文生图/Krea2特定风格人像大作文生图｜固定风格批量出人像大片_2099133481472315394.json, 图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json, 图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json, 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json, 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2105438700263006209.json, 图片生成/文生图/Qwen2.1文图生图提示词增强工作流，文生图人像写真图生图处理方案_2107586964294815746.json, 图片生成/文生图/Qwen2.1文生图提示词增强版｜人像写真质感拉满，出图更精致_2104540403243507714.json, 图片生成/文生图/Qwen_Image_2.1文生图｜官方PE参数 老许Gary出品海报制作利器_2105515254531837953.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2102218247461490690.json、图片生成/图生图/2102563638816104449.json、图片生成/文生图/BF16精度Qwen Image 2.1文生图，小字不崩高质量文字渲染工作流_2102872573246791681.json、图片生成/文生图/BF16精度Qwen_Image_2.1文生图，小字不崩高质量文字渲染工作流_2105503929613250561.json、图片生成/文生图/Krea2特定风格人像大作文生图｜固定风格批量出人像大片_2099133481472315394.json…）

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
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 11/12 个有
- `孤海注释` —— 11/12 个有
- `TextEncodeQwenImage21` —— 10/12 个有
- `ConditioningZeroOut` —— 7/12 个有
- `TextGenerate` —— 7/12 个有
- `PreviewImage` —— 6/12 个有
- `StringConstantMultiline` —— 5/12 个有
- `CR Prompt Text` —— 4/12 个有
- `SaveImageAdvanced` —— 4/12 个有
- `easy clearCacheAll` —— 4/12 个有
- `PreviewAny` —— 3/12 个有
- `EmptyImage` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `LoadImage` —— 1/12 个有
- `ModelAttentionBackend` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `easy ifElse` —— 1/12 个有
- `easy saveText` —— 1/12 个有

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
| Steps较低可能导致细节不足 | 15/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（15/12 个样本）：Steps较低可能导致细节不足
