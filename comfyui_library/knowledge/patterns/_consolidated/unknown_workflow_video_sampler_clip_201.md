---
name: unknown_workflow_video_sampler_clip_201
type: Unknown Workflow
frequency: 3
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/文生视频/Smooth_Mix文生图工作流native版_1979807859443666945.json, 视频生成/文生视频/1950807946525614081.json, 视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Smooth_Mix文生图工作流native版_1979807859443666945.json、视频生成/文生视频/1950807946525614081.json、视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Power Lora Loader (rgthree)` —— 1/3 个有
- `wanBlockSwap` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 12 | 6 - 20 | 3 | 55% |
| 采样算法 | 3.5 | 1 - 3.5 | 3 | 56% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 12，观测区间 6 - 20，3 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
