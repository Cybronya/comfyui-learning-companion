---
name: unknown_workflow_lora_sampler_clip_153
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.812
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商洗图_1925833819461750786.json, 图片生成/文生图/Flux网红美女跑图工作流1124_1893653901269241858.json, 图片生成/文生图/发光粒子衣服_1916014463953076225.json, 图片生成/文生图/最强joy3反推+Flux网红美女跑图工作流_1934549977387442177.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/电商洗图_1925833819461750786.json、图片生成/文生图/Flux网红美女跑图工作流1124_1893653901269241858.json、图片生成/文生图/发光粒子衣服_1916014463953076225.json、图片生成/文生图/最强joy3反推+Flux网红美女跑图工作流_1934549977387442177.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Aspect Ratio SDXL` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `RepeatLatentBatch` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `StringFunction|pysssss` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `Float` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/4 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | 0.1 - 1 | 4 | 39% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 800 | 800 - 800 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，观测区间 0.1 - 1，4 个样本，取值分散，一致性仅 39%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，观测区间 800 - 800，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
