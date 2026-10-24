---
name: unknown_workflow_lora_sampler_clip_121
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9725
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text Replace, DisableNoise, DualCLIPLoader, EG_TC_Node, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, Int, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LoadImage, LoraLoader, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SplitSigmasDenoise, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F1.极度真实日常生活照小红书超写实生活照3.0_1906155298510540801.json, 图片生成/图生图/小红书网感美女 双图融合  模特套图_2037782440806191106.json, 图片生成/文生图/小红书高质量美女图 网感美女 轻松涨粉_2034169411594100738.json, 图片生成/文生图/小红书高质量美女图，轻松涨粉_1828492510539993089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_121

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/F1.极度真实日常生活照小红书超写实生活照3.0_1906155298510540801.json、图片生成/图生图/小红书网感美女 双图融合  模特套图_2037782440806191106.json、图片生成/文生图/小红书高质量美女图 网感美女 轻松涨粉_2034169411594100738.json、图片生成/文生图/小红书高质量美女图，轻松涨粉_1828492510539993089.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text Replace`
- `DisableNoise`
- `DualCLIPLoader`
- `EG_TC_Node`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `Int`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 3/4 个有
- `ApplyPulidFlux` —— 1/4 个有
- `FloatSlider` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `PortraitMaster_中文版` —— 1/4 个有
- `PulidFluxEvaClipLoader` —— 1/4 个有
- `PulidFluxInsightFaceLoader` —— 1/4 个有
- `PulidFluxModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| LoRA 模型强度 | 0.2 | 0.2 - 0.5 | 4 | 53% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.2，观测区间 0.2 - 0.5，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
