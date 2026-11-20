---
name: text_to_image_controlnet_ipadapter_face_detailer
type: Text To Image
frequency: 2
level: weak
coverage: 0.813
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, EmptyLatentImage, FaceDetailer, ImageResize+, JjkText, KSampler, LoadImage, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_IPAdapterAdvancedKolors, MZ_IPAdapterModelLoaderKolors, MZ_KolorsCLIPVisionLoader, MZ_KolorsControlNetPatch, MZ_KolorsUNETLoaderV2, MiDaS-NormalMapPreprocessor, PatchModelAddDownscale, PreviewImage, SAMLoader, SaveImage, ShowText|pysssss, TextCombinerTwo, UltralyticsDetectorProvider, VAEDecode, VAELoader, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/不用请模特找各种姿势，各种视角姿势直接出_1884248852613025793.json, 图片生成/图生图/服装设计模特效果图人物一致性_1882638164387942402.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/不用请模特找各种姿势，各种视角姿势直接出_1884248852613025793.json、图片生成/图生图/服装设计模特效果图人物一致性_1882638164387942402.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `EmptyLatentImage`
- `FaceDetailer`
- `ImageResize+`
- `JjkText`
- `KSampler`
- `LoadImage`
- `MZ_ChatGLM3Loader`
- `MZ_ChatGLM3_V2`
- `MZ_IPAdapterAdvancedKolors`
- `MZ_IPAdapterModelLoaderKolors`
- `MZ_KolorsCLIPVisionLoader`
- `MZ_KolorsControlNetPatch`
- `MZ_KolorsUNETLoaderV2`
- `MiDaS-NormalMapPreprocessor`
- `PatchModelAddDownscale`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `WD14Tagger|pysssss`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1248 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1248，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
