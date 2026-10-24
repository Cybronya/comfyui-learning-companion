---
name: unknown_workflow_lora_clip_unet_11
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9612
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/wan2.2 WanMoeKsampler 文生图_1955849490886479874.json, 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json, 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json, 视频生成/文生视频/wan2.2 WanMoeKsampler 文生视频_1955652862984556545.json, 视频生成/文生视频/（（自用）官方版）Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1952591181077254146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/wan2.2 WanMoeKsampler 文生图_1955849490886479874.json、视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json、视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json、视频生成/文生视频/wan2.2 WanMoeKsampler 文生视频_1955652862984556545.json、视频生成/文生视频/（（自用）官方版）Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1952591181077254146.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `ModelSamplingSD3` —— 3/5 个有
- `WanMoeKSampler` —— 3/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `ModelPatchTorchSettings` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `ImpactInt` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `LoadLatent` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 4 - 12 | 5 | 58% |
| 采样算法 | 1 | 1 - 3 | 5 | 46% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | euler | - | 5 | 40% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 12，5 个样本
- 采样算法 中位数 1，观测区间 1 - 3，5 个样本，取值分散，一致性仅 46%
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，5 个样本，一致性 40%
