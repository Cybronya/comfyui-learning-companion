---
name: unknown_workflow_video_lora_sampler_878
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9305
common_nodes: [BerniniStudio, CLIPLoader, FlashVSRNode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SaveImage, Sleep, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/全能参考生成视频Bernini Studio工作流_2064122259987591170.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流_2073635862683934721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_878

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/全能参考生成视频Bernini Studio工作流_2064122259987591170.json、视频生成/图生视频/贝尔尼尼Bernini Studio工作流_2073635862683934721.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BerniniStudio`
- `CLIPLoader`
- `FlashVSRNode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SaveImage`
- `Sleep`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
