---
name: unknown_workflow_video_lora_sampler_760
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.94025
common_nodes: [BerniniStudio, CLIPLoader, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/全能参考生成视频Bernini Studio工作流_2064122259987591170.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流_2073635862683934721.json, 视频生成/图生视频/贝尔尼尼工作流 Bernini+Studio 12种模式_2074037576872316929.json, 视频生成/文生视频/全能视频编辑-贝尔尼尼Bernini 4步加速_2075480007203446785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_760

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/全能参考生成视频Bernini Studio工作流_2064122259987591170.json、视频生成/图生视频/贝尔尼尼Bernini Studio工作流_2073635862683934721.json、视频生成/图生视频/贝尔尼尼工作流 Bernini+Studio 12种模式_2074037576872316929.json、视频生成/文生视频/全能视频编辑-贝尔尼尼Bernini 4步加速_2075480007203446785.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BerniniStudio`
- `CLIPLoader`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `Sleep` —— 2/4 个有
- `CR Prompt List` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 50% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
