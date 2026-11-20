---
name: unknown_workflow_video_lora_sampler_613
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8466
common_nodes: [BerniniStudio, CLIPLoader, GetNode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan Bernini Studio 加速版工作流_2073577575993139202.json, 视频生成/图生视频/免费图生视频 贝尔尼尼Bernini Studio工作流_2074795916221050881.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流_2074035799124955138.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流自动反推_2064238678511280130.json, 视频生成/文生视频/贝尔尼尼加速多合一工作流_2074071622453121025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_613

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan Bernini Studio 加速版工作流_2073577575993139202.json、视频生成/图生视频/免费图生视频 贝尔尼尼Bernini Studio工作流_2074795916221050881.json、视频生成/图生视频/贝尔尼尼Bernini Studio工作流_2074035799124955138.json、视频生成/图生视频/贝尔尼尼Bernini Studio工作流自动反推_2064238678511280130.json、视频生成/文生视频/贝尔尼尼加速多合一工作流_2074071622453121025.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BerniniStudio`
- `CLIPLoader`
- `GetNode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 4/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `Int` —— 2/5 个有
- `RTXVideoSuperResolution` —— 2/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/5 个有
- `GIMMVFI_interpolate` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 5 | 69% |
| 采样算法 | 1 | 1 - 1.5 | 5 | 82% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1.5，5 个样本，取值集中（一致性 82%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
