---
name: unknown_workflow_video_lora_sampler_517
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.9795
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1950032039593558017.json, 视频生成/图生视频/1950814134864642049.json, 视频生成/图生视频/1955685244381773826.json, 视频生成/图生视频/1967246222643826690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_517

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1950032039593558017.json、视频生成/图生视频/1950814134864642049.json、视频生成/图生视频/1955685244381773826.json、视频生成/图生视频/1967246222643826690.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 3/4 个有
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `easy int` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 50% |
| Prompt 约束强度(CFG) | 7 | 4 - 14 | 4 | 53% |
| 采样算法 | 1 | 1 - 5.4 | 4 | 9% |
| 调度器 | lcm | - | 4 | 50% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 14，4 个样本
- 采样算法 中位数 1，观测区间 1 - 5.4，4 个样本，取值分散，一致性仅 9%
- 调度器 最常用 lcm，4 个样本，一致性 50%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
