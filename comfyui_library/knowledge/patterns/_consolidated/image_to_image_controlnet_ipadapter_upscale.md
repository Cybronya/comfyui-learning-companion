---
name: image_to_image_controlnet_ipadapter_upscale
type: Image To Image
frequency: 8
level: moderate
coverage: 0.7835
common_nodes: [AnyLineArtPreprocessor_aux, BasicScheduler, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DetailTransfer, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, InvertMask, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ImageBlend, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LightSource, LoadAndApplyICLightUnet, LoadImage, LoraLoader, PreviewImage, SamplerCustom, SaveImage, ShowText|pysssss, Text Concatenate, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/产品换背景   白底换背景   风格迁移 放大 ic控光 F1修复_1889253088036052993.json, 图片生成/图生图/白底图一键改背景空白工作流_1897559365912580097.json, 平台全量/2025」Flux模型生成产品背景图_1896098010688847873.json, 平台全量/2025」Flux模型生成产品背景图_1934257156625494017.json, 平台全量/产品一键生成背景简单易用_1934763244274032641.json, 平台全量/产品背景生成_1911087994957430786.json, 平台全量/安-产品一键生成背景简单易用_1934430671362547713.json, 平台全量/静物白底换背景一键生成，含风格迁移_放大_ic控光_F1修复_1895728764959719425.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/产品换背景   白底换背景   风格迁移 放大 ic控光 F1修复_1889253088036052993.json、图片生成/图生图/白底图一键改背景空白工作流_1897559365912580097.json、平台全量/2025」Flux模型生成产品背景图_1896098010688847873.json、平台全量/2025」Flux模型生成产品背景图_1934257156625494017.json、平台全量/产品一键生成背景简单易用_1934763244274032641.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `BasicScheduler`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailTransfer`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `InvertMask`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LightSource`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `ShowText|pysssss`
- `Text Concatenate`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 6/8 个有
- `DeepTranslatorTextNode` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `easy clearCacheAll` —— 4/8 个有
- `ArgosTranslateTextNode` —— 3/8 个有
- `RepeatLatentBatch` —— 3/8 个有
- `Anything Everywhere3` —— 2/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `DifferentialDiffusion` —— 2/8 个有
- `ImageConcanate` —— 2/8 个有
- `ImageCrop+` —— 2/8 个有
- `ImageToMask` —— 2/8 个有
- `InspyrenetRembgAdvanced` —— 2/8 个有
- `LayerUtility: ColorImage V2` —— 2/8 个有
- `LayerUtility: GetImageSize` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `RHHiddenNodes` —— 2/8 个有
- `SUPIR_Upscale` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.9 | 0.8 - 0.9 | 8 | 96% |
| 采样步数 | 25 | 20 - 35 | 8 | 75% |
| Prompt 约束强度(CFG) | 3 | 1 - 6 | 8 | 45% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | normal | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 0.6 | 0.6 - 0.9 | 8 | 81% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.9，观测区间 0.8 - 0.9，8 个样本，取值集中（一致性 96%）
- 采样步数 中位数 25，观测区间 20 - 35，8 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 6，8 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 normal，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.9，8 个样本，取值集中（一致性 81%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
