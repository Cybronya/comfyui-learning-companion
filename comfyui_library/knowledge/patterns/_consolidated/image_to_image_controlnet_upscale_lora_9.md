---
name: image_to_image_controlnet_upscale_lora_9
type: Image To Image
frequency: 4
level: strong
coverage: 0.92625
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, ImageResize+, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoader, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, WD14Tagger|pysssss]
problems: []
missing: []
members: [平台全量/乐高世界_1783769516971401217.json, 平台全量/毛绒质感ICON_1788758938934636546.json, 平台全量/毛绒鸭_1788764264186572802.json, 平台全量/皮克斯风格化转换_1778271838636400642.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/乐高世界_1783769516971401217.json、平台全量/毛绒质感ICON_1788758938934636546.json、平台全量/毛绒鸭_1788764264186572802.json、平台全量/皮克斯风格化转换_1778271838636400642.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `CR SDXL Style Text` —— 2/4 个有
- `Canny` —— 2/4 个有
- `CR Text Cycler` —— 1/4 个有
- `DF_Text` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `Float` —— 1/4 个有
- `HEDPreprocessor` —— 1/4 个有
- `RepeatLatentBatch` —— 1/4 个有
- `TextCombinerTwo` —— 1/4 个有
- `Zoe-DepthMapPreprocessor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | 0.55 - 0.7 | 4 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.925 | 0.75 - 1 | 4 | 88% |
| 采样步数 | 25 | 20 - 30 | 4 | 80% |
| Prompt 约束强度(CFG) | 7.5 | 7 - 8 | 4 | 93% |
| 采样算法 | dpmpp_sde | - | 4 | 50% |
| 调度器 | karras | - | 4 | 75% |
| 重绘幅度 | 0.38 | 0.32 - 0.7 | 4 | 66% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，观测区间 0.55 - 0.7，4 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.925，观测区间 0.75 - 1，4 个样本，取值集中（一致性 88%）
- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 7 - 8，4 个样本，取值集中（一致性 93%）
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 50%
- 调度器 最常用 karras，4 个样本，一致性 75%
- 重绘幅度 中位数 0.38，观测区间 0.32 - 0.7，4 个样本
