---
name: unknown_workflow_sampler_clip_unet_21
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.906
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen-image2512-8步-BF16+Z-image去AII感一体流_2008885693623308290.json, 图片生成/文生图/qwen-文生图_2090010243379060737.json, 图片生成/文生图/qwen2512-qwen-lora-文生图工作流_2008018384633466881.json, 图片生成/文生图/qwen2512文生图工作流_2068284987354476546.json, 图片生成/文生图/qwen_image2512+lora8步_2009428030506143746.json, 图片生成/文生图/qwen_image工作流_1991713723383640065.json, 图片生成/文生图/qwen_image文生图+lora8步_1955214645163278337.json, 图片生成/文生图/qwen出图对比（4步vs8步）_1955869888814436354.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流 1_2028298601872494594.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流 3_2028289669758197762.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流_2019406284654645249.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流_2028276810034712577.json, 图片生成/文生图/zimage_turbo+lora 基础工作流_2084827520289038337.json, 图片生成/文生图/【提速2倍】Qwen-Image-Lightning 8步加速文生图v2_1953283718866792449.json, 图片生成/文生图/【老金驿站】Qwen真实系列Lora工作流_1977995730776379394.json, 图片生成/文生图/千问-qwen-lora-文生图工作流_1960181642029641729.json, 图片生成/文生图/千问文生图_1985959773130633217.json, 图片生成/文生图/千问文生图快速中文直出2512_2027699940423639041.json, 图片生成/文生图/古风男工作流_2051554347225497601.json, 图片生成/文生图/小红书风格加黑丝_2003393169008041986.json, 图片生成/文生图/帝企鹅工作流_1980164055954526209.json, 图片生成/文生图/文生图 硕阳_2016782171092029441.json, 图片生成/文生图/文生图-Qwen2512-6步-模板_2023584055270313986.json, 图片生成/文生图/简单手绘风格_1962501732217536513.json, 图片生成/文生图/高质量双采样_RH版_v1_2019943536841461761.json, 视频生成/图生视频/image_qwen_image_deal_halftone_1990232206792683522.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/qwen-image2512-8步-BF16+Z-image去AII感一体流_2008885693623308290.json、图片生成/文生图/qwen-文生图_2090010243379060737.json、图片生成/文生图/qwen2512-qwen-lora-文生图工作流_2008018384633466881.json、图片生成/文生图/qwen2512文生图工作流_2068284987354476546.json、图片生成/文生图/qwen_image2512+lora8步_2009428030506143746.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 24/26 个有
- `LoraLoaderModelOnly` —— 20/26 个有
- `LoraLoader` —— 9/26 个有
- `Image Comparer (rgthree)` —— 2/26 个有
- `ImageScaleBy` —— 2/26 个有
- `VAEEncode` —— 2/26 个有
- `INTConstant` —— 1/26 个有
- `MemoryCleaner` —— 1/26 个有
- `VAEUtils_CustomVAELoader` —— 1/26 个有
- `VAEUtils_VAEDecodeTiled` —— 1/26 个有
- `easy cleanGpuUsed` —— 1/26 个有
- `easy clearCacheAll` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 26 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 26 | 33% |
| 采样算法 | euler | - | 26 | 81% |
| 调度器 | simple | - | 26 | 69% |
| 重绘幅度 | 1 | 0.19 - 1 | 26 | 80% |
| LoRA 模型强度 | 1 | 0.8 - 1.5 | 9 | 79% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，26 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，26 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，26 个样本，一致性 81%
- 调度器 最常用 simple，26 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 0.19 - 1，26 个样本
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1.5，9 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（19/26 个样本）：Steps较低可能导致细节不足
