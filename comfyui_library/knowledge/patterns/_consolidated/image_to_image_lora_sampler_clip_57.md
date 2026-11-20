---
name: image_to_image_lora_sampler_clip_57
type: Image To Image
frequency: 7
level: weak
coverage: 0.871286
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/高清放大修复-2.0_8K_2087812199464132610.json, 图片生成/图生图/高清放大修复-2026年新版【真实细节】_2003273933614907393.json, 图片生成/图生图/👾怪獸-Qwen 2511-Unblur-Anything高清修复👾_2014653934102646786.json, 平台全量/Qwen-Edit  动漫转真人 Z-iamge增加质感 Seedv2 TPP高清放大_2019585445109174274.json, 平台全量/极致万物高清修复Qwen 2511-Unblur-Anything_2013925456612954113.json, 平台全量/极致高清修复-增加细节-消除AI感Qwen2511+Flux kontext_2022083211601387522.json, 平台全量/高清修复_增强细节Qwen_2019221898801975297.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/高清放大修复-2.0_8K_2087812199464132610.json、图片生成/图生图/高清放大修复-2026年新版【真实细节】_2003273933614907393.json、图片生成/图生图/👾怪獸-Qwen 2511-Unblur-Anything高清修复👾_2014653934102646786.json、平台全量/Qwen-Edit  动漫转真人 Z-iamge增加质感 Seedv2 TPP高清放大_2019585445109174274.json、平台全量/极致万物高清修复Qwen 2511-Unblur-Anything_2013925456612954113.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `ReferenceLatent` —— 6/7 个有
- `SeedVR2LoadDiTModel` —— 6/7 个有
- `SeedVR2LoadVAEModel` —— 6/7 个有
- `SeedVR2VideoUpscaler` —— 6/7 个有
- `ImageScaleBy` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `DualCLIPLoader` —— 3/7 个有
- `FluxGuidance` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `DownloadAndLoadFlorence2Model` —— 2/7 个有
- `Florence2Run` —— 2/7 个有
- `Latent Noise Injection` —— 2/7 个有
- `ShowText` —— 2/7 个有
- `easy imageSizeBySide` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 20 | 7 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 43% |
| 重绘幅度 | 0.42 | 0.1 - 1 | 7 | 38% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 20，7 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 43%
- 重绘幅度 中位数 0.42，观测区间 0.1 - 1，7 个样本，取值分散，一致性仅 38%
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
