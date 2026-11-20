---
name: unknown_workflow_lora_sampler_clip_205
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.75925
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, ImageScale, KSamplerAdvanced, Label (rgthree), LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo]
problems: []
missing: []
members: [平台全量/video_wan2_2_数字人工作流2-放大_2010712247605141506.json, 平台全量/video_wan2_2_数字人工作流2-放大_R18_2025214150053470209.json, 平台全量/video_wan2_2_数字人工作流2-放大_plus_2017411866632392705.json, 数字人/数字人/video_wan2_2_数字人工作流2-放大_1953387295271473154.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_205

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/video_wan2_2_数字人工作流2-放大_2010712247605141506.json、平台全量/video_wan2_2_数字人工作流2-放大_R18_2025214150053470209.json、平台全量/video_wan2_2_数字人工作流2-放大_plus_2017411866632392705.json、数字人/数字人/video_wan2_2_数字人工作流2-放大_1953387295271473154.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `ImageScale`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 3/4 个有
- `Int` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `VHS_VideoCombine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
