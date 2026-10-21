---
name: unknown_workflow_video_lora_sampler_542
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9065
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ResizeLongestToNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2013186178811432961.json, 视频生成/图生视频/2073390461141733378.json, 视频生成/图生视频/1989608453410836481.json, 视频生成/图生视频/1950004149220982785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_542

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2013186178811432961.json、视频生成/图生视频/2073390461141733378.json、视频生成/图生视频/1989608453410836481.json、视频生成/图生视频/1950004149220982785.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ResizeLongestToNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `MuyeTextEditOutput` —— 3/4 个有
- `RunningHub Deepcleaner` —— 3/4 个有
- `ACE_ImageGetSize` —— 2/4 个有
- `ImageGetSize` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `RH_Translator` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 4 | 65% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
