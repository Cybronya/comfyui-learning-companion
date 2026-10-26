---
name: unknown_workflow_video_sampler_clip_216
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.852333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyHunyuanLatentVideo, ImageFromBatch+, KSamplerAdvanced, ModelSamplingSD3, PrimitiveInt, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386.json, 视频生成/文生视频/Wan2.2 SmoothMixV2文生视频高动态（官方版）_1980635563638345729.json, 视频生成/文生视频/Wan2.2smoothmix高动态文生视频V2_1979890524125564929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_216

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Qwen3 VL视频反推+Wan2.2 SmoothMix文生视频 无需输入提示词_1981207594238992386.json、视频生成/文生视频/Wan2.2 SmoothMixV2文生视频高动态（官方版）_1980635563638345729.json、视频生成/文生视频/Wan2.2smoothmix高动态文生视频V2_1979890524125564929.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyHunyuanLatentVideo`
- `ImageFromBatch+`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `String` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1.1 | 3 | 95% |
| 调度器 | uni_pc | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.1，3 个样本，取值集中（一致性 95%）
- 调度器 最常用 uni_pc，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
