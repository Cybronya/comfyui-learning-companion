---
name: unknown_workflow_sampler_clip_unet_103
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.9625
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/基础flux文生图1009_1976073946242093057.json, 图片生成/文生图/大家电场景图2.0_1943614394796568578.json, 图片生成/文生图/大家电场景图_1948667723191595009.json, 图片生成/文生图/室内建筑景观高质感文生图_2067220940961964033.json, 图片生成/文生图/沙雕动漫专用表情包快速生成_2043984326500556801.json, 图片生成/文生图/生成系列性服装设计_1884234765942538241.json, 图片生成/文生图/风后文生图_1878760414459932673.json, 平台全量/IP三视图角色生成工作流_1894290505101127681.json, 平台全量/dfhjewgfuiegfjwe_2009960431246381058.json, 平台全量/fweijfgbwe、_2000511336004153345.json, 平台全量/jhfgikerhgiewhgg_2013780798494740481.json, 平台全量/wegfuijefgew_2012022411612397569.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_103

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/基础flux文生图1009_1976073946242093057.json、图片生成/文生图/大家电场景图2.0_1943614394796568578.json、图片生成/文生图/大家电场景图_1948667723191595009.json、图片生成/文生图/室内建筑景观高质感文生图_2067220940961964033.json、图片生成/文生图/沙雕动漫专用表情包快速生成_2043984326500556801.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/12 个有
- `RH_Translator` —— 4/12 个有
- `LoraLoader` —— 3/12 个有
- `DeepTranslatorTextNode` —— 1/12 个有
- `LoraLoader|pysssss` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `Text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 904 | 720 - 2048 | 12 | 58% |
| 高度 | 1280 | 1024 - 1920 | 12 | 83% |
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 4 | 75% |
| LoRA 文本强度 | 1 | 1 - 1.02 | 4 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 904，观测区间 720 - 2048，12 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，12 个样本，取值集中（一致性 83%）
- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1.02，4 个样本，取值集中（一致性 99%）
