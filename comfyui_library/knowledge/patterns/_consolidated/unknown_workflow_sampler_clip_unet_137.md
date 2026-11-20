---
name: unknown_workflow_sampler_clip_unet_137
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8881
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/质感提升-MOSS-SFT_int8+观澜lora_2114882439335202818.json, 图片生成/文生图/FLUX 3 高质量文生图_2114203882040680450.json, 图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json, 图片生成/文生图/FLUX3 Image Klein 文生图_2111346567927123970.json, 图片生成/文生图/FLUX3 Image Klein 文生图（修复版·中文繁体招牌王）_2111323705954623489.json, 图片生成/文生图/Flux 3_Image_Klein开源版-文生图_2111064999098671105.json, 图片生成/文生图/KOOK MOSS Base 观澜文生图《8步加速》_2115993450721144834.json, 图片生成/文生图/KOOK MOSS Base 观澜文生图｜8步加速_2115950446585147394.json, 图片生成/文生图/KOOK MOSS SFT 观澜文生图｜可选8步加速_2115987305096900610.json, 图片生成/文生图/MOSS文生图-SFT_int8+观澜lora_2114627554517803009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_137

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/质感提升-MOSS-SFT_int8+观澜lora_2114882439335202818.json、图片生成/文生图/FLUX 3 高质量文生图_2114203882040680450.json、图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json、图片生成/文生图/FLUX3 Image Klein 文生图_2111346567927123970.json、图片生成/文生图/FLUX3 Image Klein 文生图（修复版·中文繁体招牌王）_2111323705954623489.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `SkipLayerGuidanceDiTSimple` —— 5/10 个有
- `孤海注释` —— 5/10 个有
- `Int` —— 3/10 个有
- `MuyeTextEditOutput` —— 3/10 个有
- `PrimitiveBoolean` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `Switch any [Crystools]` —— 3/10 个有
- `LoadImage` —— 2/10 个有
- `easy anythingIndexSwitch` —— 2/10 个有
- `PreviewImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20.5 | 8 - 25 | 10 | 70% |
| Prompt 约束强度(CFG) | 2 | 1 - 3 | 10 | 50% |
| 采样算法 | er_sde | - | 10 | 60% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20.5，观测区间 8 - 25，10 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 3，10 个样本
- 采样算法 最常用 er_sde，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
