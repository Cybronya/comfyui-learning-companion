---
name: unknown_workflow_sampler_clip_unet_15
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.979062
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-base局部重绘_2016771278450991105.json, 图片生成/文生图/Z-Image（base）文生图_2016049580982407169.json, 图片生成/文生图/Z-image 文生图工作流_1995511350388523010.json, 图片生成/文生图/Z-image 极简基础工作流_2017891493830205441.json, 图片生成/文生图/Z-image-Turbo真实文生图_2067573810974519298.json, 图片生成/文生图/Z-image-base基础文生图工作流_2016406345590775810.json, 图片生成/文生图/Z-image-base文生图-质感爆炸！_2020689012381454337.json, 图片生成/文生图/Z-image-base文生图_2016310014306160641.json, 图片生成/文生图/Z-image-base文生图_2016773694768553985.json, 图片生成/文生图/Z-image-base文生图_2017044822808338433.json, 图片生成/文生图/Z-image-base文生图_2017123904447320065.json, 图片生成/文生图/【阡陌】Ovis Image文生图工作流_1999424887913578498.json, 图片生成/文生图/全量版Z_IMAGE文生图工作流_2068260369071689729.json, 图片生成/文生图/关键帧生成_2069402773254397953.json, 图片生成/文生图/在线-Z-T2I-1128_1994378488129986561.json, 图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/Z-Image-base局部重绘_2016771278450991105.json、图片生成/文生图/Z-Image（base）文生图_2016049580982407169.json、图片生成/文生图/Z-image 文生图工作流_1995511350388523010.json、图片生成/文生图/Z-image 极简基础工作流_2017891493830205441.json、图片生成/文生图/Z-image-Turbo真实文生图_2067573810974519298.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 15/16 个有
- `LoadImage` —— 3/16 个有
- `CustomAddLabel` —— 1/16 个有
- `DifferentialDiffusion` —— 1/16 个有
- `INTConstant` —— 1/16 个有
- `InpaintModelConditioning` —— 1/16 个有
- `MaskBlur+` —— 1/16 个有
- `MemoryCleaner` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 8 - 50 | 16 | 36% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 16 | 49% |
| 采样算法 | res_multistep | - | 16 | 69% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 0.85 - 1 | 16 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 8 - 50，16 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，16 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 res_multistep，16 个样本，一致性 69%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，16 个样本，取值集中（一致性 96%）
