---
name: unknown_workflow_sampler_clip_unet_47
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.8525
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1 超清人像 Z-image turbo_2071175125273239553.json, 图片生成/文生图/1-图像生成 (T2I) Z-Image Turbo_ Fast Image 工作流_2053392780503859202.json, 图片生成/文生图/12月最新文生图 Qwen 2512 标准模型非FP8_2007791461693136897.json, 图片生成/文生图/19.Z-image 文生图_2079606575005790210.json, 图片生成/文生图/1953065521521618946.json, 图片生成/文生图/1955336945507471361.json, 图片生成/文生图/AI口播人物-文生图_2027299018845458433.json, 图片生成/文生图/Qwen-Image-LLM计算工作流-计算器_2009215925676937218.json, 图片生成/文生图/中文书法字体设计 -文生图-中文字体logo-书法字体设计-艺术字_2021848205499043842.json, 图片生成/文生图/千问Qwen-image中文书法字体设计 - 媲美即梦_2002775003546415106.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1 超清人像 Z-image turbo_2071175125273239553.json、图片生成/文生图/1-图像生成 (T2I) Z-Image Turbo_ Fast Image 工作流_2053392780503859202.json、图片生成/文生图/12月最新文生图 Qwen 2512 标准模型非FP8_2007791461693136897.json、图片生成/文生图/19.Z-image 文生图_2079606575005790210.json、图片生成/文生图/1953065521521618946.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 9/10 个有
- `ModelSamplingAuraFlow` —— 9/10 个有
- `ConditioningZeroOut` —— 7/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `easy showAnything` —— 6/10 个有
- `CR SDXL Aspect Ratio` —— 4/10 个有
- `Text Multiline` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `JWInteger` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `Qwen3_VQA_Plus` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 1 - 50 | 10 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 10 | 53% |
| 采样算法 | euler | - | 10 | 60% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 1 - 50，10 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（6/10 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR SDXL Aspect Ratio
