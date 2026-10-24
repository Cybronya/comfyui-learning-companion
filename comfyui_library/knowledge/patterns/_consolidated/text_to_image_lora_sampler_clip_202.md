---
name: text_to_image_lora_sampler_clip_202
type: Text To Image
frequency: 9
level: strong
coverage: 0.876
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/心然·寻源Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102218247461490690.json, 图片生成/文生图/Bkz人像摄影应用｜krea2-turbo-bf16人物特效文生图_2095790317579620353.json, 图片生成/文生图/Krea2人像摄影应用｜turbo-bf16写实人像生成_2095562706337230850.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102097450449326081.json, 图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json, 图片生成/文生图/Qwen Image 2.1空间折叠流太虚生成，简洁连线文生图傻瓜操作方案_2103612146377641986.json, 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2104764071617851393.json, 图片生成/文生图/Qwen2.1提示词增强文生图 写实画面质量跃升_2105438700263006209.json, 图片生成/文生图/Qwen2.1文图生图提示词增强工作流，文生图人像写真图生图处理方案_2107586964294815746.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_202

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/心然·寻源Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102218247461490690.json、图片生成/文生图/Bkz人像摄影应用｜krea2-turbo-bf16人物特效文生图_2095790317579620353.json、图片生成/文生图/Krea2人像摄影应用｜turbo-bf16写实人像生成_2095562706337230850.json、图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102097450449326081.json、图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 8/9 个有
- `TextEncodeQwenImage21` —— 7/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `StringConstantMultiline` —— 4/9 个有
- `TextGenerate` —— 4/9 个有
- `easy clearCacheAll` —— 3/9 个有
- `GetNode` —— 2/9 个有
- `KSamplerAdvanced` —— 2/9 个有
- `LatentUpscaleBy` —— 2/9 个有
- `ModelSamplingAuraFlow` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `ImpactInt` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `Text` —— 1/9 个有
- `easy saveText` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
