---
name: image_to_image_controlnet_sampler_clip_17
type: Image To Image
frequency: 3
level: strong
coverage: 0.822
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleBy, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux量化版高清修复_1966727739929735170.json, "图片生成/图生图/默语细化,二次放大_1963045256818298882.json", 平台全量/Flux_ControlNet Upscaler 高清放大模型直接用_1961788462322139138.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux量化版高清修复_1966727739929735170.json、图片生成/图生图/默语细化,二次放大_1963045256818298882.json、平台全量/Flux_ControlNet Upscaler 高清放大模型直接用_1961788462322139138.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `Text to Conditioning` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
