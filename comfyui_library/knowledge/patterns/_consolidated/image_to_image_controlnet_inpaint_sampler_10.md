---
name: image_to_image_controlnet_inpaint_sampler_10
type: Image To Image
frequency: 4
level: strong
coverage: 0.74975
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, ImageAndMaskPreview, ImageConcanate, ImagePadForOutpaint, KSampler, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingAuraFlow, PDIMAGE_LongerSize, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/01-07-01-QwenImage+InstantX超强局部重绘+扩图_1986833968727322625.json, 平台全量/Qwen Image InstanX超强局部重绘_1966396118634541058.json, 平台全量/Qwen Image InstanX超强扩图（支持文字）_1966386989530558465.json, 平台全量/【支持文字】Qwen Image InstanX超强扩图 无痕扩充_1966754719635058690.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/01-07-01-QwenImage+InstantX超强局部重绘+扩图_1986833968727322625.json、平台全量/Qwen Image InstanX超强局部重绘_1966396118634541058.json、平台全量/Qwen Image InstanX超强扩图（支持文字）_1966386989530558465.json、平台全量/【支持文字】Qwen Image InstanX超强扩图 无痕扩充_1966754719635058690.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImagePadForOutpaint`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `Anything Everywhere` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageMaskSwitch` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `PreviewBridge` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
