---
name: text_to_image_sampler_clip_unet_26
type: Text To Image
frequency: 16
level: moderate
coverage: 0.913188
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima 动漫王者文生图_2057038503191605250.json, 图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json, 图片生成/文生图/anima文生图3lora工作流_2059246446616080386.json, 图片生成/文生图/anima文生图基础工作流_2057116788260954114.json, 图片生成/文生图/b-最新krea2文生图_2070050778475220994.json, 图片生成/文生图/boogu turbo文生图_2067882978142941186.json, 图片生成/文生图/boogu. image电商海报_2040459014437347330.json, 图片生成/文生图/boogu_base 文生图_2068898981547171841.json, 图片生成/文生图/boogu_base_example_2068252685769461761.json, 图片生成/文生图/boogu_base_文生图-支持复杂提示词_2069073383496708097.json, 图片生成/文生图/boogu_image_turbo 文生图_2074111380944408578.json, 图片生成/文生图/boogu_turbo_2069417901609799682.json, 图片生成/文生图/boogu_turbo文生图_2068959350126891010.json, 图片生成/文生图/boogu文生图_2069052782014984193.json, 图片生成/文生图/flux1-krea-文生图_1951258671458234369.json, 图片生成/文生图/文生图ZImage_2064901103308861442.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/anima 动漫王者文生图_2057038503191605250.json、图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json、图片生成/文生图/anima文生图3lora工作流_2059246446616080386.json、图片生成/文生图/anima文生图基础工作流_2057116788260954114.json、图片生成/文生图/b-最新krea2文生图_2070050778475220994.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 15/16 个有
- `ConditioningZeroOut` —— 12/16 个有
- `JjkText` —— 7/16 个有
- `RH_Translator` —— 5/16 个有
- `LoraLoaderModelOnly` —— 4/16 个有
- `PreviewImage` —— 3/16 个有
- `PrimitiveInt` —— 2/16 个有
- `Anything Everywhere3` —— 1/16 个有
- `DualCLIPLoader` —— 1/16 个有
- `Int` —— 1/16 个有
- `LoadImage` —— 1/16 个有
- `PromptBatchQueue` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 4 - 50 | 16 | 26% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4.5 | 16 | 39% |
| 采样算法 | er_sde | - | 16 | 31% |
| 调度器 | simple | - | 16 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 1024 | 512 - 1920 | 16 | 72% |
| 高度 | 1180 | 512 - 1536 | 16 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 4 - 50，16 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4.5，16 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 er_sde，16 个样本，一致性 31%
- 调度器 最常用 simple，16 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1920，16 个样本
- 高度 中位数 1180，观测区间 512 - 1536，16 个样本
