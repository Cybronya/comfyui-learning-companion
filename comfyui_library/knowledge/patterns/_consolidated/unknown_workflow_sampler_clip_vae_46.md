---
name: unknown_workflow_sampler_clip_vae_46
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9776
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/CFGzero简单工作流带lora_1928999965027155970.json, 图片生成/文生图/FLUX文生图 繁花lora工作流_1942505597264924674.json, 图片生成/文生图/Flux 1 文生图基础工作流_1937783580867084290.json, 图片生成/文生图/Flux+Lora标准文生图_1932966165364834305.json, 图片生成/文生图/Flux文生图工作流_1941002485245100033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_46

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/CFGzero简单工作流带lora_1928999965027155970.json、图片生成/文生图/FLUX文生图 繁花lora工作流_1942505597264924674.json、图片生成/文生图/Flux 1 文生图基础工作流_1937783580867084290.json、图片生成/文生图/Flux+Lora标准文生图_1932966165364834305.json、图片生成/文生图/Flux文生图工作流_1941002485245100033.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `DeepTranslatorTextNode` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `CFGZeroStar` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `ImageSmartSharpen+` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `Int` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1440 | 5 | 86% |
| 高度 | 1080 | 768 - 1536 | 5 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1440，5 个样本，取值集中（一致性 86%）
- 高度 中位数 1080，观测区间 768 - 1536，5 个样本
