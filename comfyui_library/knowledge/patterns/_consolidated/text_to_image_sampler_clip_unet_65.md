---
name: text_to_image_sampler_clip_unet_65
type: Text To Image
frequency: 7
level: moderate
coverage: 0.909857
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1982000492014379010.json, 图片生成/文生图/API - FLux文生图_2066848618040086529.json, 图片生成/文生图/API - FLux文生图_2091105641225080833.json, 图片生成/文生图/FLux文生图API工作流｜高质量图像生成_2095581101854121986.json, 图片生成/文生图/Krea2人物四视图工作流，人物角色角色设计文生图工具_2107516751167713281.json, 图片生成/文生图/好玩的文生图工作流｜人物类特效创意出图神器_2098761942302289921.json, 视频生成/图生视频/5倍噌噌噌加速｜FLUX Nunchaku文生图生视频_2091234693151805442.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_65

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1982000492014379010.json、图片生成/文生图/API - FLux文生图_2066848618040086529.json、图片生成/文生图/API - FLux文生图_2091105641225080833.json、图片生成/文生图/FLux文生图API工作流｜高质量图像生成_2095581101854121986.json、图片生成/文生图/Krea2人物四视图工作流，人物角色角色设计文生图工具_2107516751167713281.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `DualCLIPLoader` —— 6/7 个有
- `FluxGuidance` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `CLIPLoader` —— 4/7 个有
- `JjkText` —— 4/7 个有
- `solarL_SaveImagesToZip` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `LoraLoader` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `easy int` —— 3/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `LatentUpscale` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `NunchakuFluxDiTLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 67% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 50% |
| 采样算法 | er_sde | - | 7 | 57% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 1536 | 7 | 0% |
| 高度 | 80 | 80 - 864 | 7 | 7% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 50%
- 采样算法 最常用 er_sde，7 个样本，一致性 57%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1536，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 864，7 个样本，取值分散，一致性仅 7%
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
