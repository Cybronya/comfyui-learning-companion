---
name: unknown_workflow_video_lora_sampler_642
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.973333
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJ, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, String Literal, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ, easy int, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-VACE-图生视频&单图参考_1950455319556218882.json, 视频生成/图生视频/双图参考_1950519561194033153.json, 视频生成/文生视频/Wan2.2-VACE-文生视频_1950526542499729410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_642

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-VACE-图生视频&单图参考_1950455319556218882.json、视频生成/图生视频/双图参考_1950519561194033153.json、视频生成/文生视频/Wan2.2-VACE-文生视频_1950526542499729410.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJ`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `String Literal`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `Image Blank` —— 2/3 个有
- `ImageCompositeMasked` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `LayerMask: LoadFlorence2Model` —— 2/3 个有
- `LayerMask: ObjectDetectorFL2` —— 2/3 个有
- `LayerMask: SAM2Ultra` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `GetImageSize+` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImagePadKJ` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `InpaintPreprocessor` —— 1/3 个有
- `JWImageExtractFromBatch` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 3 | 100% |
| 重绘幅度 | beta | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 100%
- 重绘幅度 最常用 beta，3 个样本，一致性 100%
