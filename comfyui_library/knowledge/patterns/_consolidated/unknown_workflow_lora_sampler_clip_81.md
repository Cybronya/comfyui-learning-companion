---
name: unknown_workflow_lora_sampler_clip_81
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.817
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, String Literal, Seed (rgthree), Text Multiline]
members: [图片生成/文生图/1983097610955333634.json, 图片生成/文生图/1983138603914174466.json, 图片生成/文生图/1984498747142979586.json, 图片生成/文生图/一字马-300张Lora-洗图工作流_1994669431991246850.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1983097610955333634.json、图片生成/文生图/1983138603914174466.json、图片生成/文生图/1984498747142979586.json、图片生成/文生图/一字马-300张Lora-洗图工作流_1994669431991246850.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `String Literal` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `TextEncodeQwenImageEdit` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | 4 - 30 | 4 | 24% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 40% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，观测区间 4 - 30，4 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM V2、String Literal、Seed (rgthree)、Text Multiline
