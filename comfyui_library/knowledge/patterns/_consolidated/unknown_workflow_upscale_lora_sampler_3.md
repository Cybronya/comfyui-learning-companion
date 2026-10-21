---
name: unknown_workflow_upscale_lora_sampler_3
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.73965
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [PlaySound|pysssss, easy cleanGpuUsed]
members: [图片生成/文生图/1949750428735070210.json, 图片生成/文生图/AA--8步加速-Zimage-base-蒸馏加速lora+超清放大_2026691270235660289.json, 图片生成/文生图/Z-Image_Base+SeedVR2 （BF16版模型）高清放大RH在线工作流_2017118139036737537.json, 图片生成/文生图/image_z_image_文生图+高清修复工作流_2059558030781534210.json, 图片生成/文生图/image_z_image_文生图+高清修复工作流_2060289625578627073.json, 图片生成/文生图/qwen-image-2512-文生图-袜子设计稿_2009892327812239362.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2071433989394620417.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2082363616162045954.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2082367656837079041.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2082757941278625794.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2082760082005250049.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2084542000178749441.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2084997582266388481.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2089256377515593729.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2089267305149722625.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2089509829680386049.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2089524938330951681.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2090257712734097410.json, 图片生成/文生图/文生图krea2_turbo+SeedVR2放大+极致4K画质_2092091186575134721.json, 视频生成/文生视频/文生图krea2_turbo+SeedVR2放大+极致4K画质_2084528488534601730.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/1949750428735070210.json、图片生成/文生图/AA--8步加速-Zimage-base-蒸馏加速lora+超清放大_2026691270235660289.json、图片生成/文生图/Z-Image_Base+SeedVR2 （BF16版模型）高清放大RH在线工作流_2017118139036737537.json、图片生成/文生图/image_z_image_文生图+高清修复工作流_2059558030781534210.json、图片生成/文生图/image_z_image_文生图+高清修复工作流_2060289625578627073.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 19/20 个有
- `ConditioningZeroOut` —— 18/20 个有
- `GetNode` —— 18/20 个有
- `ModelSamplingAuraFlow` —— 18/20 个有
- `SetNode` —— 18/20 个有
- `easy cleanGpuUsed` —— 18/20 个有
- `PreviewImage` —— 17/20 个有
- `ImageScaleToTotalPixels` —— 15/20 个有
- `LayerUtility: PurgeVRAM V2` —— 15/20 个有
- `CR Text Concatenate` —— 14/20 个有
- `Float` —— 14/20 个有
- `KSamplerAdvanced` —— 14/20 个有
- `Seed (rgthree)` —— 14/20 个有
- `Text` —— 14/20 个有
- `VAEEncode` —— 14/20 个有
- `PlaySound|pysssss` —— 4/20 个有
- `ImageScaleBy` —— 3/20 个有
- `INTConstant` —— 2/20 个有
- `CR Text` —— 1/20 个有
- `LayerColor: Brightness & Contrast` —— 1/20 个有
- `ModelSamplingZImage` —— 1/20 个有
- `easy clearCacheAll` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 20 | 20 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 20 | 31% |
| 采样算法 | euler_ancestral | - | 20 | 70% |
| 调度器 | beta57 | - | 20 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 20，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，20 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler_ancestral，20 个样本，一致性 70%
- 调度器 最常用 beta57，20 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（19/20 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：PlaySound|pysssss、easy cleanGpuUsed
