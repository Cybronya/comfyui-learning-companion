---
name: unknown_workflow_lora_sampler_clip_149
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.81425
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SaveLatent, SeedVR2BlockSwap, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/IRC艺术作品_1962782328558862338.json, 图片生成/文生图/Qwen Image多训练器人像拟合度对比教程工作流_1962098134904147969.json, 图片生成/文生图/Qwen Image文生图（Bridge版）_1962778802571096065.json, 图片生成/文生图/（贞贞版）Qwen Image文生图（水墨纸片）_1963157852737212417.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_149

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/IRC艺术作品_1962782328558862338.json、图片生成/文生图/Qwen Image多训练器人像拟合度对比教程工作流_1962098134904147969.json、图片生成/文生图/Qwen Image文生图（Bridge版）_1962778802571096065.json、图片生成/文生图/（贞贞版）Qwen Image文生图（水墨纸片）_1963157852737212417.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SaveLatent`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `SeedVR2GGUF` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `QwenTemplateBuilder` —— 2/4 个有
- `IRC Art Converter` —— 1/4 个有
- `IRC PNG Exporter` —— 1/4 个有
- `IRC Text Saver` —— 1/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（15/4 个样本）：Steps较低可能导致细节不足
