---
name: unknown_workflow_sampler_unet_vae_200
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9622
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/卡通3d中国美食生成_1929220483173224450.json, 图片生成/反推提示词/反推后出图_1954531331520786433.json, 图片生成/图生图/ai滤镜应用版_1985270833641832449.json, 图片生成/图生图/照片转全能图片G-4o卡通人像形象丨一键在线运行_1911405677586149377.json, 图片生成/文生图/反推提示词+在线生图v1.0_1946032541281251330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_200

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/卡通3d中国美食生成_1929220483173224450.json、图片生成/反推提示词/反推后出图_1954531331520786433.json、图片生成/图生图/ai滤镜应用版_1985270833641832449.json、图片生成/图生图/照片转全能图片G-4o卡通人像形象丨一键在线运行_1911405677586149377.json、图片生成/文生图/反推提示词+在线生图v1.0_1946032541281251330.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `DisplayText` —— 3/5 个有
- `LayerUtility: TextJoin` —— 3/5 个有
- `LoraLoader` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `CLIPTextEncodeFlux` —— 2/5 个有
- `ImageResize+` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `CR Latent Batch Size` —— 1/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `Joy_caption_alpha_load` —— 1/5 个有
- `Joy_caption_alpha_run` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1024 | 4 | 86% |
| 高度 | 1024 | 720 - 1400 | 4 | 77% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 3 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1024，4 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 720 - 1400，4 个样本
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
