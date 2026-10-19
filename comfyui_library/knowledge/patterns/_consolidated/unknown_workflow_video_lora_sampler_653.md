---
name: unknown_workflow_video_lora_sampler_653
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2030591840105275393.json, 视频生成/文生视频/1967648604473233410.json, 视频生成/文生视频/Wan 2.2-Fun-VACE-文生视频_2072999543329038336.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_653

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2030591840105275393.json、视频生成/文生视频/1967648604473233410.json、视频生成/文生视频/Wan 2.2-Fun-VACE-文生视频_2072999543329038336.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `TrimVideoLatent` —— 2/3 个有
- `WanVaceToVideo` —— 2/3 个有
- `ImageLoader` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `WanFunInpaintToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 12 | 3 | 65% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | sa_solver_pece | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 12，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver_pece，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
