---
name: unknown_workflow_sampler_clip_unet_66
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.916444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ideogram4-Instant KJ_2078288747602464770.json, 图片生成/文生图/KJ结构化提示_FAST单模型_2078065107753590786.json, 图片生成/文生图/KJ结构化提示_Instant单模型_2077705321124028417.json, 图片生成/文生图/Krea2双采+高分辨修复_2084950880146771969.json, 图片生成/文生图/qwen_image2512+lora8步_2009428030506143746.json, 图片生成/文生图/日系街拍套图生成器-jpset工作流_2095424852239929346.json, 图片生成/文生图/暗调夜景街拍生成器-nightset工作流_2095497922401099778.json, 图片生成/文生图/穿戴甲详情页批量直出工作流_2094422991236059137.json, 图片生成/文生图/街拍套图稳定器-streetset工作流_2095309050455089154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Ideogram4-Instant KJ_2078288747602464770.json、图片生成/文生图/KJ结构化提示_FAST单模型_2078065107753590786.json、图片生成/文生图/KJ结构化提示_Instant单模型_2077705321124028417.json、图片生成/文生图/Krea2双采+高分辨修复_2084950880146771969.json、图片生成/文生图/qwen_image2512+lora8步_2009428030506143746.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 6/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `CFGOverride` —— 3/9 个有
- `Ideogram4PromptBuilderKJ` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `LatentUpscaleBy` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 26 | 8 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 8 | 27% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | normal | - | 8 | 50% |
| 重绘幅度 | 1 | 0.45 - 1 | 8 | 80% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 6 | 92% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 6 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 26，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 normal，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.45 - 1，8 个样本，取值集中（一致性 80%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，6 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，6 个样本，取值集中（一致性 92%）
