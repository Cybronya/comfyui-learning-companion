---
name: image_to_image_controlnet_inpaint_sampler_10
type: Image To Image
frequency: 2
level: weak
coverage: 0.7795
common_nodes: [CLIPTextEncodeHunyuanDiT, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, Image Comparer (rgthree), ImageConcanate, ImageScaleToTotalPixels, JjkText, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, TTPlanet_inpainting_Preprecessor, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/混元Dit局部重绘-手动蒙版_1950589761754976257.json, 图片生成/图生图/混元Dit局部重绘-自动识别版_1950422532752064514.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/混元Dit局部重绘-手动蒙版_1950589761754976257.json、图片生成/图生图/混元Dit局部重绘-自动识别版_1950422532752064514.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeHunyuanDiT`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `TTPlanet_inpainting_Preprecessor`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `BBoxesToSAM2` —— 1/2 个有
- `DownloadAndLoadQwenModel` —— 1/2 个有
- `LayerMask: LoadSAM2Model` —— 1/2 个有
- `LayerMask: SAM2UltraV2` —— 1/2 个有
- `QwenVLDetection` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
