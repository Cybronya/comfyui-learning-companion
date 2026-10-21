---
name: unknown_workflow_sampler_unet_vae_47
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.922455
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAELoader]
problems: []
missing: [CR Text Concatenate, Text Concatenate (JPS), Text Concatenate]
members: [图片生成/文生图/08.flux-lora-快速文生图_1993297535381028865.json, 图片生成/文生图/1902172176840335361.json, 图片生成/文生图/1904904736871469057.json, 图片生成/文生图/1904906707053776898.json, 图片生成/文生图/1904907559919357954.json, 图片生成/文生图/1904908786933633026.json, 图片生成/文生图/1904909104412807170.json, 图片生成/文生图/1905062711074689026.json, 图片生成/文生图/1909546503734763521.json, 图片生成/文生图/1920491097255251969.json, 图片生成/文生图/In-Context-Lora字体设计_2018938772628443138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_47

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/08.flux-lora-快速文生图_1993297535381028865.json、图片生成/文生图/1902172176840335361.json、图片生成/文生图/1904904736871469057.json、图片生成/文生图/1904906707053776898.json、图片生成/文生图/1904907559919357954.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 10/11 个有
- `TextInput_` —— 9/11 个有
- `CLIPTextEncode` —— 6/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `CLIPTextEncodeFlux` —— 5/11 个有
- `LoraLoader` —— 5/11 个有
- `CR Text Concatenate` —— 4/11 个有
- `Int` —— 4/11 个有
- `Text Concatenate (JPS)` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `Anything Everywhere3` —— 1/11 个有
- `Fast Bypasser (rgthree)` —— 1/11 个有
- `ImageGenResolutionFromLatent` —— 1/11 个有
- `ModelSamplingFlux` —— 1/11 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/11 个有
- `Text Concatenate` —— 1/11 个有
- `VAEDecodeTiled` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1792 | 11 | 68% |
| 高度 | 1216 | 1024 - 1920 | 11 | 77% |
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 5 | 79% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1792，11 个样本
- 高度 中位数 1216，观测区间 1024 - 1920，11 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、Text Concatenate (JPS)、Text Concatenate
