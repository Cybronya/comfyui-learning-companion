---
name: image_to_image_controlnet_sampler_clip_10
type: Image To Image
frequency: 4
level: strong
coverage: 0.9425
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/LABUBU转绘3D立体插画_1937034572326424578.json, 图片生成/图生图/LABUBU转绘动漫游戏二次元_1936653899098935298.json, 图片生成/图生图/SD1.5 ControlNet+智能锐化 1.0_2098206538765783041.json, 图片生成/图生图/真人转绘3D立体插画_1937038246817746946.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/LABUBU转绘3D立体插画_1937034572326424578.json、图片生成/图生图/LABUBU转绘动漫游戏二次元_1936653899098935298.json、图片生成/图生图/SD1.5 ControlNet+智能锐化 1.0_2098206538765783041.json、图片生成/图生图/真人转绘3D立体插画_1937038246817746946.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `IPAdapterAdvanced` —— 3/4 个有
- `IPAdapterModelLoader` —— 3/4 个有
- `PrepImageForClipVision` —— 3/4 个有
- `WD14Tagger|pysssss` —— 3/4 个有
- `IPAdapterNoise` —— 2/4 个有
- `ImageSmartSharpen+` —— 1/4 个有
- `Morphology` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 4 | 91% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 75% |
| 调度器 | karras | - | 4 | 75% |
| 重绘幅度 | 1 | 0.1 - 1 | 4 | 50% |
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 75%
- 调度器 最常用 karras，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，4 个样本，取值分散，一致性仅 50%
- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
