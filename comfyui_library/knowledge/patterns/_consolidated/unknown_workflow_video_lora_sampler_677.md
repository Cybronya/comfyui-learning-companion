---
name: unknown_workflow_video_lora_sampler_677
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/最新WAN2.2-14B图生视频_1949839253868077058.json, 视频生成/文生视频/Wan2.2_14B_图生视频 (稳定加速版) 丨提示词生成视频_1968987843408379906.json, 视频生成/文生视频/炸裂更新！阿里万相WAN2.2图重心视频 质量飙升！_1950004459780923393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_677

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/最新WAN2.2-14B图生视频_1949839253868077058.json、视频生成/文生视频/Wan2.2_14B_图生视频 (稳定加速版) 丨提示词生成视频_1968987843408379906.json、视频生成/文生视频/炸裂更新！阿里万相WAN2.2图重心视频 质量飙升！_1950004459780923393.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Int` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 3 | 86% |
| 采样算法 | 1 | 1 - 3.5 | 3 | 36% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
