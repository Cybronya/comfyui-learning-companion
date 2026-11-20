---
name: unknown_workflow_sampler_clip_unet_22
type: Unknown Workflow
frequency: 24
level: weak
coverage: 0.963333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/PBR材质生成 模型贴图生成 z-image+育碧开源CHORD模型_1998964415804399617.json, 图片生成/文生图/Qwen-Image 加速版文生图_1953378626261712898.json, 图片生成/文生图/Qwen-image PPT 制作_1955087487033118722.json, 图片生成/文生图/Qwen2512原生工作流_2114158316933963778.json, 图片生成/文生图/Qwen2512原生工作流_2114177531707482114.json, 图片生成/文生图/Z-Image文生图_2007450236398084098.json, 图片生成/文生图/Z_image文生图极速版_2064941900221734914.json, 图片生成/文生图/Zimage文生图 4 步_2112430735486447618.json, 图片生成/文生图/chris_export_image_z_image_turbo_02_2004521005383118850.json, 图片生成/文生图/chris_export_image_z_image_turbo_2002908032482852866.json, 图片生成/文生图/danotebook-z-image-turbo_2062428549738487809.json, 图片生成/文生图/image_z_image_turbo_2058123503169269762.json, 图片生成/文生图/image_z_image_turbo造像 去除ai油腻味文生图_1996224077834633218.json, 图片生成/文生图/image_z_turbo_文生图_原版无Lora_2004484063744454657.json, 图片生成/文生图/z-image-turbo文生图_2081602813930594305.json, 图片生成/文生图/z-image-turbo文生图工作流_1997643407344513025.json, 图片生成/文生图/z-image文生图_2037067831744925697.json, 图片生成/文生图/z_image_turbo文生图_2067946808487276545.json, 图片生成/文生图/z_image_turbo文生图透明_2067952553903611905.json, 图片生成/文生图/材质贴图生成_2018526649268051969.json, 图片生成/文生图/🎮育碧开源CHORD大模型，一句话生成3A游戏级PBR贴图！_2004035810066350082.json, 平台全量/PBR贴图生成器(育碧CHORD模型)_2005554224576561153.json, 平台全量/育碧PBR贴图工作流_2003729274735632386.json, 平台全量/🎮育碧开源CHORD大模型，一句话生成3A游戏级PBR贴图！_2002056249988530178.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/PBR材质生成 模型贴图生成 z-image+育碧开源CHORD模型_1998964415804399617.json、图片生成/文生图/Qwen-Image 加速版文生图_1953378626261712898.json、图片生成/文生图/Qwen-image PPT 制作_1955087487033118722.json、图片生成/文生图/Qwen2512原生工作流_2114158316933963778.json、图片生成/文生图/Qwen2512原生工作流_2114177531707482114.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 20/24 个有
- `ChordLoadModel` —— 6/24 个有
- `ChordMaterialEstimation` —— 6/24 个有
- `ChordNormalToHeight` —— 6/24 个有
- `ResizeAndPadImage` —— 6/24 个有
- `PrimitiveStringMultiline` —— 3/24 个有
- `BiRefNetRMBG` —— 1/24 个有
- `Label (rgthree)` —— 1/24 个有
- `LoadImage` —— 1/24 个有
- `easy cleanGpuUsed` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 50 | 24 | 1% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 24 | 35% |
| 采样算法 | euler | - | 24 | 50% |
| 调度器 | simple | - | 24 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 50，24 个样本，取值分散，一致性仅 1%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，24 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，24 个样本，一致性 50%
- 调度器 最常用 simple，24 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（24/24 个样本）：Steps较低可能导致细节不足
