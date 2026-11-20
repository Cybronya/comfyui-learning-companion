---
name: image_to_image_controlnet_ipadapter_inpaint_3
type: Image To Image
frequency: 2
level: weak
coverage: 0.711
common_nodes: [AV_VAELoader, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DetailerForEach, Display Int (rgthree), DualCLIPLoader, FluxGuidance, GetImageSize, GetNode, Image Comparer (rgthree), ImagePadForOutpaint, ImageResize+, JjkText, KSampler, KSamplerSelect, Label (rgthree), LayerColor: ColorAdapter, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageBlendAdvance, LoadImage, LoraLoader, LoraLoaderModelOnly, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_IPAdapterAdvancedKolors, MZ_IPAdapterModelLoaderKolors, MZ_KolorsCLIPVisionLoader, MZ_KolorsControlNetPatch, MZ_KolorsUNETLoaderV2, Mask Invert, MaskPreview+, MaskToImage, MaskToSEGS, PreviewImage, RH_Captioner, RH_Prompter, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TextCombinerSix, UNETLoader, VAEDecode, VAEEncode, VAEEncodeForInpaint, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/产品图创意海报【一键换背景】_1853675044148023298.json, 平台全量/生成创意海报generate_creative_posters_1950024565730795522.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_inpaint_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/产品图创意海报【一键换背景】_1853675044148023298.json、平台全量/生成创意海报generate_creative_posters_1950024565730795522.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `AV_VAELoader`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailerForEach`
- `Display Int (rgthree)`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageResize+`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerColor: ColorAdapter`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MZ_ChatGLM3Loader`
- `MZ_ChatGLM3_V2`
- `MZ_IPAdapterAdvancedKolors`
- `MZ_IPAdapterModelLoaderKolors`
- `MZ_KolorsCLIPVisionLoader`
- `MZ_KolorsControlNetPatch`
- `MZ_KolorsUNETLoaderV2`
- `Mask Invert`
- `MaskPreview+`
- `MaskToImage`
- `MaskToSEGS`
- `PreviewImage`
- `RH_Captioner`
- `RH_Prompter`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TextCombinerSix`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeForInpaint`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
