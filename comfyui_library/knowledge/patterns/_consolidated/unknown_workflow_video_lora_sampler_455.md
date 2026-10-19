---
name: unknown_workflow_video_lora_sampler_455
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9132
common_nodes: [BerniniStudio, CLIPLoader, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2064238678511280130.json, 视频生成/图生视频/2074037576872316929.json, 视频生成/文生视频/全能视频编辑-贝尔尼尼Bernini 4步加速_2075480007203446785.json, 视频生成/文生视频/贝尔尼尼-R视频编辑流_2062053839146147841.json, 视频生成/文生视频/贝尔尼尼加速多合一工作流_2074071622453121025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_455

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2064238678511280130.json、视频生成/图生视频/2074037576872316929.json、视频生成/文生视频/全能视频编辑-贝尔尼尼Bernini 4步加速_2075480007203446785.json、视频生成/文生视频/贝尔尼尼-R视频编辑流_2062053839146147841.json、视频生成/文生视频/贝尔尼尼加速多合一工作流_2074071622453121025.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
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
- `GetNode` —— 2/5 个有
- `RTXVideoSuperResolution` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 5 | 67% |
| 采样算法 | 1 | 1 - 1.5 | 5 | 82% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1.5，5 个样本，取值集中（一致性 82%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
