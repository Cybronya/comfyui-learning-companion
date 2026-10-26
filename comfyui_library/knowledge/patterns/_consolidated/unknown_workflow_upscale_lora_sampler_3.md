---
name: unknown_workflow_upscale_lora_sampler_3
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.733455
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/文生图krea2_turbo+SeedVR2放大+极致4K画质 (1)_2085544228448464898.json, 图片生成/文生图/image_z_image_文生图+高清修复工作流_1949750428735070210.json, 图片生成/文生图/image_z_image_文生图+高清修复工作流_2051844222583623681.json, 图片生成/文生图/image_z_image_文生图+高清修复工作流_2052642708036046849.json, 图片生成/文生图/image_z_image_文生图+高清修复工作流_2055189350849236994.json, 图片生成/文生图/image_z_image_文生图+高清修复工作流_2059558030781534210.json, 图片生成/文生图/image_z_image_文生图+高清修复工作流_2060289625578627073.json, 图片生成/文生图/qwen-image-2512-文生图-袜子设计稿_2009892327812239362.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2071433989394620417.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2082363616162045954.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2082367656837079041.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2082757941278625794.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2082760082005250049.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2084542000178749441.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2084997582266388481.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2089256377515593729.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2089267305149722625.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2089509829680386049.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2089524938330951681.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2090257712734097410.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2092091186575134721.json, 视频生成/文生视频/文生图krea2_turbo+SeedVR2放大+极致4K画质_2084528488534601730.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/文生图krea2_turbo+SeedVR2放大+极致4K画质 (1)_2085544228448464898.json、图片生成/文生图/image_z_image_文生图+高清修复工作流_1949750428735070210.json、图片生成/文生图/image_z_image_文生图+高清修复工作流_2051844222583623681.json、图片生成/文生图/image_z_image_文生图+高清修复工作流_2052642708036046849.json、图片生成/文生图/image_z_image_文生图+高清修复工作流_2055189350849236994.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 21/22 个有
- `PreviewImage` —— 21/22 个有
- `easy cleanGpuUsed` —— 21/22 个有
- `ImageScaleToTotalPixels` —— 16/22 个有
- `LayerUtility: PurgeVRAM V2` —— 16/22 个有
- `CR Text Concatenate` —— 15/22 个有
- `Float` —— 15/22 个有
- `KSamplerAdvanced` —— 15/22 个有
- `Seed (rgthree)` —— 15/22 个有
- `Text` —— 15/22 个有
- `VAEEncode` —— 15/22 个有
- `PlaySound|pysssss` —— 7/22 个有
- `ImageScaleBy` —— 6/22 个有
- `CR Text` —— 1/22 个有
- `LayerColor: Brightness & Contrast` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 22 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler_ancestral | - | 22 | 68% |
| 调度器 | beta57 | - | 22 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，22 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，22 个样本，一致性 68%
- 调度器 最常用 beta57，22 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 高发问题（22/22 个样本）：Steps较低可能导致细节不足
