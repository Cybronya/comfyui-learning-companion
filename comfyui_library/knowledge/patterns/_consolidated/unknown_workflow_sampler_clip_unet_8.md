---
name: unknown_workflow_sampler_clip_unet_8
type: Unknown Workflow
frequency: 36
level: moderate
coverage: 0.998528
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image最新千问文生图_1993894546499108866.json, 图片生成/文生图/Z-image 来袭，这才是真正的降维打击！_1994248474698989570.json, 图片生成/文生图/Z-image 极简基础工作流_2017891493830205441.json, 图片生成/文生图/Z-image-Turbo真实文生图_2067573810974519298.json, 图片生成/文生图/Z-image-base  文生图工作流_2016356755948703746.json, 图片生成/文生图/Z-image-base  电影分镜、游戏美术、高端商业摄影_2017866317071650817.json, 图片生成/文生图/Z-image-base 文生图-高细节_2016335325617987585.json, 图片生成/文生图/Z-image-base 生图多样性_2016234401843122178.json, 图片生成/文生图/Z-image-base_2016195556967714818.json, 图片生成/文生图/Z-image-base_2018237442960138241.json, 图片生成/文生图/Z-image-base_2042138409904377858.json, 图片生成/文生图/Z-image-base_2057267276319121409.json, 图片生成/文生图/Z-image-base基础文生图工作流_2016406345590775810.json, 图片生成/文生图/Z-image-base文生图-质感爆炸！_2020689012381454337.json, 图片生成/文生图/Z-image-base文生图_2016310014306160641.json, 图片生成/文生图/Z-image-base文生图_2016773694768553985.json, 图片生成/文生图/Z-image-base文生图_2017044822808338433.json, 图片生成/文生图/Z-image-base文生图_2019404038776823810.json, 图片生成/文生图/Z-image-base文生图_2020836862188851201.json, 图片生成/文生图/Z-image_turbo生图急速版_2036675538508587010.json, 图片生成/文生图/Z-image_turbo生图急速版、全量版_2038263362722729985.json, 图片生成/文生图/Z-image_zimage_文生图_超真实感_2039246037906366465.json, 图片生成/文生图/Z-image_zimage_文生图_超真实感_2042149760525668353.json, 图片生成/文生图/Z-image_zimage_文生图_超真实感_2042524425781780481.json, 图片生成/文生图/Z-image_zimage_文生图_超真实感_2042822338177142786.json, 图片生成/文生图/Z-image_zimage_文生图_超真实感_2042900414516961281.json, 图片生成/文生图/Z-image_zimage_文生图工作流 Base版_2039923913303531522.json, 图片生成/文生图/Z-image_zimage_文生图工作流_2019697317217046529.json, 图片生成/文生图/Z-image_zimage_文生图工作流_2037725984199282690.json, 图片生成/文生图/Z-image文生图_2016334900588191745.json, 图片生成/文生图/Z-image文生图官方基础工作流 zimage_2041859367644962817.json, 图片生成/文生图/Z-image文生图官方基础工作流 zimage_2042620316907741185.json, 图片生成/文生图/Z-image文生图官方基础工作流 zimage_2042822446759284738.json, 图片生成/文生图/Z-image最新文生图，超细腻画面_2018208815497351170.json, 图片生成/文生图/Z-image模型 文生图_2068898439915728897.json, 图片生成/文生图/chm文生图片工作流_2111389341728731137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 36 个 workflow 归纳得出（图片生成/文生图/Z-Image最新千问文生图_1993894546499108866.json、图片生成/文生图/Z-image 来袭，这才是真正的降维打击！_1994248474698989570.json、图片生成/文生图/Z-image 极简基础工作流_2017891493830205441.json、图片生成/文生图/Z-image-Turbo真实文生图_2067573810974519298.json、图片生成/文生图/Z-image-base  文生图工作流_2016356755948703746.json…）

- **类型**：Unknown Workflow
- **样本数**：36
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 36 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 35/36 个有
- `Int` —— 2/36 个有
- `CompressImages` —— 1/36 个有
- `PrimitiveStringMultiline` —— 1/36 个有
- `easy getNode` —— 1/36 个有
- `easy promptList` —— 1/36 个有
- `easy setNode` —— 1/36 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 8 - 50 | 36 | 56% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 8 | 36 | 53% |
| 采样算法 | res_multistep | - | 36 | 83% |
| 调度器 | simple | - | 36 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 36 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/36 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 8 - 50，36 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 8，36 个样本
- 采样算法 最常用 res_multistep，36 个样本，一致性 83%
- 调度器 最常用 simple，36 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，36 个样本，取值集中（一致性 100%）
