---
name: unknown_workflow_sampler_clip_unet_7
type: Unknown Workflow
frequency: 39
level: weak
coverage: 0.937897
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nvidia Cosmos Predict2 T2I_1938596846677712898.json, 图片生成/文生图/Ovis文生图工作流_1997584970094952450.json, 图片生成/文生图/PBR材质生成 模型贴图生成 z-image+育碧开源CHORD模型_1998964415804399617.json, 图片生成/文生图/QWEN官方文生图工作流V1_1968150332159197185.json, 图片生成/文生图/Qwen image pruning——权重瘦身版_2073209712295899137.json, 图片生成/文生图/Qwen-Image 加速版文生图_1953378626261712898.json, 图片生成/文生图/Qwen-Image中文电商海报_1953059659532988418.json, 图片生成/文生图/Qwen-image PPT 制作_1955087487033118722.json, 图片生成/文生图/Qwen千问图像大模型_1953710081516994562.json, 图片生成/文生图/Qwen文生图_1957383820934836225.json, 图片生成/文生图/Y-Z-Image-turbo-workflow_1995084581466464257.json, 图片生成/文生图/Z-IAMGE 文生图_2042789497263362049.json, 图片生成/文生图/Z-Image Turbo 文生图_2012561031096176642.json, 图片生成/文生图/Z-Image Turbo 文生图_2013174546978836481.json, 图片生成/文生图/Z-Image-Turbo基础文生图-工作流_2011542094619353089.json, 图片生成/文生图/Z-Image-Turbo文生图_1994260229521162241.json, 图片生成/文生图/Z-Image-Turbo文生图（OpenClaw远程控制版本）_2020379259021303809.json, 图片生成/文生图/Z-Image文生图大模型：满血版的出图效果宣判封顶！_2016493247157243905.json, 图片生成/文生图/Z-image文生图_2098605302726873090.json, 图片生成/文生图/Z_image文生图极速版_2064941900221734914.json, 图片生成/文生图/Zimage文生图 4 步_2112430735486447618.json, 图片生成/文生图/chris_export_image_z_image_turbo_02_2004521005383118850.json, 图片生成/文生图/chris_export_image_z_image_turbo_2002908032482852866.json, 图片生成/文生图/danotebook-z-image-turbo_2062428549738487809.json, 图片生成/文生图/image_qwen_image_1953087441538322434.json, 图片生成/文生图/image_qwen_image_distill-10步蒸馏版_1960503206273085442.json, 图片生成/文生图/image_z_image_turbo_2058123503169269762.json, 图片生成/文生图/ovis-image-文生图工作流_1997464079977627649.json, 图片生成/文生图/qwen Image2512-文生图片生成视觉海报平面设计-封装优化版_2092630964051734530.json, 图片生成/文生图/z-image-turbo文生图_2081602813930594305.json, 图片生成/文生图/z-image-turbo文生图工作流_1997643407344513025.json, 图片生成/文生图/z-image文生图_2037067831744925697.json, 图片生成/文生图/z_image_turbo_飞速写实文生图_1994300683828527106.json, 图片生成/文生图/zimage-base文生图_2039943203540967425.json, 图片生成/文生图/【Z-Image-Turbo LoRA 一站式炼丹教程】手把手教你训练自己的猫咪LoRA，让自家猫咪“出现”在世界各地！_2004888505304182785.json, 图片生成/文生图/手把手教你训练LORA，配合Qwen Image大模型，生图一致性达到99%！_1981265802265616385.json, 图片生成/文生图/批量文生图_2033573673789034498.json, 图片生成/文生图/材质贴图生成_2018526649268051969.json, 图片生成/文生图/🎮育碧开源CHORD大模型，一句话生成3A游戏级PBR贴图！_2004035810066350082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 39 个 workflow 归纳得出（图片生成/文生图/Nvidia Cosmos Predict2 T2I_1938596846677712898.json、图片生成/文生图/Ovis文生图工作流_1997584970094952450.json、图片生成/文生图/PBR材质生成 模型贴图生成 z-image+育碧开源CHORD模型_1998964415804399617.json、图片生成/文生图/QWEN官方文生图工作流V1_1968150332159197185.json、图片生成/文生图/Qwen image pruning——权重瘦身版_2073209712295899137.json…）

- **类型**：Unknown Workflow
- **样本数**：39
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 39 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 35/39 个有
- `ConditioningZeroOut` —— 24/39 个有
- `Label (rgthree)` —— 5/39 个有
- `ChordLoadModel` —— 3/39 个有
- `ChordMaterialEstimation` —— 3/39 个有
- `ChordNormalToHeight` —— 3/39 个有
- `LoraLoaderModelOnly` —— 3/39 个有
- `ResizeAndPadImage` —— 3/39 个有
- `easy promptList` —— 1/39 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 50 | 39 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 39 | 29% |
| 采样算法 | euler | - | 39 | 56% |
| 调度器 | simple | - | 39 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 39 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/39 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 50，39 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，39 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，39 个样本，一致性 56%
- 调度器 最常用 simple，39 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，39 个样本，取值集中（一致性 100%）
- 高发问题（25/39 个样本）：Steps较低可能导致细节不足
