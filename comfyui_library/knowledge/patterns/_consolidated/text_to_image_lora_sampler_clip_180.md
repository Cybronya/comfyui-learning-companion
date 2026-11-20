---
name: text_to_image_lora_sampler_clip_180
type: Text To Image
frequency: 10
level: weak
coverage: 0.8503
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, ResizeImageMaskNode, ResolutionSelector, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SkipLayerGuidanceDiTSimple, TextGenerate, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/黑鹤001 MOSS-Image 文生图流整合移植RH版｜一键出图高清直出_2114161760012955650.json, 图片生成/文生图/黑鹤001 MOSS-Image-生图流（整合移植RH 版）_2114008445971161090.json, 平台全量/MOSS Turbo 八步生图_2119876669409423362.json, 平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2118457277727469569.json, 平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2119695228968984577.json, 平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2119711495486533633.json, 平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2119715014327234561.json, 平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2120049632129667074.json, 平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2120054990969593858.json, 平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2120079479115706369.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_180

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/黑鹤001 MOSS-Image 文生图流整合移植RH版｜一键出图高清直出_2114161760012955650.json、图片生成/文生图/黑鹤001 MOSS-Image-生图流（整合移植RH 版）_2114008445971161090.json、平台全量/MOSS Turbo 八步生图_2119876669409423362.json、平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2118457277727469569.json、平台全量/pipi-MOSS文生图提示词优化+seedVR2放大_2119695228968984577.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SkipLayerGuidanceDiTSimple`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 3/10 个有
- `LatentUpscaleBy` —— 3/10 个有
- `LoadImageOutput` —— 3/10 个有
- `孤海注释` —— 3/10 个有
- `忽略多组孤海` —— 2/10 个有
- `JjkText` —— 1/10 个有
- `solarL_SaveImagesToZip` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 10 | 70% |
| 高度 | 1024 | 80 - 1024 | 10 | 70% |
| 采样步数 | 1 | 1 - 4 | 8 | 28% |
| Prompt 约束强度(CFG) | 1 | 1 - 25 | 10 | 0% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，10 个样本
- 高度 中位数 1024，观测区间 80 - 1024，10 个样本
- 采样步数 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 25，10 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（14/10 个样本）：Steps较低可能导致细节不足
