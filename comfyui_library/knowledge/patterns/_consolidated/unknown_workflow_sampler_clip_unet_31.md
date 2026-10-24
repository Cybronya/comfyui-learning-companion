---
name: unknown_workflow_sampler_clip_unet_31
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.895409
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【Qwen 爆款神器】朋友圈_商业海报一键生成！_2104408211523719170.json, 图片生成/图生图/丝绸珠宝陈列LoRA-穿戴甲产品图工作流_2094452152767963138.json, 图片生成/图生图/大理石美甲摆拍-穿戴甲产品图工作流_2094401063536386049.json, 图片生成/文生图/001.Z-image生图巅峰002.文生图.json_2033717053093318658.json, 图片生成/文生图/002.Qwen编辑之王012.文生图Q版3D人物_2034643730707255297.json, 图片生成/文生图/1-图像生成 (T2I) Z-Image Turbo_ Fast Image 工作流_2053392780503859202.json, 图片生成/文生图/2029714470322315266.json, 图片生成/文生图/251207-02.Z_image_turbo文生图_1997679556008022018.json, 图片生成/文生图/3D盲盒潮玩手办-文生图_2094262553378648065.json, 图片生成/文生图/4步极速文生图Qwen-image！艾橘溪_1952538030328492034.json, 图片生成/文生图/56.tonnie-zimage文生图_1993951157917777921.json, 图片生成/文生图/Qwen 朋友圈日签海报设计 V1.0_1955900129352011777.json, 图片生成/文生图/Qwen 电商小票创意海报 工作流 V1.0_1959790560150237186.json, 图片生成/文生图/Qwen+朋友圈、海报设计+V1.0_1986046293481050114.json, 图片生成/文生图/Qwen+朋友圈、海报设计+V1.0文生图_2100404141968412674.json, 图片生成/文生图/Qwen+朋友圈、海报设计+V1.0文生图_2100492455136288770.json, 图片生成/文生图/Qwen+朋友圈日签海报封面设计+V1.0_1999336951855579137.json, 图片生成/文生图/Qwen-image-lora-文生图工作流_1961062588018835457.json, 图片生成/文生图/Qwen-image-lora-文生图工作流_1973970749973204993.json, 图片生成/文生图/Ultimate SD 图像升频放大 Z-Image Turbo_2036815909616099329.json, 图片生成/文生图/Z Image 文生图_1993906798906327041.json, 图片生成/文生图/工作流基础系列8-QwenImage2512文生图工作流-基础向讲解此工作流_2044339209980354561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/【Qwen 爆款神器】朋友圈_商业海报一键生成！_2104408211523719170.json、图片生成/图生图/丝绸珠宝陈列LoRA-穿戴甲产品图工作流_2094452152767963138.json、图片生成/图生图/大理石美甲摆拍-穿戴甲产品图工作流_2094401063536386049.json、图片生成/文生图/001.Z-image生图巅峰002.文生图.json_2033717053093318658.json、图片生成/文生图/002.Qwen编辑之王012.文生图Q版3D人物_2034643730707255297.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 19/22 个有
- `LoraLoader` —— 14/22 个有
- `PreviewImage` —— 12/22 个有
- `UpscaleModelLoader` —— 10/22 个有
- `UltimateSDUpscale` —— 8/22 个有
- `Image Comparer (rgthree)` —— 3/22 个有
- `ImageScaleBy` —— 2/22 个有
- `ImageUpscaleWithModel` —— 2/22 个有
- `LoraLoaderModelOnly` —— 2/22 个有
- `PathchSageAttentionKJ` —— 2/22 个有
- `Text` —— 2/22 个有
- `VAEEncode` —— 2/22 个有
- `Seed (rgthree)` —— 1/22 个有
- `easy cleanGpuUsed` —— 1/22 个有
- `easy promptList` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.8 - 1 | 14 | 89% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 14 | 89% |
| 采样步数 | 25 | 4 - 50 | 21 | 43% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 7 | 21 | 34% |
| 采样算法 | euler | - | 21 | 86% |
| 调度器 | simple | - | 21 | 81% |
| 重绘幅度 | 1 | 0.15 - 1 | 21 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.8 - 1，14 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，14 个样本，取值集中（一致性 89%）
- 采样步数 中位数 25，观测区间 4 - 50，21 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 7，21 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，21 个样本，一致性 86%
- 调度器 最常用 simple，21 个样本，一致性 81%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，21 个样本，取值集中（一致性 81%）
- 高发问题（14/22 个样本）：Steps较低可能导致细节不足
