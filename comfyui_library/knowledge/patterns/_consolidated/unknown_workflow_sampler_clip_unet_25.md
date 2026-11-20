---
name: unknown_workflow_sampler_clip_unet_25
type: Unknown Workflow
frequency: 23
level: weak
coverage: 0.856913
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/kera-2 文生图 _ 图生图 + gemma4 自动提示词工作流_2072549485133262849.json, 图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json, 图片生成/文生图/qwen_image工作流_1991713723383640065.json, 图片生成/文生图/qwen高级风格场景_2106951966848016385.json, 图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流 1_2028298601872494594.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流 3_2028289669758197762.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流_2019406284654645249.json, 图片生成/文生图/z-image base 水墨风 文生图 工作流_2028276810034712577.json, 图片生成/文生图/z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817.json, 图片生成/文生图/zimage_turbo+lora 基础工作流_2084827520289038337.json, 图片生成/文生图/【老金驿站】Qwen真实系列Lora工作流_1977995730776379394.json, 图片生成/文生图/【遇见AI】flux3 image 蒸馏版文生图基础流_2111000814536978434.json, 图片生成/文生图/自动词优化Moss-image Sft fixed文生图-低显存版_2112824054842486786.json, 平台全量/MOSS图生图  洗图 一键洗图  2K极速版_2117595753035161601.json, 平台全量/MOSS图生图  洗图 一键洗图  2K极速版_2118031904959188994.json, 平台全量/MOSS图生图  洗图 一键洗图  2K极速版_2118303838057885698.json, 平台全量/MOSS图生图  洗图 一键洗图  2K极速版_2118304198310842369.json, 平台全量/MOSS图生图  洗图 一键洗图  2K极速版_2118315051634479105.json, 平台全量/MOSS图生图  洗图 一键洗图  2K极速版_2118322452462915585.json, 平台全量/MOSS图生图  洗图 一键洗图  2K极速版_2118322952805634049.json, 平台全量/MOSS图生图_洗图_一键洗图_2K极速版_2117905540830556162.json, 平台全量/图生图  MOSS  洗图 一键洗图  2K极速版_2117535315412996097.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/文生图/kera-2 文生图 _ 图生图 + gemma4 自动提示词工作流_2072549485133262849.json、图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json、图片生成/文生图/qwen_image工作流_1991713723383640065.json、图片生成/文生图/qwen高级风格场景_2106951966848016385.json、图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 21/23 个有
- `LoadImage` —— 14/23 个有
- `EmptySD3LatentImage` —— 12/23 个有
- `ResolutionSelector` —— 12/23 个有
- `TextGenerate` —— 12/23 个有
- `EmptyFlux2LatentImage` —— 11/23 个有
- `ModelSamplingAuraFlow` —— 11/23 个有
- `PrimitiveStringMultiline` —— 11/23 个有
- `ImageConcatMulti` —— 9/23 个有
- `PreviewImage` —— 2/23 个有
- `ShowText|pysssss` —— 2/23 个有
- `PreviewAny` —— 1/23 个有
- `StringConcatenate` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 50 | 23 | 32% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 4 | 23 | 47% |
| 采样算法 | euler | - | 23 | 91% |
| 调度器 | simple | - | 23 | 57% |
| 重绘幅度 | 1 | 0.15 - 1 | 23 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 50，23 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 4，23 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，23 个样本，一致性 91%
- 调度器 最常用 simple，23 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，23 个样本，取值集中（一致性 82%）
