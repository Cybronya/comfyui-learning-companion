---
name: text_to_image_lora_sampler_clip_339
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9064
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785.json, 图片生成/图生图/Qwen Image 2512商业商品摄影Lora 单品棚拍电商主图生成_2098659266436616193.json, 图片生成/图生图/SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857.json, 图片生成/图生图/SDXL4.0图生图｜高质量图像生成基础工作流_2095970298251268098.json, 图片生成/文生图/SDXL图生图极速版 零成本快速图片风格转换_2098114830124281858.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_339

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785.json、图片生成/图生图/Qwen Image 2512商业商品摄影Lora 单品棚拍电商主图生成_2098659266436616193.json、图片生成/图生图/SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857.json、图片生成/图生图/SDXL4.0图生图｜高质量图像生成基础工作流_2095970298251268098.json、图片生成/文生图/SDXL图生图极速版 零成本快速图片风格转换_2098114830124281858.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `CheckpointLoaderSimple` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `ControlNetLoader` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `ControlNetApplyAdvanced` —— 1/5 个有
- `ControlNetApplySD3` —— 1/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `SetUnionControlNetType` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 0.8 | - | 2 | 75% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| LoRA 模型强度 | 0.65 | - | 2 | 46% |
| LoRA 文本强度 | 0.65 | - | 2 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- LoRA 文本强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
