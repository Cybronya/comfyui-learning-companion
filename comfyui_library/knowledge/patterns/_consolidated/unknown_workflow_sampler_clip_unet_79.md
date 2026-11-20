---
name: unknown_workflow_sampler_clip_unet_79
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.794462
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image 图生图 支持中文字体_1990712081664139265.json, 图片生成/图生图/Qwen-Image创意字体，一键直出-图生图_2008858589422690305.json, 图片生成/图生图/中文字体设计Qwen-Image图生图_2019564571903660034.json, 图片生成/文生图/Qwen-Image文生图 中文书法字体标题设计_1953729540789075969.json, 图片生成/文生图/中文字体设计  -  Qwen-Image图生图_1955892796286795777.json, 图片生成/文生图/中文字体设计 - 媲美即梦 -  Qwen-Image图生图_1953067660055613442.json, 图片生成/文生图/中秋节文字一键生成 - Qwen-Image文生图_1970162502074068993.json, 图片生成/文生图/双11大促活动字体一键生成 Qwen-Image文生图_1973238135855386626.json, 图片生成/文生图/双11年终大促+-+活动字体一键成_1970152346649063426.json, 图片生成/文生图/高级感艺术字生成（自带提示词模板）_1972314392975110146.json, 平台全量/QWen-Image中文字体设计_1954943735462182913.json, 平台全量/Qwen-千问多字体直出-字体设计 中文字体设计 - 媲美即梦 -  Qwen-Image图生图_1991742119616393218.json, 平台全量/字体设计，一键直出_1985917018920628225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen-Image 图生图 支持中文字体_1990712081664139265.json、图片生成/图生图/Qwen-Image创意字体，一键直出-图生图_2008858589422690305.json、图片生成/图生图/中文字体设计Qwen-Image图生图_2019564571903660034.json、图片生成/文生图/Qwen-Image文生图 中文书法字体标题设计_1953729540789075969.json、图片生成/文生图/中文字体设计  -  Qwen-Image图生图_1955892796286795777.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/13 个有
- `Text Multiline` —— 12/13 个有
- `easy showAnything` —— 12/13 个有
- `Int` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `RH_Captioner` —— 11/13 个有
- `ImpactSwitch` —— 10/13 个有
- `PrimitiveBoolean` —— 10/13 个有
- `easy ifElse` —— 10/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/13 个有
- `FluxResolutionNode` —— 5/13 个有
- `CR Text Replace` —— 4/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `PreviewImage` —— 4/13 个有
- `Prompt_Text` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 13 | 87% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 4 | 13 | 85% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，13 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 4，13 个样本，取值集中（一致性 85%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
