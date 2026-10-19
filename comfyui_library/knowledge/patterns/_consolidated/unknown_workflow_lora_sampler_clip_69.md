---
name: unknown_workflow_lora_sampler_clip_69
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.716667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, CR Aspect Ratio SDXL, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, StringFunction|pysssss, CR Aspect Ratio SDXL]
members: [图片生成/文生图/1934549977387442177.json, 图片生成/文生图/FLUX-随机提示词-基础文生图-提示词反推_1901113562578984962.json, 图片生成/文生图/Flux网红美女跑图工作流1124_1893653901269241858.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1934549977387442177.json、图片生成/文生图/FLUX-随机提示词-基础文生图-提示词反推_1901113562578984962.json、图片生成/文生图/Flux网红美女跑图工作流1124_1893653901269241858.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `CR Aspect Ratio SDXL`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2Run` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `DownloadAndLoadFlorence2Model` —— 1/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `Primitive string multiline [Crystools]` —— 1/3 个有
- `SDXLPromptStyler` —— 1/3 个有
- `Text Random Line` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 800 - 800 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.4 - 0.8 | 3 | 72% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 800 - 800，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.4 - 0.8，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: JoyCaptionBeta1ExtraOptions、LayerUtility: LoadJoyCaptionBeta1Model、StringFunction|pysssss、CR Aspect Ratio SDXL
