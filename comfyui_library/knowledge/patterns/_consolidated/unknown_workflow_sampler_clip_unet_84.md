---
name: unknown_workflow_sampler_clip_unet_84
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.970818
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext-单图编辑_1957777844306018305.json, 图片生成/图生图/【角色一致性】kontext一键三视图_1941385374562467841.json, 图片生成/图生图/【角色生视图生成】flux kontext_1942377392872820737.json, 图片生成/图生图/一句话去除文字水印_2007189651940974593.json, 图片生成/图生图/万能改图 - Kontext Dev  单图模式_1939636345130098689.json, 图片生成/图生图/万能改图 - 双图模式_1939867866118459394.json, 图片生成/图生图/图片扩图 _kontext -2.0_1953103553411878914.json, 图片生成/文生图/FLUX Kontext DEV 图片编辑_1939140747582955521.json, 图片生成/文生图/Flux Kontext - 万能改图_1942739895523979266.json, 图片生成/文生图/Flux Kontext - 万能改图_1942746478307946498.json, 图片生成/文生图/Flux Kontext Dev单图模式_1938559858222551041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_84

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/kontext-单图编辑_1957777844306018305.json、图片生成/图生图/【角色一致性】kontext一键三视图_1941385374562467841.json、图片生成/图生图/【角色生视图生成】flux kontext_1942377392872820737.json、图片生成/图生图/一句话去除文字水印_2007189651940974593.json、图片生成/图生图/万能改图 - Kontext Dev  单图模式_1939636345130098689.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `ModelSamplingFlux` —— 10/11 个有
- `RH_Translator` —— 10/11 个有
- `FluxResolutionNode` —— 9/11 个有
- `ImageResize+` —— 8/11 个有
- `MathExpression|pysssss` —— 8/11 个有
- `Anything Everywhere` —— 2/11 个有
- `Anything Everywhere3` —— 2/11 个有
- `JWImageResizeByShorterSide` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `DF_Get_image_size` —— 1/11 个有
- `FluxKontextImageScale` —— 1/11 个有
- `GetImageSize+` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `ImagePadForOutpaintMasked_UTK` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `LoadImagesFromURL` —— 1/11 个有
- `RMBG` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 10 | 100% |
| 高度 | 1280 | 1280 - 1280 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，10 个样本，取值集中（一致性 100%）
