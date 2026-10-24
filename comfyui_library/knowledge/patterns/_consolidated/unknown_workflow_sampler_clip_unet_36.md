---
name: unknown_workflow_sampler_clip_unet_36
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.990842
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo高质量文生图_2021205123837468673.json, 图片生成/文生图/Z-ImageBase+4步加速+文生图_2021786374671704065.json, 图片生成/文生图/Z-ImageBase+8步加速+文生图_2021754201637916674.json, 图片生成/文生图/Z-ImageBase+文生图_2016327178299904002.json, 图片生成/文生图/Z-Image_BASE工作流_2066527774562668546.json, 图片生成/文生图/Z-Image_BASE造像完整版文生图_2019239958594199554.json, 图片生成/文生图/Z-Image_BASE造像模型完整版开源工作流_2049377951891853314.json, 图片生成/文生图/Z-Image基础文生图工作流_2016022338512359425.json, 图片生成/文生图/Z-Imgae一键生成大胸美女_2028683377297072130.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2041531285021134849.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2041694117238939649.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042149150724198401.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042149662869692418.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042468324331757569.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042827110661758977.json, 图片生成/文生图/Z-image 文生图_2027351141612265474.json, 图片生成/文生图/Z-image-base+lora文生图工作流_2016716307059707905.json, 图片生成/文生图/Z-image-base+lora文生图工作流_2058729767695904769.json, 图片生成/文生图/Z-image-base加速lora文生图_2017613550671372290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo高质量文生图_2021205123837468673.json、图片生成/文生图/Z-ImageBase+4步加速+文生图_2021786374671704065.json、图片生成/文生图/Z-ImageBase+8步加速+文生图_2021754201637916674.json、图片生成/文生图/Z-ImageBase+文生图_2016327178299904002.json、图片生成/文生图/Z-Image_BASE工作流_2066527774562668546.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 18/19 个有
- `LoraLoaderModelOnly` —— 7/19 个有
- `Text` —— 4/19 个有
- `CFGZeroStar` —— 1/19 个有
- `CompressImages` —— 1/19 个有
- `EasyCache` —— 1/19 个有
- `JWInteger` —— 1/19 个有
- `Seed Generator` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 4 - 50 | 19 | 43% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 19 | 51% |
| 采样算法 | res_multistep | - | 19 | 53% |
| 调度器 | simple | - | 19 | 79% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 28，观测区间 4 - 50，19 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，19 个样本
- 采样算法 最常用 res_multistep，19 个样本，一致性 53%
- 调度器 最常用 simple，19 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
