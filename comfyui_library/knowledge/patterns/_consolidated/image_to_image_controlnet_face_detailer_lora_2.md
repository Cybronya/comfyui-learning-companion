---
name: image_to_image_controlnet_face_detailer_lora_2
type: Image To Image
frequency: 3
level: strong
coverage: 0.858
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetLoader, FaceDetailer, FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), GrowMaskWithBlur, KSampler, LoadImage, LoraLoader, PreviewImage, SaveImage, SetLatentNoiseMask, UltralyticsDetectorProvider, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/专业女性人像精修工作流_1928070423513022465.json, 图片生成/图生图/人像精修带妆感（保留肌肤质感）_1919605193082867714.json, 平台全量/高精度人脸修图_1925022612584341506.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_face_detailer_lora_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/专业女性人像精修工作流_1928070423513022465.json、图片生成/图生图/人像精修带妆感（保留肌肤质感）_1919605193082867714.json、平台全量/高精度人脸修图_1925022612584341506.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetLoader`
- `FaceDetailer`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `GrowMaskWithBlur`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `ControlNetApply` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `CoreMLDetailerHookProvider` —— 1/3 个有
- `SAMLoader` —— 1/3 个有
- `SUPIR_Upscale` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 26 | 3 | 51% |
| Prompt 约束强度(CFG) | 8 | 5 - 8 | 3 | 80% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 3 | 100% |
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| LoRA 模型强度 | 0.3 | 0.3 - 0.4 | 3 | 86% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 26，3 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 8，3 个样本
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.3，观测区间 0.3 - 0.4，3 个样本，取值集中（一致性 86%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
