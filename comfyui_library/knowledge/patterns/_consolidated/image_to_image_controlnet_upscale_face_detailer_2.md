---
name: image_to_image_controlnet_upscale_face_detailer_2
type: Image To Image
frequency: 2
level: weak
coverage: 0.806
common_nodes: [Anything Everywhere, CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApply, ControlNetLoader, FaceDetailer, FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), GrowMaskWithBlur, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, LoraLoader, MaskPreview+, PreviewImage, SaveImage, SetLatentNoiseMask, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/专业女性人像精修工作流_1928070423513022465.json, 图片生成/图生图/人像精修带妆感（保留肌肤质感）_1919605193082867714.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_face_detailer_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/专业女性人像精修工作流_1928070423513022465.json、图片生成/图生图/人像精修带妆感（保留肌肤质感）_1919605193082867714.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApply`
- `ControlNetLoader`
- `FaceDetailer`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.4 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |
| LoRA 模型强度 | 0.3 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
