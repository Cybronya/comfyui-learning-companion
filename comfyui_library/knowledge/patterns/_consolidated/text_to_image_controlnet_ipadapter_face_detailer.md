---
name: text_to_image_controlnet_ipadapter_face_detailer
type: Text To Image
frequency: 5
level: strong
coverage: 0.8104
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, EmptyLatentImage, FaceDetailer, ImageResize+, JjkText, KSampler, LoadImage, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_IPAdapterAdvancedKolors, MZ_IPAdapterModelLoaderKolors, MZ_KolorsCLIPVisionLoader, MZ_KolorsControlNetPatch, MZ_KolorsUNETLoaderV2, MiDaS-NormalMapPreprocessor, PatchModelAddDownscale, PreviewImage, SAMLoader, SaveImage, ShowText|pysssss, TextCombinerTwo, UltralyticsDetectorProvider, VAEDecode, VAELoader, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/不用请模特找各种姿势，各种视角姿势直接出_1884248852613025793.json, 图片生成/图生图/服装设计模特效果图人物一致性_1882638164387942402.json, 平台全量/【实验流】Kolor  人物多视图 IPA+Face Detailer_1819570243533713409.json, 平台全量/人物多视图_1819213607627567105.json, 平台全量/服装设计模特效果图人物一致性_2033811259002462209.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_face_detailer

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/不用请模特找各种姿势，各种视角姿势直接出_1884248852613025793.json、图片生成/图生图/服装设计模特效果图人物一致性_1882638164387942402.json、平台全量/【实验流】Kolor  人物多视图 IPA+Face Detailer_1819570243533713409.json、平台全量/人物多视图_1819213607627567105.json、平台全量/服装设计模特效果图人物一致性_2033811259002462209.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 1/5 个有
- `Florence2Run` —— 1/5 个有
- `ImageUpscaleWithModelBatched` —— 1/5 个有
- `Translate2Chinese|fofo` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 5 | 100% |
| 采样算法 | dpmpp_sde | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1248 | 1248 - 1248 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1248，观测区间 1248 - 1248，5 个样本，取值集中（一致性 100%）
