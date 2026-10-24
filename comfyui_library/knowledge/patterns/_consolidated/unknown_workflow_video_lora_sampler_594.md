---
name: unknown_workflow_video_lora_sampler_594
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.939
common_nodes: [BerniniStudio, CLIPLoader, DapaoSmartMemoryOptimizerNode, ImageSharpen, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, RIFE VFI, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy int, 孤海注释]
problems: []
missing: []
members: [视频生成/图生视频/Bernini 4步急速LORA视频编辑_2076959623524995074.json, 视频生成/图生视频/Bernini 4步急速LORA视频编辑_2083599403918643201.json, 视频生成/图生视频/Bernini 图生视频_4步极速LORA视频编辑_2078379268756828161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_594

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Bernini 4步急速LORA视频编辑_2076959623524995074.json、视频生成/图生视频/Bernini 4步急速LORA视频编辑_2083599403918643201.json、视频生成/图生视频/Bernini 图生视频_4步极速LORA视频编辑_2078379268756828161.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `BerniniStudio`
- `CLIPLoader`
- `DapaoSmartMemoryOptimizerNode`
- `ImageSharpen`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RIFE VFI`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy int`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | uni_pc | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
