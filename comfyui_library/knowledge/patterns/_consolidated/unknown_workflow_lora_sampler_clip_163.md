---
name: unknown_workflow_lora_sampler_clip_163
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.707667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ConstrainImage|pysssss, DualCLIPLoader, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/FLUX 图生图 +Lora + joy自动反推提示词_1892548146520612865.json, 图片生成/图生图/FLUX图生图_超级实用_1920375666431430657.json, 图片生成/图生图/majicFlus 图生图_1884514047411343361.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_163

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX 图生图 +Lora + joy自动反推提示词_1892548146520612865.json、图片生成/图生图/FLUX图生图_超级实用_1920375666431430657.json、图片生成/图生图/majicFlus 图生图_1884514047411343361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `Joy_caption` —— 2/3 个有
- `Joy_caption_load` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `Text Concatenate (JPS)` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `Joy_caption_two` —— 1/3 个有
- `Joy_caption_two_load` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `ttN concat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
