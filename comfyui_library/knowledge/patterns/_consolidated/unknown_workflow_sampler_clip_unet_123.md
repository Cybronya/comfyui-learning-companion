---
name: unknown_workflow_sampler_clip_unet_123
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9846
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image-base局部重绘_2016771278450991105.json, 图片生成/文生图/Z-Image_turbo造像模型文生图极速版_2049364318055043073.json, 图片生成/文生图/Z-Image（base）文生图_2016049580982407169.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2041531285021134849.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2041694117238939649.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042149150724198401.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042149662869692418.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042468324331757569.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042827110661758977.json, 图片生成/文生图/Z-image zimage 提示词反推 图生图 去AI味超真实感_2037758338104041474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_123

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z-Image-base局部重绘_2016771278450991105.json、图片生成/文生图/Z-Image_turbo造像模型文生图极速版_2049364318055043073.json、图片生成/文生图/Z-Image（base）文生图_2016049580982407169.json、图片生成/文生图/Z-image  zimage  文生图  工作流_2041531285021134849.json、图片生成/文生图/Z-image  zimage  文生图  工作流_2041694117238939649.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 9/10 个有
- `LoadImage` —— 4/10 个有
- `DifferentialDiffusion` —— 1/10 个有
- `InpaintModelConditioning` —— 1/10 个有
- `MaskBlur+` —— 1/10 个有
- `Qwen3_VQA` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 20 - 50 | 10 | 69% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 10 | 73% |
| 采样算法 | res_multistep | - | 10 | 90% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 0.85 - 1 | 10 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 20 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，10 个样本
- 采样算法 最常用 res_multistep，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，10 个样本，取值集中（一致性 95%）
