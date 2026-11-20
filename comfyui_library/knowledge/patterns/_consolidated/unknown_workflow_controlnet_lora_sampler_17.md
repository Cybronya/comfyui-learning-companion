---
name: unknown_workflow_controlnet_lora_sampler_17
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.988
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, ZImageFunControlnet]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ZIB+LoRA+Controlnet生图_2020785046222802945.json, 平台全量/Z-Image Controlnet 2  最强局部重绘 换脸换装 真实无痕 万物迁移_2014201657894113282.json, 平台全量/Z-Image Controlnet2 12月最强局部重绘_2003439556055736322.json, 平台全量/极速版Z-Image最强局部重绘  Controlnet2 换脸换装 真实无痕 万物迁移_2016024662324547585.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/ZIB+LoRA+Controlnet生图_2020785046222802945.json、平台全量/Z-Image Controlnet 2  最强局部重绘 换脸换装 真实无痕 万物迁移_2014201657894113282.json、平台全量/Z-Image Controlnet2 12月最强局部重绘_2003439556055736322.json、平台全量/极速版Z-Image最强局部重绘  Controlnet2 换脸换装 真实无痕 万物迁移_2016024662324547585.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZImageFunControlnet`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `DifferentialDiffusion` —— 3/4 个有
- `ImageComposite+` —— 1/4 个有
- `InvertMask` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有
- `MaskFromColor+` —— 1/4 个有
- `OpenposePreprocessor` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 4 | 81% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，4 个样本，取值集中（一致性 81%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
