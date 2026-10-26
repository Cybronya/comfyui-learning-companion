---
name: unknown_workflow_video_inpaint_upscale
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.75
common_nodes: [Anything Everywhere, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetImageSize, GetNode, Image Filter Adjustments, ImageConcanate, ImageCrop, ImageResize+, ImageScale, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, PreviewImage, RIFE VFI, SaveImage, SeedVR2, SeedVR2BlockSwap, SetNode, StyleModelApply, StyleModelLoader, Text Prompt (JPS), UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll, easy mathInt]
problems: []
missing: []
members: [图片生成/图生图/至尊电商_2073219699759992833.json, 数字人/数字人/至尊电商_1966680740526239745.json, 视频生成/图生视频/极致电商穿搭_2066873867511091201.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/至尊电商_2073219699759992833.json、数字人/数字人/至尊电商_1966680740526239745.json、视频生成/图生视频/极致电商穿搭_2066873867511091201.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize`
- `GetNode`
- `Image Filter Adjustments`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `ImageScale`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewImage`
- `RIFE VFI`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `StyleModelApply`
- `StyleModelLoader`
- `Text Prompt (JPS)`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy mathInt`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
