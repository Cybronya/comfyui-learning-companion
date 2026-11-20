---
name: unknown_workflow_controlnet_inpaint_lora_8
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.87
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CR Simple Image Compare, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetInpaintingAliMamaApply, ControlNetLoader, DownloadAndLoadFlorence2Model, Florence2Run, FluxGuidance, ImageCrop+, KSamplerSelect, LayerUtility: ExtendCanvasV2, LoraLoader, LoraLoaderModelOnly, MaskPreview+, ModelSamplingFlux, PreviewImage, RandomNoise, Replace Text _O, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, ShowText|pysssss, SimpleMath+, VAEDecode, VAEEncode, easy cleanGpuUsed, easy imageSize]
problems: []
missing: []
members: [平台全量/Flux Product Design (In-Context LoRA)_1860233861719355393.json, 平台全量/Flux Virtual Try-on (in-context lora)_1861694610878681090.json, 平台全量/Flux product design_1879392036263784449.json, 平台全量/Writing on product_1878988295345762305.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Flux Product Design (In-Context LoRA)_1860233861719355393.json、平台全量/Flux Virtual Try-on (in-context lora)_1861694610878681090.json、平台全量/Flux product design_1879392036263784449.json、平台全量/Writing on product_1878988295345762305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxGuidance`
- `ImageCrop+`
- `KSamplerSelect`
- `LayerUtility: ExtendCanvasV2`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `Replace Text _O`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SimpleMath+`
- `VAEDecode`
- `VAEEncode`
- `easy cleanGpuUsed`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `LayerUtility: If ` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `easy compare` —— 3/4 个有
- `easy int` —— 3/4 个有
- `AddMaskForICLora` —— 1/4 个有
- `DownloadAndLoadSAM2Model` —— 1/4 个有
- `Florence2toCoordinates` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `ImageToMask` —— 1/4 个有
- `LayerUtility: ColorImage V2` —— 1/4 个有
- `LayerUtility: ImageBlend` —— 1/4 个有
- `Mask Invert` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `PrepareImageAndMaskForInpaint` —— 1/4 个有
- `SDXLAspectRatioSelector` —— 1/4 个有
- `Sam2Segmentation` —— 1/4 个有
- `Text_Image_Zho` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | -1.51 - 1 | 4 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 -1.51 - 1，4 个样本，取值分散，一致性仅 0%
