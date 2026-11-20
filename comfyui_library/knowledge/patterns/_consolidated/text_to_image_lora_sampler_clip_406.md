---
name: text_to_image_lora_sampler_clip_406
type: Text To Image
frequency: 5
level: strong
coverage: 0.9138
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen image 2.1文生图稳定版｜中文语义理解到位｜长句描述也不崩_2102287119891918849.json, 图片生成/文生图/Qwen2.1 BF16官方文生图工作流｜海报制作字体设计一次到位_2102219743238385666.json, 图片生成/文生图/qwen image2.1文生图利器｜数字人海报制作一步搞定_2104529003418836993.json, 图片生成/文生图/qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090.json, 图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102267329873801217.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_406

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1文生图稳定版｜中文语义理解到位｜长句描述也不崩_2102287119891918849.json、图片生成/文生图/Qwen2.1 BF16官方文生图工作流｜海报制作字体设计一次到位_2102219743238385666.json、图片生成/文生图/qwen image2.1文生图利器｜数字人海报制作一步搞定_2104529003418836993.json、图片生成/文生图/qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090.json、图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102267329873801217.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 4/5 个有
- `SaveImageAdvanced` —— 4/5 个有
- `AnySwitch` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `Seed Generator` —— 1/5 个有
- `easy batchAnything` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
