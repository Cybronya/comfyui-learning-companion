---
name: image_to_image_controlnet_sampler_clip_16
type: Image To Image
frequency: 2
level: weak
coverage: 0.8465
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleBy, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: PurgeVRAM, LoadImage, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux量化版高清修复_1966727739929735170.json, "图片生成/图生图/默语细化,二次放大_1963045256818298882.json"]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux量化版高清修复_1966727739929735170.json、图片生成/图生图/默语细化,二次放大_1963045256818298882.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
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
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `ArgosTranslateTextNode` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `Text to Conditioning` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.75 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
