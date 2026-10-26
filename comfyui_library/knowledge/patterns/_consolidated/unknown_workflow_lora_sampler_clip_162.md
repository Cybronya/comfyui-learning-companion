---
name: unknown_workflow_lora_sampler_clip_162
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.99
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2文生图_1951193822992773122.json, 图片生成/文生图/Wan2.2文生图常规版V1_1950531381078249473.json, 图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json, 图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_162

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Wan2.2文生图_1951193822992773122.json、图片生成/文生图/Wan2.2文生图常规版V1_1950531381078249473.json、图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json、图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `JWInteger` —— 1/4 个有
- `PMRF` —— 1/4 个有
- `SaveAnimatedWEBP` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 12 | 12 - 20 | 4 | 75% |
| 采样算法 | 1 | 1 - 3.5 | 4 | 33% |
| 调度器 | res_2s | - | 4 | 50% |
| 重绘幅度 | bong_tangent | - | 4 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 20，4 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 调度器 最常用 res_2s，4 个样本，一致性 50%
- 重绘幅度 最常用 bong_tangent，4 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
