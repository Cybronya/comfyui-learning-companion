---
name: unknown_workflow_face_detailer_lora_sampler_2
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.952
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, ConstrainImage|pysssss, DetailDaemonSamplerNode, DualCLIPLoader, EmptyLatentImage, FaceDetailer, FluxAttentionSeeker+, FluxGuidance, ImpactImageBatchToImageList, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LoadImage, LoraLoader, ModelSamplingFlux, RandomNoise, SAMLoader, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, TeaCache, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader, easy imageSize, ttN concat]
problems: []
missing: []
members: [图片生成/图生图/Flux人物多角度｜秒变多角度时尚大片_1935150534972383233.json, 图片生成/图生图/【网红大片】多角度时尚模特一致性风格_1914203359530942465.json, 图片生成/图生图/【网红大片】多角度时尚模特一致性风格v1.0_1908047771457495042.json, 图片生成/图生图/【网红洗图pulid_flux】多角度时尚模特人物一致性风格_1914985791666253826.json, 图片生成/图生图/【网红海报】多角度时尚模特一致性风格_1911136662779326466.json, 图片生成/图生图/模特一致性上传模特图，秒变多角度时尚大片！_1906378891399991297.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux人物多角度｜秒变多角度时尚大片_1935150534972383233.json、图片生成/图生图/【网红大片】多角度时尚模特一致性风格_1914203359530942465.json、图片生成/图生图/【网红大片】多角度时尚模特一致性风格v1.0_1908047771457495042.json、图片生成/图生图/【网红洗图pulid_flux】多角度时尚模特人物一致性风格_1914985791666253826.json、图片生成/图生图/【网红海报】多角度时尚模特一致性风格_1911136662779326466.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceDetailer`
- `FluxAttentionSeeker+`
- `FluxGuidance`
- `ImpactImageBatchToImageList`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `RandomNoise`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `TeaCache`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 4/6 个有
- `JjkShowText` —— 4/6 个有
- `Joy_caption` —— 3/6 个有
- `Joy_caption_load` —— 3/6 个有
- `ArgosTranslateTextNode` —— 2/6 个有
- `ETN_Translate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 512 | 512 - 512 | 6 | 100% |
| LoRA 模型强度 | 0.1 | 0.1 - 0.8 | 6 | 0% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.1，观测区间 0.1 - 0.8，6 个样本，取值分散，一致性仅 0%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
