---
name: unknown_workflow_video_clip_unet_13
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.960875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: [easy int]
members: [视频生成/文生视频/1975738907180576770.json, 视频生成/文生视频/1977308765202587649.json, 视频生成/文生视频/1949875905322729473.json, 视频生成/文生视频/ComfyUI官方文生视频工作流_2050448250037121026.json, 视频生成/文生视频/1923566284871823361.json, 视频生成/文生视频/1954184197437059073.json, 视频生成/文生视频/1950002171104419841.json, 视频生成/文生视频/Wan2.2 smoothmix v2 文生视频+ 补帧_2064601257079296001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/1975738907180576770.json、视频生成/文生视频/1977308765202587649.json、视频生成/文生视频/1949875905322729473.json、视频生成/文生视频/ComfyUI官方文生视频工作流_2050448250037121026.json、视频生成/文生视频/1923566284871823361.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 7/8 个有
- `KSamplerAdvanced` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `KSampler` —— 2/8 个有
- `RIFE VFI` —— 2/8 个有
- `easy int` —— 2/8 个有
- `ModelPatchTorchSettings` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `TorchCompileModel` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 38% |
| Prompt 约束强度(CFG) | 6 | 5 - 14 | 8 | 57% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 34% |
| 调度器 | euler | - | 8 | 75% |
| 重绘幅度 | simple | - | 8 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 38%
- Prompt 约束强度(CFG) 中位数 6，观测区间 5 - 14，8 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 调度器 最常用 euler，8 个样本，一致性 75%
- 重绘幅度 最常用 simple，8 个样本，一致性 75%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：easy int
