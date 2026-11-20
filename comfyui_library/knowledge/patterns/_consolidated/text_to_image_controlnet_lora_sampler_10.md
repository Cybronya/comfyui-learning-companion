---
name: text_to_image_controlnet_lora_sampler_10
type: Text To Image
frequency: 4
level: moderate
coverage: 0.921
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, ImageResize+, KSampler, LoadImage, LoraLoader, PreviewImage, SaveImage, VAEDecode, Zoe-DepthMapPreprocessor]
problems: []
missing: []
members: [平台全量/毛毡风格化_1797854717544624130.json, 平台全量/艺术字体_1778261827810025474.json, 平台全量/艺术插画制作_1790258952844464130.json, 平台全量/艺术海报设计_1782682521612365825.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/毛毡风格化_1797854717544624130.json、平台全量/艺术字体_1778261827810025474.json、平台全量/艺术插画制作_1790258952844464130.json、平台全量/艺术海报设计_1782682521612365825.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `Zoe-DepthMapPreprocessor`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `Canny` —— 2/4 个有
- `IPAdapter` —— 2/4 个有
- `IPAdapterUnifiedLoader` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `WD14Tagger|pysssss` —— 2/4 个有
- `DWPreprocessor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 512 - 960 | 4 | 79% |
| 高度 | 1044 | 512 - 1064 | 4 | 74% |
| ControlNet 权重 | 0.6 | 0.5 - 1 | 4 | 72% |
| 采样步数 | 25 | 20 - 30 | 4 | 80% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 50% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 0.65 | 0.4 - 1 | 4 | 68% |
| LoRA 模型强度 | 0.5 | 0.2 - 1 | 4 | 42% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 512 - 960，4 个样本
- 高度 中位数 1044，观测区间 512 - 1064，4 个样本
- ControlNet 权重 中位数 0.6，观测区间 0.5 - 1，4 个样本
- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 50%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.4 - 1，4 个样本
- LoRA 模型强度 中位数 0.5，观测区间 0.2 - 1，4 个样本，取值分散，一致性仅 42%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
