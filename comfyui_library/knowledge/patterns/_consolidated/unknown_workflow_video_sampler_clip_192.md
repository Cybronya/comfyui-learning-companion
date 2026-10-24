---
name: unknown_workflow_video_sampler_clip_192
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.743333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json, 视频生成/图生视频/🐳wan2.2 图生视频 加速出图版🦋【官方模型】_1950018274672164866.json, 视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_192

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json、视频生成/图生视频/🐳wan2.2 图生视频 加速出图版🦋【官方模型】_1950018274672164866.json、视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `HAIGC_VideoSubtitleEnhanced` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `Int` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `wanBlockSwap` —— 1/3 个有
- `孤海-取色器` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 8 - 12 | 3 | 80% |
| 采样算法 | 1 | 1 - 1.5 | 3 | 80% |
| 调度器 | uni_pc | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 12，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1.5，3 个样本
- 调度器 最常用 uni_pc，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
