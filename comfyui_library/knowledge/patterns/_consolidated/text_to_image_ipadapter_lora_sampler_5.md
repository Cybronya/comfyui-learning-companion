---
name: text_to_image_ipadapter_lora_sampler_5
type: Text To Image
frequency: 3
level: strong
coverage: 0.671667
common_nodes: [AV_IPAdapter, Anything Everywhere, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, GetImageSize+, GetNode, ImageBatch, ImageDesaturate+, ImageRemoveBackground+, ImageScaleToMegapixels, KSampler, Label (rgthree), LoadAndResizeImage, LoadImage, LoraLoader, MergeLayers, NewLayer, PreviewImage, Prompts Everywhere, RemBGSession+, SaveImage, Seed Generator, SetNode, ShowText|pysssss, VAEDecode, easy promptReplace]
problems: []
missing: []
members: [平台全量/卡通盲盒形象_1823996642528768002.json, 平台全量/运动系可爱头像_1843673299460259841.json, 平台全量/风格化头像_1823604325620060161.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/卡通盲盒形象_1823996642528768002.json、平台全量/运动系可爱头像_1843673299460259841.json、平台全量/风格化头像_1823604325620060161.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `AV_IPAdapter`
- `Anything Everywhere`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetImageSize+`
- `GetNode`
- `ImageBatch`
- `ImageDesaturate+`
- `ImageRemoveBackground+`
- `ImageScaleToMegapixels`
- `KSampler`
- `Label (rgthree)`
- `LoadAndResizeImage`
- `LoadImage`
- `LoraLoader`
- `MergeLayers`
- `NewLayer`
- `PreviewImage`
- `Prompts Everywhere`
- `RemBGSession+`
- `SaveImage`
- `Seed Generator`
- `SetNode`
- `ShowText|pysssss`
- `VAEDecode`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `ApplyPulid` —— 2/3 个有
- `PulidEvaClipLoader` —— 2/3 个有
- `PulidInsightFaceLoader` —— 2/3 个有
- `PulidModelLoader` —— 2/3 个有
- `SeargePromptCombiner` —— 2/3 个有
- `ACN_ControlNet++LoaderSingle` —— 1/3 个有
- `AV_ControlNetPreprocessor` —— 1/3 个有
- `CR Image Input Switch (4 way)` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `Joy_caption` —— 1/3 个有
- `Joy_caption_load` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `WD14Tagger|pysssss` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageIndexSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | 0.2 - 0.5 | 3 | 65% |
| LoRA 文本强度 | 0.5 | 0.2 - 0.5 | 3 | 65% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 30 | 25 - 30 | 3 | 92% |
| Prompt 约束强度(CFG) | 6.5 | 5.4 - 6.5 | 3 | 92% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，观测区间 0.2 - 0.5，3 个样本
- LoRA 文本强度 中位数 0.5，观测区间 0.2 - 0.5，3 个样本
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 25 - 30，3 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 5.4 - 6.5，3 个样本，取值集中（一致性 92%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
