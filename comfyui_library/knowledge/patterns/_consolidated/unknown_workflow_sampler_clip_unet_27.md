---
name: unknown_workflow_sampler_clip_unet_27
type: Unknown Workflow
frequency: 8
level: strong
coverage: 1
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1917390442533687298.json, 图片生成/文生图/1920589333093617666.json, 图片生成/文生图/1921046708803796993.json, 图片生成/文生图/1931362971040022529.json, 图片生成/文生图/1954389130199351298.json, 图片生成/文生图/1985548530460860417.json, 视频生成/图生视频/1931362971040022529.json, 视频生成/图生视频/1932632244605620225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1917390442533687298.json、图片生成/文生图/1920589333093617666.json、图片生成/文生图/1921046708803796993.json、图片生成/文生图/1931362971040022529.json、图片生成/文生图/1954389130199351298.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 5/8 个有
- `LoraLoader` —— 5/8 个有
- `ImageToMask` —— 3/8 个有
- `InpaintModelConditioning` —— 3/8 个有
- `LoadImage` —— 3/8 个有
- `DeepTranslatorTextNode` —— 2/8 个有
- `CLIPAttentionMultiply` —— 1/8 个有
- `ModelSamplingFlux` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1920 | 5 | 66% |
| 高度 | 1080 | 1024 - 1536 | 5 | 83% |
| 采样步数 | 22 | 20 - 30 | 8 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 5 | 92% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 5 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1920，5 个样本
- 高度 中位数 1080，观测区间 1024 - 1536，5 个样本，取值集中（一致性 83%）
- 采样步数 中位数 22，观测区间 20 - 30，8 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
