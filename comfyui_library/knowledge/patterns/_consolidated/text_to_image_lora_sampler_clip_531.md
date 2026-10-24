---
name: text_to_image_lora_sampler_clip_531
type: Text To Image
frequency: 3
level: weak
coverage: 0.889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Qwen2511-角色复刻极简工作流_2083813171214770177.json, 数字人/数字人/角色复刻极简工作流｜Qwen2511数字人快速生成_2088770876085985282.json, 视频生成/图生视频/5倍噌噌噌加速｜FLUX Nunchaku文生图生视频_2091234693151805442.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_531

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/Qwen2511-角色复刻极简工作流_2083813171214770177.json、数字人/数字人/角色复刻极简工作流｜Qwen2511数字人快速生成_2088770876085985282.json、视频生成/图生视频/5倍噌噌噌加速｜FLUX Nunchaku文生图生视频_2091234693151805442.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `TTResolutionSelector` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 512 | 3 | 9% |
| 高度 | 80 | 80 - 512 | 3 | 9% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 512，3 个样本，取值分散，一致性仅 9%
- 高度 中位数 80，观测区间 80 - 512，3 个样本，取值分散，一致性仅 9%
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
