---
name: text_to_image_lora_sampler_clip_427
type: Text To Image
frequency: 4
level: weak
coverage: 0.92325
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785.json, 图片生成/图生图/Flux.1-controlnet工作流_2113996622580506626.json, 图片生成/图生图/SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857.json, 图片生成/图生图/SDXL4.0图生图｜高质量图像生成基础工作流_2095970298251268098.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_427

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785.json、图片生成/图生图/Flux.1-controlnet工作流_2113996622580506626.json、图片生成/图生图/SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857.json、图片生成/图生图/SDXL4.0图生图｜高质量图像生成基础工作流_2095970298251268098.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `CLIPLoader` —— 3/4 个有
- `ControlNetLoader` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `ControlNetApplyAdvanced` —— 2/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `SetUnionControlNetType` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `ControlNetApplySD3` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 4 | 2% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 0.02 - 1 | 4 | 44% |
| ControlNet 权重 | 1 | 0.6 - 1 | 3 | 78% |
| 宽度 | 80 | 80 - 352 | 4 | 20% |
| 高度 | 80 | 80 - 168 | 4 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，4 个样本，取值分散，一致性仅 2%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.02 - 1，4 个样本，取值分散，一致性仅 44%
- ControlNet 权重 中位数 1，观测区间 0.6 - 1，3 个样本
- 宽度 中位数 80，观测区间 80 - 352，4 个样本，取值分散，一致性仅 20%
- 高度 中位数 80，观测区间 80 - 168，4 个样本
- 风险：重绘幅度 观测到 0.02，低于常用下限 0.1（）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
