---
name: unknown_workflow_controlnet_ipadapter_sampler_3
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.825
common_nodes: [AIO_Preprocessor, Anything Everywhere3, BNK_CLIPTextEncodeAdvanced, BrushNet, BrushNetLoader, CR Text, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DF_Image_scale_to_side, DWPreprocessor, DetailTransfer, ICLightConditioning, IPAdapterUnifiedLoader, Image Comparer (rgthree), ImageResize+, JWImageResizeByLongerSide, KSampler //Inspire, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LoadAndApplyICLightUnet, LoadImage, MaskPreview+, MiniCPM_VQA, PreviewImage, Prompts Everywhere, SaveImage, Text Concatenate, VAEDecode, VAEEncode, easy imageColorMatch, easy imageSize, easy showAnything]
problems: []
missing: []
members: [平台全量/人像写真换背景 风格迁移 只需一张参考图一键出图_1932429081357000705.json, 平台全量/人像换背景，仅需一张参考图一键背景，ICLight光影融合，人物保持不变_1931934860389056513.json, 平台全量/人像换背景，提示词描述任意背景，ICLight光影融合，人物保持不变_1931925592696881153.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_sampler_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/人像写真换背景 风格迁移 只需一张参考图一键出图_1932429081357000705.json、平台全量/人像换背景，仅需一张参考图一键背景，ICLight光影融合，人物保持不变_1931934860389056513.json、平台全量/人像换背景，提示词描述任意背景，ICLight光影融合，人物保持不变_1931925592696881153.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `BNK_CLIPTextEncodeAdvanced`
- `BrushNet`
- `BrushNetLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DF_Image_scale_to_side`
- `DWPreprocessor`
- `DetailTransfer`
- `ICLightConditioning`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `JWImageResizeByLongerSide`
- `KSampler //Inspire`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskPreview+`
- `MiniCPM_VQA`
- `PreviewImage`
- `Prompts Everywhere`
- `SaveImage`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `easy imageColorMatch`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `IPAdapter` —— 2/3 个有
- `InspyrenetRembgAdvanced` —— 2/3 个有
- `CR Text Input Switch` —— 1/3 个有
- `IPAdapterAdvanced` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.3 | 0.3 - 0.3 | 3 | 100% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | ddim_uniform | - | 3 | 100% |
| 重绘幅度 | 0.45 | 0.45 - 0.45 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 ddim_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 0.45，3 个样本，取值集中（一致性 100%）
