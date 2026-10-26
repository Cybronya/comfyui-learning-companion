---
name: unknown_workflow_sampler_clip_unet_24
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.909652
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【Qwen 爆款神器】朋友圈_商业海报一键生成！_2104408211523719170.json, 图片生成/图生图/丝绸珠宝陈列LoRA-穿戴甲产品图工作流_2094452152767963138.json, 图片生成/图生图/大理石美甲摆拍-穿戴甲产品图工作流_2094401063536386049.json, 图片生成/文生图/001.Z-image生图巅峰002.文生图.json_2033717053093318658.json, 图片生成/文生图/002.Qwen编辑之王012.文生图Q版3D人物_2034643730707255297.json, 图片生成/文生图/1-图像生成 (T2I) Z-Image Turbo_ Fast Image 工作流_2053392780503859202.json, 图片生成/文生图/2029714470322315266.json, 图片生成/文生图/251207-02.Z_image_turbo文生图_1997679556008022018.json, 图片生成/文生图/3D盲盒潮玩手办-文生图_2094262553378648065.json, 图片生成/文生图/4步极速文生图Qwen-image！艾橘溪_1952538030328492034.json, 图片生成/文生图/56.tonnie-zimage文生图_1993951157917777921.json, 图片生成/文生图/Qwen Image 中文文生图_1952919451249348609.json, 图片生成/文生图/Qwen 朋友圈日签海报设计 V1.0_1955900129352011777.json, 图片生成/文生图/Qwen 电商小票创意海报 工作流 V1.0_1959790560150237186.json, 图片生成/文生图/Qwen+朋友圈、海报设计+V1.0_1986046293481050114.json, 图片生成/文生图/Qwen+朋友圈、海报设计+V1.0文生图_2100404141968412674.json, 图片生成/文生图/Qwen+朋友圈、海报设计+V1.0文生图_2100492455136288770.json, 图片生成/文生图/Qwen+朋友圈日签海报封面设计+V1.0_1999336951855579137.json, 图片生成/文生图/Qwen-image-lora-文生图工作流_1961062588018835457.json, 图片生成/文生图/Qwen-image-lora-文生图工作流_1973970749973204993.json, 图片生成/文生图/Z Image 小强模型极速出图_1993947409080401922.json, 图片生成/文生图/Z Image 文生图_1993906798906327041.json, 图片生成/文生图/z-image turbo + flux2 klein 高质感生图流_2016531485704065026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/【Qwen 爆款神器】朋友圈_商业海报一键生成！_2104408211523719170.json、图片生成/图生图/丝绸珠宝陈列LoRA-穿戴甲产品图工作流_2094452152767963138.json、图片生成/图生图/大理石美甲摆拍-穿戴甲产品图工作流_2094401063536386049.json、图片生成/文生图/001.Z-image生图巅峰002.文生图.json_2033717053093318658.json、图片生成/文生图/002.Qwen编辑之王012.文生图Q版3D人物_2034643730707255297.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 20/23 个有
- `LoraLoader` —— 14/23 个有
- `PreviewImage` —— 11/23 个有
- `UpscaleModelLoader` —— 8/23 个有
- `UltimateSDUpscale` —— 7/23 个有
- `PathchSageAttentionKJ` —— 4/23 个有
- `Text` —— 4/23 个有
- `Image Comparer (rgthree)` —— 2/23 个有
- `ImageScaleBy` —— 2/23 个有
- `VAEEncode` —— 2/23 个有
- `easy cleanGpuUsed` —— 2/23 个有
- `ConditioningZeroOut` —— 1/23 个有
- `EmptyFlux2LatentImage` —— 1/23 个有
- `GetImageSize` —— 1/23 个有
- `ImageUpscaleWithModel` —— 1/23 个有
- `ReferenceLatent` —— 1/23 个有
- `easy imageColorMatch` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.8 - 1 | 14 | 89% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 14 | 89% |
| 采样步数 | 25 | 4 - 50 | 22 | 45% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 7 | 22 | 36% |
| 采样算法 | euler | - | 22 | 82% |
| 调度器 | simple | - | 22 | 86% |
| 重绘幅度 | 1 | 0.15 - 1 | 22 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.8 - 1，14 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，14 个样本，取值集中（一致性 89%）
- 采样步数 中位数 25，观测区间 4 - 50，22 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 7，22 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，22 个样本，一致性 82%
- 调度器 最常用 simple，22 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，22 个样本，取值集中（一致性 82%）
