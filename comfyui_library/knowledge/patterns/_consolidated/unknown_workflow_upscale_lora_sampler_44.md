---
name: unknown_workflow_upscale_lora_sampler_44
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8695
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, ResolutionSelector, SaveImage, Seed (rgthree), UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy promptList]
problems: []
missing: []
members: [图片生成/文生图/VividMuse Z-Image+Krea2高清修复_2073277061501902849.json, 图片生成/文生图/VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_44

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/VividMuse Z-Image+Krea2高清修复_2073277061501902849.json、图片生成/文生图/VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LayerColor: ColorAdapter` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `ModelPatchLoader` —— 1/2 个有
- `QwenImageDiffsynthControlnet` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8.5 | - | 2 | 94% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8.5，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
