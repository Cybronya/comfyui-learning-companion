---
name: text_to_image_ipadapter_upscale_sampler
type: Text To Image
frequency: 7
level: moderate
coverage: 0.959571
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, IPAdapter, IPAdapterUnifiedLoader, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, UpscaleModelLoader, VAEDecode]
problems: []
missing: []
members: [平台全量/日漫小房子制作_1782327487129235458.json, 平台全量/星际眺望者_1801549022973341698.json, 平台全量/暗影女刺客_1798640655904382978.json, 平台全量/未来之城_1795039423080022018.json, 平台全量/未来城市_1797860075847675906.json, 平台全量/父爱如山_1801511380156100610.json, 平台全量/端午安康_1798268782561484801.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/日漫小房子制作_1782327487129235458.json、平台全量/星际眺望者_1801549022973341698.json、平台全量/暗影女刺客_1798640655904382978.json、平台全量/未来之城_1795039423080022018.json、平台全量/未来城市_1797860075847675906.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 5/7 个有
- `CLIPSetLastLayer` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `TextConcatenator` —— 3/7 个有
- `VAEEncode` —— 3/7 个有
- `WD14Tagger|pysssss` —— 3/7 个有
- `Image Overlay` —— 2/7 个有
- `ColorCorrect` —— 1/7 个有
- `ImageResize+` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 7 | 83% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 7 | 100% |
| 采样算法 | dpmpp_2m | - | 7 | 57% |
| 调度器 | karras | - | 7 | 71% |
| 重绘幅度 | 1 | 0.4 - 1 | 7 | 69% |
| 宽度 | 1024 | 512 - 1280 | 7 | 67% |
| 高度 | 640 | 640 - 1064 | 7 | 77% |
| LoRA 模型强度 | 0.5 | 0.29 - 0.55 | 3 | 75% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，7 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 57%
- 调度器 最常用 karras，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，7 个样本
- 宽度 中位数 1024，观测区间 512 - 1280，7 个样本
- 高度 中位数 640，观测区间 640 - 1064，7 个样本
- LoRA 模型强度 中位数 0.5，观测区间 0.29 - 0.55，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
