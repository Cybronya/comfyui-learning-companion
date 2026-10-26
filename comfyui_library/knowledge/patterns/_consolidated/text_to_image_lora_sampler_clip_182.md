---
name: text_to_image_lora_sampler_clip_182
type: Text To Image
frequency: 10
level: weak
coverage: 0.9656
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z_image角色生成【文生图】_2050492161661128706.json, 图片生成/文生图/Zimage-ART文生图_2017256373024722946.json, 图片生成/文生图/Zimage图片处理（4K文生图）_2016847780504936449.json, 图片生成/文生图/pipi-anima-普通采样器基础文生图工作流_2064683171064672258.json, 图片生成/文生图/qwen2512文生图泳装系列_2041408599649423361.json, 图片生成/文生图/qwen_edit_2512_越真实文生图-真实去ai味_2010517531177521153.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2098225838008389634.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2099331628756725762.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2099337911668924418.json, 图片生成/文生图/👾怪獸-Z-Image 文生图圣诞特集👾_1996136993329496065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z_image角色生成【文生图】_2050492161661128706.json、图片生成/文生图/Zimage-ART文生图_2017256373024722946.json、图片生成/文生图/Zimage图片处理（4K文生图）_2016847780504936449.json、图片生成/文生图/pipi-anima-普通采样器基础文生图工作流_2064683171064672258.json、图片生成/文生图/qwen2512文生图泳装系列_2041408599649423361.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/10 个有
- `ConditioningZeroOut` —— 4/10 个有
- `QZ_ResolutionPreset` —— 3/10 个有
- `DyPE_FLUX` —— 1/10 个有
- `FastFilmGrain` —— 1/10 个有
- `LayerColor: BrightnessContrastV2` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 10 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 10 | 25% |
| 采样算法 | euler | - | 10 | 50% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1052 | 768 - 2560 | 10 | 59% |
| 高度 | 1392 | 1024 - 1920 | 10 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，10 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，10 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 768 - 2560，10 个样本
- 高度 中位数 1392，观测区间 1024 - 1920，10 个样本
