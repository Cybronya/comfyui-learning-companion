---
name: unknown_workflow_video_lora_sampler_563
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.959
common_nodes: [CLIPLoader, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, EmptyHunyuanLatentVideo, GIMMVFI_interpolate, INTConstant, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, SimpleMath+, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json, 视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json, 视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json, 视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_563

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json、视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json、视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json、视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyHunyuanLatentVideo`
- `GIMMVFI_interpolate`
- `INTConstant`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SimpleMath+`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Text Concatenate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
