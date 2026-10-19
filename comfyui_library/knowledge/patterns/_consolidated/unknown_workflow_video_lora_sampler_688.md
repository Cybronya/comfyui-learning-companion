---
name: unknown_workflow_video_lora_sampler_688
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.984333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ImpactInt, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1963220175883571201.json, 视频生成/图生视频/1950018274672164866.json, 视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_688

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1963220175883571201.json、视频生成/图生视频/1950018274672164866.json、视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `Seed Generator` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `ImageResize+` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
