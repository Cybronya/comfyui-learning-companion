---
name: image_to_image_controlnet_ipadapter_upscale_8
type: Image To Image
frequency: 2
level: weak
coverage: 0.7595
common_nodes: [AIO_Preprocessor, Anything Everywhere, ControlNetApply, ControlNetLoader, DownloadAndLoadFlorence2Model, Florence2Run, HD UltimateSDUpscale, ImageResize+, KSampler, LoadImage, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_IPAdapterAdvancedKolors, MZ_IPAdapterModelLoaderKolors, MZ_KolorsCLIPVisionLoader, MZ_KolorsControlNetPatch, MZ_KolorsUNETLoaderV2, PatchModelAddDownscale, PreviewImage, SaveImage, ShowText|pysssss, TextCombinerTwo, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, easy seed]
problems: []
missing: []
members: [平台全量/Kolors模型(IPA+CN) 结合Florence 图生图_1821112326128078850.json, 平台全量/Kolors模型(IPA+CN) 结合Florence 图生图_1821408374780268546.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Kolors模型(IPA+CN) 结合Florence 图生图_1821112326128078850.json、平台全量/Kolors模型(IPA+CN) 结合Florence 图生图_1821408374780268546.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `ControlNetApply`
- `ControlNetLoader`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `HD UltimateSDUpscale`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `MZ_ChatGLM3Loader`
- `MZ_ChatGLM3_V2`
- `MZ_IPAdapterAdvancedKolors`
- `MZ_IPAdapterModelLoaderKolors`
- `MZ_KolorsCLIPVisionLoader`
- `MZ_KolorsControlNetPatch`
- `MZ_KolorsUNETLoaderV2`
- `PatchModelAddDownscale`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy setNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
