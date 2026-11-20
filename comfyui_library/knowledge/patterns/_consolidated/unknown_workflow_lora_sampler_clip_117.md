---
name: unknown_workflow_lora_sampler_clip_117
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9758
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen2512+文生图_2006906953485783042.json, 图片生成/文生图/Qwen2512+文生图_2010038639497056258.json, 图片生成/文生图/QwenImage2512_文生图(战双帕米什赛琳娜)_2041055957064617986.json, 图片生成/文生图/文生图Qwen-Image-2512_2080217378687905793.json, 图片生成/文生图/（Bf16+lighttning版）Qwen Image 2512手动提示词文生图V1_2006374521699307522.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_117

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen2512+文生图_2006906953485783042.json、图片生成/文生图/Qwen2512+文生图_2010038639497056258.json、图片生成/文生图/QwenImage2512_文生图(战双帕米什赛琳娜)_2041055957064617986.json、图片生成/文生图/文生图Qwen-Image-2512_2080217378687905793.json、图片生成/文生图/（Bf16+lighttning版）Qwen Image 2512手动提示词文生图V1_2006374521699307522.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `TTResolutionSelector` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `Qwen2.5` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_2s | - | 5 | 80% |
| 调度器 | beta57 | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，5 个样本，一致性 80%
- 调度器 最常用 beta57，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
