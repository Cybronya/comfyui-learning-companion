---
name: unknown_workflow_controlnet_sampler_clip_12
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8635
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResize+, KSamplerAdvanced, LoadImage, ModelPatchLoader, PrimitiveStringMultiline, QwenImageDiffsynthControlnet, ResolutionSelector, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/VividMuse_Z-Image-ControlNet+Krea2-HiRes_2075384130866601986.json, 图片生成/图生图/VividMuse_Z-Image-ControlNet+Krea2-HiRes_2075393781821693953.json, 图片生成/文生图/VividMuse Krea2 ControlNet VS Z-Image ControlNet_2079206301841846273.json, 图片生成/文生图/VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/VividMuse_Z-Image-ControlNet+Krea2-HiRes_2075384130866601986.json、图片生成/图生图/VividMuse_Z-Image-ControlNet+Krea2-HiRes_2075393781821693953.json、图片生成/文生图/VividMuse Krea2 ControlNet VS Z-Image ControlNet_2079206301841846273.json、图片生成/文生图/VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchLoader`
- `PrimitiveStringMultiline`
- `QwenImageDiffsynthControlnet`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `VAEDecodeTiled` —— 3/4 个有
- `VAEEncodeTiled` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy imageColorMatch` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `Krea2ControlApply` —— 1/4 个有
- `Krea2ControlImageEncode` —— 1/4 个有
- `Krea2ControlLoRALoader` —— 1/4 个有
- `easy loraStack` —— 1/4 个有
- `easy loraStackApply` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 100% |
| 重绘幅度 | kl_optimal | - | 4 | 75% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 100%
- 重绘幅度 最常用 kl_optimal，4 个样本，一致性 75%
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
