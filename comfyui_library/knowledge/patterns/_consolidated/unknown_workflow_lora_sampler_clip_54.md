---
name: unknown_workflow_lora_sampler_clip_54
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.87275
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SeargePromptCombiner, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [DrawText+, SDXL Resolutions (JPS)]
members: [图片生成/文生图/1934815242520043521.json, 图片生成/文生图/1938572723696099330.json, 图片生成/文生图/1945170907587596289.json, 图片生成/文生图/1946922717151158273.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1934815242520043521.json、图片生成/文生图/1938572723696099330.json、图片生成/文生图/1945170907587596289.json、图片生成/文生图/1946922717151158273.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeargePromptCombiner`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawText+` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `JJC_JoyCaption` —— 1/4 个有
- `JJC_JoyCaption_Custom` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `SDXL Resolutions (JPS)` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 768 | 4 | 97% |
| 高度 | 1024 | 1024 - 1280 | 4 | 90% |
| LoRA 模型强度 | 0.825 | 0.8 - 1 | 4 | 90% |
| LoRA 文本强度 | 1 | 0.85 - 1 | 4 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 768，4 个样本，取值集中（一致性 97%）
- 高度 中位数 1024，观测区间 1024 - 1280，4 个样本，取值集中（一致性 90%）
- LoRA 模型强度 中位数 0.825，观测区间 0.8 - 1，4 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 0.85 - 1，4 个样本，取值集中（一致性 93%）
- 这些节点还没有知识卡，系统对它们的理解有限：DrawText+、SDXL Resolutions (JPS)
