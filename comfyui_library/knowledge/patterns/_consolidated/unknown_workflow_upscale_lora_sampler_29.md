---
name: unknown_workflow_upscale_lora_sampler_29
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.687333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Z-image D-OPSD文生图+高清修复_2059661332814852097.json, 图片生成/文生图/z-image BEYOND超越真实   文生图细节增强 噪声返回2次采样+seedvr2分块放大_2006269781057478658.json, 图片生成/文生图/zimage高级文生图，三阶段采样，带seedvr2+ttp放大，效果可达到商用级别_2004212112182439937.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image D-OPSD文生图+高清修复_2059661332814852097.json、图片生成/文生图/z-image BEYOND超越真实   文生图细节增强 噪声返回2次采样+seedvr2分块放大_2006269781057478658.json、图片生成/文生图/zimage高级文生图，三阶段采样，带seedvr2+ttp放大，效果可达到商用级别_2004212112182439937.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `KOOK_ImageCompression` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `Image to Noise` —— 1/3 个有
- `ImageCASharpening+` —— 1/3 个有
- `LatentBlend` —— 1/3 个有
- `LatentColorMatch` —— 1/3 个有
- `LayerColor: Brightness & Contrast` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 10 | 8 - 15 | 3 | 73% |
| 采样算法 | 1 | 1 - 2 | 3 | 65% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |
| 宽度 | 992 | - | 2 | 97% |
| 高度 | 1480 | - | 2 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 10，观测区间 8 - 15，3 个样本
- 采样算法 中位数 1，观测区间 1 - 2，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 宽度 中位数 992，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1480，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
