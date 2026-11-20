---
name: unknown_workflow_sampler_clip_unet_103
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.944727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS_4步_FP32模型 VS 25步_SFT模型 文生图工作流_2113618754377707521.json, 图片生成/文生图/MOSS_Image_SFT_BF16 + 4步加速LoRA 文生图工作流_2113944419647975426.json, 图片生成/文生图/Moss 文生图 2K分辨率直出_2113627882475053058.json, 图片生成/文生图/Moss-Base Fixed文生图_2112960445203177473.json, 图片生成/文生图/Moss-Image图像生成（官方示例版）_2111823655494840322.json, 图片生成/文生图/Moss-image+8步极速文生图_2112930768900149250.json, 图片生成/文生图/Moss-image-文生图-高质量-Base-SFT_2114528333923971074.json, 图片生成/文生图/pandy-MOSS-Image-50步文生图_2114240691202248706.json, 图片生成/文生图/pandy-MOSS-Image-8步加速文生图_2114246092383670273.json, 图片生成/文生图/【遇见AI】Moss image 文生图8步加速基础流_2112071294949879810.json, 图片生成/文生图/质感提升-MOSS-SFT_int8+观澜lora_2113835209383829506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_103

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/MOSS_4步_FP32模型 VS 25步_SFT模型 文生图工作流_2113618754377707521.json、图片生成/文生图/MOSS_Image_SFT_BF16 + 4步加速LoRA 文生图工作流_2113944419647975426.json、图片生成/文生图/Moss 文生图 2K分辨率直出_2113627882475053058.json、图片生成/文生图/Moss-Base Fixed文生图_2112960445203177473.json、图片生成/文生图/Moss-Image图像生成（官方示例版）_2111823655494840322.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SkipLayerGuidanceDiTSimple` —— 7/11 个有
- `ResolutionSelector` —— 6/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `Label (rgthree)` —— 2/11 个有
- `LoadImage` —— 2/11 个有
- `easy anythingIndexSwitch` —— 2/11 个有
- `ImageBatch` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 50 | 11 | 23% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 11 | 44% |
| 采样算法 | euler | - | 11 | 64% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 50，11 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，11 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，11 个样本，一致性 64%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
