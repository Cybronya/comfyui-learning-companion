---
name: unknown_workflow_video_lora_sampler_453
type: Unknown Workflow
frequency: 5
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1949839253868077058.json, 视频生成/图生视频/2023300078865223682.json, 视频生成/文生视频/1968987843408379906.json, 视频生成/文生视频/1952999225413070849.json, 视频生成/文生视频/1950004459780923393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_453

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1949839253868077058.json、视频生成/图生视频/2023300078865223682.json、视频生成/文生视频/1968987843408379906.json、视频生成/文生视频/1952999225413070849.json、视频生成/文生视频/1950004459780923393.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 4 - 14 | 5 | 55% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 35% |
| 调度器 | euler | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 14，5 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 35%
- 调度器 最常用 euler，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
