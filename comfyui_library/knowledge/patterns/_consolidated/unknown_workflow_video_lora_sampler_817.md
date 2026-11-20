---
name: unknown_workflow_video_lora_sampler_817
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.908
common_nodes: [BerniniStudio, CLIPLoader, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/bernini运镜复刻工作流_2082065792786587649.json, 视频生成/图生视频/bernini全能工作流_2081973710835240961.json, 视频生成/文生视频/贝尔尼尼-R视频编辑流_2062053839146147841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_817

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/bernini运镜复刻工作流_2082065792786587649.json、视频生成/图生视频/bernini全能工作流_2081973710835240961.json、视频生成/文生视频/贝尔尼尼-R视频编辑流_2062053839146147841.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Int` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `TTResolutionSelector` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `DepthAnything_V2` —— 1/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1.5 | 1 - 1.5 | 3 | 82% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1.5，观测区间 1 - 1.5，3 个样本，取值集中（一致性 82%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
