---
name: image_to_image_upscale_lora_sampler_66
type: Image To Image
frequency: 3
level: moderate
coverage: 0.842
common_nodes: [CLIPTextEncode, DualCLIPLoader, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux洗图工作流_1980098420092342273.json, 图片生成/图生图/高清修复工作流v2.0_1971575847595470849.json, 平台全量/服装材质纹理保留放大！拒绝涂抹感！_1936805018500517889.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux洗图工作流_1980098420092342273.json、图片生成/图生图/高清修复工作流v2.0_1971575847595470849.json、平台全量/服装材质纹理保留放大！拒绝涂抹感！_1936805018500517889.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `Image Lucy Sharpen` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `UltimateSDUpscaleNoUpscale` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 0.34 | 0.3 - 0.4 | 3 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 0.34，观测区间 0.3 - 0.4，3 个样本，取值集中（一致性 88%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
