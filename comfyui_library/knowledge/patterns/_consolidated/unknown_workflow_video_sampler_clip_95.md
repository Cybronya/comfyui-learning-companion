---
name: unknown_workflow_video_sampler_clip_95
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.95
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 smoothmix v2 文生视频+ 补帧_2064601257079296001.json, 视频生成/文生视频/Wan2.2 文生视频工作流_1991800430478962690.json, 视频生成/文生视频/Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882.json, 视频生成/文生视频/Wan2.2Remix高质量文生视频_1988716572640423937.json, 视频生成/文生视频/Wan2.2文生视频_2002368127193235457.json, 视频生成/文生视频/惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338.json, "视频生成/文生视频/纯净万相 Wan2.2-Remix-Comfy-T2V-文生视频 不带lora,带插帧丝滑_2042646743598243841.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 smoothmix v2 文生视频+ 补帧_2064601257079296001.json、视频生成/文生视频/Wan2.2 文生视频工作流_1991800430478962690.json、视频生成/文生视频/Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882.json、视频生成/文生视频/Wan2.2Remix高质量文生视频_1988716572640423937.json、视频生成/文生视频/Wan2.2文生视频_2002368127193235457.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 5/7 个有
- `RIFE VFI` —— 2/7 个有
- `Int` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `easy int` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 71% |
| Prompt 约束强度(CFG) | 12 | 6 - 30 | 7 | 49% |
| 采样算法 | 1 | 1 - 3.5 | 7 | 36% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 12，观测区间 6 - 30，7 个样本，取值分散，一致性仅 49%
- 采样算法 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
