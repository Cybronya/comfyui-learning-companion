---
name: text_to_image_controlnet_lora_sampler_7
type: Text To Image
frequency: 2
level: weak
coverage: 0.837
common_nodes: [AIO_Preprocessor, AnyLineArtPreprocessor_aux, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, Canny, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingV2Preprocessor, DualCLIPLoader, EmptyFlux2LatentImage, EmptyLatentImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LineArtPreprocessor, LoadImage, LoraLoader, LoraLoaderModelOnly, Metric3D-NormalMapPreprocessor, PreviewImage, SDXLEmptyLatentSizePicker+, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/SDXL_FLUX + LORA+Controlnet基础学习工作流_2056427488204648450.json, 图片生成/文生图/SDXL_FLUX_+_LORA+Controlnet基础学习工作流_2064154626043236353.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/SDXL_FLUX + LORA+Controlnet基础学习工作流_2056427488204648450.json、图片生成/文生图/SDXL_FLUX_+_LORA+Controlnet基础学习工作流_2064154626043236353.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AnyLineArtPreprocessor_aux`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `Canny`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `Metric3D-NormalMapPreprocessor`
- `PreviewImage`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 24 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
