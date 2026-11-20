---
name: unknown_workflow_lora_sampler_clip_210
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.889333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), INTConstant, Int, JjkText, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Gemini31Flash, RH_YouchuanTextToImageV7, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/MJ图生视频素材库合集_2044015670647590913.json, 图片生成/文生图/Work-Fisher专用资产库_2043593659563646977.json, 图片生成/文生图/资产库生成流_2076915112404930561.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_210

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MJ图生视频素材库合集_2044015670647590913.json、图片生成/文生图/Work-Fisher专用资产库_2043593659563646977.json、图片生成/文生图/资产库生成流_2076915112404930561.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Int`
- `JjkText`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Gemini31Flash`
- `RH_YouchuanTextToImageV7`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
