---
name: text_to_image_inpaint_sampler_clip_3
type: Text To Image
frequency: 4
level: strong
coverage: 0.76575
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DetailerForEach, EmptyLatentImage, GetNode, Image Comparer (rgthree), ImageResize+, ImpactSwitch, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ImageBlendAdvance, LoadImage, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_KolorsUNETLoaderV2, Mask Invert, MaskPreview+, MaskToSEGS, PreviewImage, SaveImage, SetNode, VAEDecode, VAEEncodeForInpaint, VAELoader]
problems: []
missing: []
members: [平台全量/Kolors模型局部重绘_1821071450840150017.json, 平台全量/Kolors模型局部重绘_1848929035710611458.json, 平台全量/人像换背景_1833023390457487361.json, 平台全量/高精度人物换背景溶图_1915076276024184834.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Kolors模型局部重绘_1821071450840150017.json、平台全量/Kolors模型局部重绘_1848929035710611458.json、平台全量/人像换背景_1833023390457487361.json、平台全量/高精度人物换背景溶图_1915076276024184834.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DetailerForEach`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImpactSwitch`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `MZ_ChatGLM3Loader`
- `MZ_ChatGLM3_V2`
- `MZ_KolorsUNETLoaderV2`
- `Mask Invert`
- `MaskPreview+`
- `MaskToSEGS`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `VAEDecode`
- `VAEEncodeForInpaint`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `Textbox` —— 3/4 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 2/4 个有
- `BRIA_RMBG_Zho` —— 2/4 个有
- `GrowMask` —— 2/4 个有
- `HD UltimateSDUpscale` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerColor: ColorAdapter` —— 2/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/4 个有
- `MZ_IPAdapterAdvancedKolors` —— 2/4 个有
- `MZ_IPAdapterModelLoaderKolors` —— 2/4 个有
- `MZ_KolorsCLIPVisionLoader` —— 2/4 个有
- `TextCombinerTwo` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `Bjornulf_ShowStringText` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Joy_caption_two` —— 1/4 个有
- `Joy_caption_two_load` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 4 | 100% |
| 采样算法 | dpmpp_3m_sde | - | 4 | 100% |
| 调度器 | exponential | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_3m_sde，4 个样本，一致性 100%
- 调度器 最常用 exponential，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
