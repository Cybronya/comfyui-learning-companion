---
name: unknown_workflow_sampler_clip_unet_266
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9712
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json, 图片生成/文生图/Wan2.2文生图_1950935703578419201.json, 图片生成/文生图/Wan2.2文生图常规版V1_1950531381078249473.json, 图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json, 图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_266

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json、图片生成/文生图/Wan2.2文生图_1950935703578419201.json、图片生成/文生图/Wan2.2文生图常规版V1_1950531381078249473.json、图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json、图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `ModelSamplingSD3` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `PMRF` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 75% |
| LoRA 文本强度 | 0.8 | - | 2 | 75% |
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 12 | 8 - 14 | 5 | 83% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | res_2s | - | 5 | 60% |
| 重绘幅度 | bong_tangent | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.8，样本不足，未给区间，2 个样本
- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 12，观测区间 8 - 14，5 个样本，取值集中（一致性 83%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2s，5 个样本，一致性 60%
- 重绘幅度 最常用 bong_tangent，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
