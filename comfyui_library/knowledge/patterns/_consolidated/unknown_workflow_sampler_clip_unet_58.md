---
name: unknown_workflow_sampler_clip_unet_58
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.831867
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/kera-2 文生图 _ 图生图 + gemma4 自动提示词工作流_2072549485133262849.json, 图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json, 图片生成/文生图/qwen_image工作流_1991713723383640065.json, 图片生成/文生图/qwen高级风格场景_2106951966848016385.json, 图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流 1_2028298601872494594.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流 3_2028289669758197762.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流_2019406284654645249.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流_2028276810034712577.json, 图片生成/文生图/z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817.json, 图片生成/文生图/zimage_turbo+lora 基础工作流_2084827520289038337.json, 图片生成/文生图/【老金驿站】Qwen真实系列Lora工作流_1977995730776379394.json, 图片生成/文生图/【遇见AI】flux3 image 蒸馏版文生图基础流_2111000814536978434.json, 图片生成/文生图/一字马-300张Lora-洗图工作流_1994669431991246850.json, 图片生成/文生图/极致真实的人像质感(Qwen Image 文生图）_1984498747142979586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/kera-2 文生图 _ 图生图 + gemma4 自动提示词工作流_2072549485133262849.json、图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json、图片生成/文生图/qwen_image工作流_1991713723383640065.json、图片生成/文生图/qwen高级风格场景_2106951966848016385.json、图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 14/15 个有
- `LoraLoaderModelOnly` —— 14/15 个有
- `ModelSamplingAuraFlow` —— 13/15 个有
- `LoadImage` —— 6/15 个有
- `ShowText|pysssss` —— 4/15 个有
- `AILab_QwenVL` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `ResolutionSelector` —— 2/15 个有
- `Text Multiline` —— 2/15 个有
- `TextGenerate` —— 2/15 个有
- `EmptyFlux2LatentImage` —— 1/15 个有
- `PrimitiveStringMultiline` —— 1/15 个有
- `StringConcatenate` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 50 | 15 | 48% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 15 | 52% |
| 采样算法 | euler | - | 15 | 80% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 0.15 - 1 | 15 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 50，15 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 80%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，15 个样本
