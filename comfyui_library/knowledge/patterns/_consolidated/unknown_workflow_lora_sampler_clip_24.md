---
name: unknown_workflow_lora_sampler_clip_24
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.915333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image抖音小红书爆款涨粉美女_2011359697030352898.json, 图片生成/文生图/(2秒采样极速版)Qwen Image 4步文生图V1_1958755445714345985.json, 图片生成/文生图/(z base)纸艺风格lora测试生图工作流_2016907094099759106.json, 图片生成/文生图/(贞贞版)Z-image Base Distilled蒸馏加速版_2019080504754049025.json, 图片生成/文生图/01-01-02-QwenImage-基础文生图-2512版_2007006077161836545.json, 图片生成/文生图/2512抖音美女真实生活照爆款涨粉合集_2010620930929729537.json, 图片生成/文生图/Qwen Image 2512手动提示词文生图V1_2006339793495531522.json, 图片生成/文生图/Qwen Image 2512手动提示词文生图_2007697399430520834.json, 图片生成/文生图/Qwen Image 2512智能扩写文生图V1_2006338997970276354.json, 图片生成/文生图/Qwen Image 2512智能扩写文生图不带高清放大节点_2007696454147641345.json, 图片生成/文生图/Qwen Image手动提示词文生图-Bf16+lihgning版_2006647725940547586.json, 图片生成/文生图/Qwen2512 Vs Qwen Old Vs Z-image横向对比流_2006547512198434818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Z-image抖音小红书爆款涨粉美女_2011359697030352898.json、图片生成/文生图/(2秒采样极速版)Qwen Image 4步文生图V1_1958755445714345985.json、图片生成/文生图/(z base)纸艺风格lora测试生图工作流_2016907094099759106.json、图片生成/文生图/(贞贞版)Z-image Base Distilled蒸馏加速版_2019080504754049025.json、图片生成/文生图/01-01-02-QwenImage-基础文生图-2512版_2007006077161836545.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 11/12 个有
- `ModelSamplingAuraFlow` —— 11/12 个有
- `CFGNorm` —— 8/12 个有
- `LayerUtility: PurgeVRAM` —— 8/12 个有
- `UNETLoader` —— 8/12 个有
- `easy showAnything` —— 7/12 个有
- `RH_LLMAPI_NODE` —— 5/12 个有
- `UnetLoaderGGUF` —— 4/12 个有
- `ConditioningZeroOut` —— 2/12 个有
- `ConcatTextOfUtils` —— 1/12 个有
- `KOOK_ImageCompression` —— 1/12 个有
- `KOOK_SaveJPGImage` —— 1/12 个有
- `LayerUtility: ImageReel` —— 1/12 个有
- `LayerUtility: ImageReelComposit` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `Textbox` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 12 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 12 | 34% |
| 采样算法 | res_2s | - | 12 | 50% |
| 调度器 | beta57 | - | 12 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，12 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，12 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 res_2s，12 个样本，一致性 50%
- 调度器 最常用 beta57，12 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（10/12 个样本）：Steps较低可能导致细节不足
