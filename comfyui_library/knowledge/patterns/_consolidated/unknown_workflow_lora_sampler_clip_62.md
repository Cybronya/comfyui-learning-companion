---
name: unknown_workflow_lora_sampler_clip_62
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.964714
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2512文生图_2006571269797453825.json, 图片生成/文生图/Qwen Image 2512（bf16）文生图_2006636107433254914.json, 图片生成/文生图/Qwen Image手动提示词文生图-Bf16+lihgning版_2006647725940547586.json, 图片生成/文生图/Qwen2512+文生图_2006906953485783042.json, 图片生成/文生图/QwenImage2512_文生图(战双帕米什赛琳娜)_2041055957064617986.json, 图片生成/文生图/文生图Qwen-Image-2512_2080217378687905793.json, 图片生成/文生图/（Bf16+lighttning版）Qwen Image 2512手动提示词文生图V1_2006374521699307522.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2512文生图_2006571269797453825.json、图片生成/文生图/Qwen Image 2512（bf16）文生图_2006636107433254914.json、图片生成/文生图/Qwen Image手动提示词文生图-Bf16+lihgning版_2006647725940547586.json、图片生成/文生图/Qwen2512+文生图_2006906953485783042.json、图片生成/文生图/QwenImage2512_文生图(战双帕米什赛琳娜)_2041055957064617986.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `LayerUtility: PurgeVRAM` —— 5/7 个有
- `easy showAnything` —— 3/7 个有
- `TTResolutionSelector` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `Prompts Everywhere` —— 1/7 个有
- `Qwen2.5` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | res_2s | - | 7 | 100% |
| 调度器 | beta57 | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，7 个样本，一致性 100%
- 调度器 最常用 beta57，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
