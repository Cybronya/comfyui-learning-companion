---
name: text_to_image_controlnet_ipadapter_lora
type: Text To Image
frequency: 3
level: strong
coverage: 0.767
common_nodes: [ACN_ControlNet++LoaderSingle, AV_ControlNetPreprocessor, AV_IPAdapter, Anything Everywhere, CLIPSetLastLayer, CLIPTextEncode, CM_NearestSDXLResolution, CM_SDXLResolution, CR Color Gradient, CR Text Concatenate, CR Text Input Switch, CheckpointLoaderSimple, ControlNetApplyAdvanced, EmptyLatentImage, ImageBatch, ImageResize+, ImpactInt, ImpactSwitch, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageBlendAdvance V2, LayerUtility: TextJoin, LoadImage, LoraLoader, MiniCPM_VQA, PreviewImage, Prompts Everywhere, SaveImage, Seed Generator, ShowText|pysssss, Simple String, VAEDecode, easy promptReplace]
problems: []
missing: []
members: [图片生成/图生图/手绘插画工作流_2041758922905755650.json, 平台全量/【update】Hand-drawn illustration workflow _ 手绘插画工作流_1862384348501835778.json, 平台全量/手绘插画工作流_2038516937226985474.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_lora

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/手绘插画工作流_2041758922905755650.json、平台全量/【update】Hand-drawn illustration workflow _ 手绘插画工作流_1862384348501835778.json、平台全量/手绘插画工作流_2038516937226985474.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `ACN_ControlNet++LoaderSingle`
- `AV_ControlNetPreprocessor`
- `AV_IPAdapter`
- `Anything Everywhere`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CM_NearestSDXLResolution`
- `CM_SDXLResolution`
- `CR Color Gradient`
- `CR Text Concatenate`
- `CR Text Input Switch`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `EmptyLatentImage`
- `ImageBatch`
- `ImageResize+`
- `ImpactInt`
- `ImpactSwitch`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageBlendAdvance V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoader`
- `MiniCPM_VQA`
- `PreviewImage`
- `Prompts Everywhere`
- `SaveImage`
- `Seed Generator`
- `ShowText|pysssss`
- `Simple String`
- `VAEDecode`
- `easy promptReplace`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
