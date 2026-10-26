---
name: unknown_workflow_lora_clip_unet_11
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/wan2.2 WanMoeKsampler 文生图_1955849490886479874.json, 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json, 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json, 视频生成/文生视频/wan2.2 WanMoeKsampler 文生视频_1955652862984556545.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/wan2.2 WanMoeKsampler 文生图_1955849490886479874.json、视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json、视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json、视频生成/文生视频/wan2.2 WanMoeKsampler 文生视频_1955652862984556545.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `WanMoeKSampler` —— 3/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `ModelPatchTorchSettings` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `ImpactInt` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `SaveImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 50% |
| Prompt 约束强度(CFG) | 7 | 4 - 12 | 4 | 52% |
| 采样算法 | 2 | 1 - 3 | 4 | 50% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | euler | - | 4 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 12，4 个样本
- 采样算法 中位数 2，观测区间 1 - 3，4 个样本
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，4 个样本，一致性 50%
