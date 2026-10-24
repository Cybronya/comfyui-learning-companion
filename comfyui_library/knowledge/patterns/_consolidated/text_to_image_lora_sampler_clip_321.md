---
name: text_to_image_lora_sampler_clip_321
type: Text To Image
frequency: 6
level: strong
coverage: 0.8985
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen2.1_BF16官方文生图工作流｜海报制作字体设计一次到位_2104058681204764674.json, 图片生成/文生图/Qwen2.1文生图写实风格 照片级质感画面直出_2105475614315737089.json, 图片生成/文生图/Qwen2.1文生图提示词增强版｜人像写真质感拉满，出图更精致_2104540403243507714.json, 图片生成/文生图/Qwen_Image_2.1文生图｜官方PE参数 老许Gary出品海报制作利器_2105515254531837953.json, 图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102320781945561089.json, 图片生成/文生图/千问2.1文生图片支持透明底｜文生图海报制作 商品换背景好帮手_2104051581292466177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_321

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen2.1_BF16官方文生图工作流｜海报制作字体设计一次到位_2104058681204764674.json、图片生成/文生图/Qwen2.1文生图写实风格 照片级质感画面直出_2105475614315737089.json、图片生成/文生图/Qwen2.1文生图提示词增强版｜人像写真质感拉满，出图更精致_2104540403243507714.json、图片生成/文生图/Qwen_Image_2.1文生图｜官方PE参数 老许Gary出品海报制作利器_2105515254531837953.json、图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102320781945561089.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
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
- `TextEncodeQwenImage21` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `EmptyImage` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `SaveImageAdvanced` —— 2/6 个有
- `TextGenerate` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `StringConstantMultiline` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
