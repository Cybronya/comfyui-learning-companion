---
name: image_to_image_ipadapter_sampler_clip_5
type: Image To Image
frequency: 2
level: weak
coverage: 0.389
common_nodes: [BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, Blur, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, CreateGradientFromCoords, CreateShapeMask, GetNode, GrowMaskWithBlur, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), Image Rembg (Remove Background), ImageResize+, KSampler, LoadAndApplyICLightUnet, LoadImage, MaskToImage, PrepImageForClipVision, PreviewImage, ResizeMask, SaveImage, SetNode, SplineEditor, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/渐变高级光源 IC-light V2 版本_1917596055444328450.json, 平台全量/IC-Light渐变光源重打光_1808761698449862658.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/渐变高级光源 IC-light V2 版本_1917596055444328450.json、平台全量/IC-Light渐变光源重打光_1808761698449862658.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：39%

## 共有节点

全部 2 个 workflow 都包含：
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `Blur`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `CreateGradientFromCoords`
- `CreateShapeMask`
- `GetNode`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `Image Rembg (Remove Background)`
- `ImageResize+`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `ResizeMask`
- `SaveImage`
- `SetNode`
- `SplineEditor`
- `VAEDecode`
- `VAEEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.98 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.98，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
