---
name: unknown_workflow_lora_sampler_clip_214
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.965333
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptyImage, EmptySD3LatentImage, GetImageSizeAndCount, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, RH_LLMAPI_NODE, SaveImage, StringFunction|pysssss, Text Multiline, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/生图-文生图(角色白底图)-qwen-image-2512-8步_2007728914164092929.json, 图片生成/文生图/生图-文生图-qwen-image-2512-8步_1983723915740651522.json, 图片生成/文生图/生图-文生图-qwen_nunchaku_1972956269776646145.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_214

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/生图-文生图(角色白底图)-qwen-image-2512-8步_2007728914164092929.json、图片生成/文生图/生图-文生图-qwen-image-2512-8步_1983723915740651522.json、图片生成/文生图/生图-文生图-qwen_nunchaku_1972956269776646145.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptySD3LatentImage`
- `GetImageSizeAndCount`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `StringFunction|pysssss`
- `Text Multiline`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 2/3 个有
- `easy saveText` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
