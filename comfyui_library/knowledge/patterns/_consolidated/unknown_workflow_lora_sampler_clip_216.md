---
name: unknown_workflow_lora_sampler_clip_216
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.806
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, EmptySD3LatentImage, Int, JjkText, KSampler, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, RH_LLMAPI_NODE, SaveImage, SeedVR2, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen-Image-2512-毛笔书法字体-高清直出_2034243256430632961.json, 图片生成/文生图/书法字体-毛笔字-Qwen-Image-2512-文生图-高清直出_2034233371894747138.json, 图片生成/文生图/书法字体-毛笔字-草书-Qwen-Image-2512-文生图-高清直出_2034240729781903361.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_216

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-2512-毛笔书法字体-高清直出_2034243256430632961.json、图片生成/文生图/书法字体-毛笔字-Qwen-Image-2512-文生图-高清直出_2034233371894747138.json、图片生成/文生图/书法字体-毛笔字-草书-Qwen-Image-2512-文生图-高清直出_2034240729781903361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `EmptySD3LatentImage`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SeedVR2`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CustomAddLabel` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
