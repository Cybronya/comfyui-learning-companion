---
name: text_to_image_sampler_clip_unet_56
type: Text To Image
frequency: 12
level: weak
coverage: 0.9085
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS_BASE_SFT的人像资产测试_2111781812916801538.json, 图片生成/文生图/MOSS与Krea2双模型文生图 高质量图像生成处理工具_2113761690222415874.json, 图片生成/文生图/MOSS与Krea2联合文生图｜双模型加持创意生图更出片_2113529543649751042.json, 图片生成/文生图/MOSS动漫加速工作流 动漫游戏角色文生图处理工具_2113700438838177794.json, 图片生成/文生图/MOSS动漫加速工作流_2113206327819456514.json, 图片生成/文生图/MOSS动漫加速工作流_2115254285742198786.json, 图片生成/文生图/MOSS动漫加速工作流｜动漫角色游戏角色文生图快速产出_2113510899704225793.json, 图片生成/文生图/MOSS文生图2K极速 人物特效角色一致性生成工具_2114130557742444546.json, 图片生成/文生图/MOSS文生图2K极速 角色设计表演高速生成工具_2113734631899090946.json, 图片生成/文生图/MOSS文生图2K极速版 写实美少女图像生成工具_2113774445595811841.json, 图片生成/文生图/MOSS文生图2K极速版 写实美少女高速图像生成工具_2113483541777567746.json, 图片生成/文生图/MOSS文生图2K极速版工作流，美少女写实风一键生成高清图_2114460846381420546.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_56

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/MOSS_BASE_SFT的人像资产测试_2111781812916801538.json、图片生成/文生图/MOSS与Krea2双模型文生图 高质量图像生成处理工具_2113761690222415874.json、图片生成/文生图/MOSS与Krea2联合文生图｜双模型加持创意生图更出片_2113529543649751042.json、图片生成/文生图/MOSS动漫加速工作流 动漫游戏角色文生图处理工具_2113700438838177794.json、图片生成/文生图/MOSS动漫加速工作流_2113206327819456514.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `孤海注释` —— 10/12 个有
- `JjkText` —— 9/12 个有
- `solarL_SaveImagesToZip` —— 9/12 个有
- `EmptyFlux2LatentImage` —— 7/12 个有
- `SkipLayerGuidanceDiTSimple` —— 7/12 个有
- `Fast Groups Bypasser (rgthree)` —— 5/12 个有
- `CR Prompt Text` —— 4/12 个有
- `JoinStringMulti` —— 4/12 个有
- `ModelSamplingAuraFlow` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `SeedNode` —— 4/12 个有
- `CR Text` —— 1/12 个有
- `FacialCustomization` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 12 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 3.5 - 5 | 12 | 91% |
| 采样算法 | er_sde | - | 12 | 75% |
| 调度器 | beta | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 1024 | 12 | 0% |
| 高度 | 80 | 80 - 1024 | 12 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，12 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3.5 - 5，12 个样本，取值集中（一致性 91%）
- 采样算法 最常用 er_sde，12 个样本，一致性 75%
- 调度器 最常用 beta，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，12 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，12 个样本，取值分散，一致性仅 0%
- 高发问题（14/12 个样本）：Steps较低可能导致细节不足
