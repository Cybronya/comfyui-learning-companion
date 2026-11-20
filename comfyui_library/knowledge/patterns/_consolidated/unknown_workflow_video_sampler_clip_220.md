---
name: unknown_workflow_video_sampler_clip_220
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.886
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyHunyuanLatentVideo, FluxGuidance, KSamplerSelect, ModelSamplingSD3, RandomNoise, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/混元FastVideo文生视频加速版_1901602052710244354.json, 视频生成/文生视频/混元VIP视频工作流_1870307237162815489.json, 视频生成/文生视频/混元视频移动增强器_1905450015412916226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_220

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/混元FastVideo文生视频加速版_1901602052710244354.json、视频生成/文生视频/混元VIP视频工作流_1870307237162815489.json、视频生成/文生视频/混元视频移动增强器_1905450015412916226.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `SamplerCustomAdvanced` —— 2/3 个有
- `ApplyFirstBlockCachePatchAdvanced` —— 1/3 个有
- `CR Upscale Image` —— 1/3 个有
- `HunyuanVideoLoraLoader` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `StringConstantMultiline` —— 1/3 个有
- `TeaCacheHunyuanVideoSampler` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | double_blocks | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
