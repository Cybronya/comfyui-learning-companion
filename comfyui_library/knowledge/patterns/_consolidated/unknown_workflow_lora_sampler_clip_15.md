---
name: unknown_workflow_lora_sampler_clip_15
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.86125
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Replace, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, ProcessString, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/图生图/极致美学文生图提升构图+真实性_1994236855046651906.json, 图片生成/文生图/Z Image：极致写实图像，抖音小红书洗图，一键就能拥有，反推出图，文生图，极致美学文生图（完美构_2036281015341158401.json, 图片生成/文生图/大凯辰光-极致美学参考图反推+文生图-9宫格直出-工作流_2009588663545503746.json, 图片生成/文生图/大凯辰光-极致美学参考图反推+文生图-9宫格直出-工作流自用_2014134484735627265.json, 图片生成/文生图/大凯辰光-极致美学文生图-（9宫格直出）提升构图及真实性工作流_2009552798479814658.json, 图片生成/文生图/批量生成极致真实人像 提升美学质感 提升氛围感 QWEN+Z image turbo 自动提示词创意_2053490147555061762.json, 图片生成/文生图/极致真实人像V2.0（提升美学）_2008839119325110273.json, 图片生成/文生图/极致真实人像摄影V1.0_2009073989850767361.json, 图片生成/文生图/极致美学 文生图（提升构图+真实性）_2008535816078888962.json, 图片生成/文生图/极致美学文生图-提升构图+真实性_2007814565563736066.json, 图片生成/文生图/极致美学文生图（完美构图+真实性）_2031969796539027457.json, 图片生成/文生图/极致美学文生图（提升构图+真实性）V4.0_1993873613419905026.json, 图片生成/文生图/极致美学文生图（提升构图+真实性）V5.0_1993948868719165441.json, 图片生成/文生图/极致美学文生图（提升构图+真实性）V5.0_2001899008475951105.json, 图片生成/文生图/极致美学文生图（提升构图+真实性）V6.0_1994216495739846658.json, 图片生成/文生图/电影质感真实人像V1.0_2009482138478977026.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/极致美学文生图提升构图+真实性_1994236855046651906.json、图片生成/文生图/Z Image：极致写实图像，抖音小红书洗图，一键就能拥有，反推出图，文生图，极致美学文生图（完美构_2036281015341158401.json、图片生成/文生图/大凯辰光-极致美学参考图反推+文生图-9宫格直出-工作流_2009588663545503746.json、图片生成/文生图/大凯辰光-极致美学参考图反推+文生图-9宫格直出-工作流自用_2014134484735627265.json、图片生成/文生图/大凯辰光-极致美学文生图-（9宫格直出）提升构图及真实性工作流_2009552798479814658.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Replace`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/16 个有
- `SetNode` —— 3/16 个有
- `AILab_QwenVL` —— 2/16 个有
- `Display Any (rgthree)` —— 2/16 个有
- `LoadImage` —— 2/16 个有
- `PreviewAny` —— 2/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 16 | 100% |
| 高度 | 1920 | 1920 - 1920 | 16 | 100% |
| 采样步数 | randomize | - | 16 | 100% |
| Prompt 约束强度(CFG) | 10 | 4 - 10 | 16 | 74% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | dpmpp_2m | - | 16 | 75% |
| 重绘幅度 | simple | - | 16 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，16 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，16 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，16 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 10，16 个样本
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m，16 个样本，一致性 75%
- 重绘幅度 最常用 simple，16 个样本，一致性 81%
