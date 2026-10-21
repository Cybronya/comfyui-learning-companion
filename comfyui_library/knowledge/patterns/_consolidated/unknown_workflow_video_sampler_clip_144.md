---
name: unknown_workflow_video_sampler_clip_144
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95125
common_nodes: [CLIPLoader, CLIPTextEncode, ImageLoader, ImageResizeKJv2, KSamplerAdvanced, ModelSamplingSD3, MultiplePathsInput, PainterI2V, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2041549150814216193.json, 视频生成/图生视频/2041522312066895874.json, 视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json, 视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_144

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2041549150814216193.json、视频生成/图生视频/2041522312066895874.json、视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json、视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageLoader`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `MultiplePathsInput`
- `PainterI2V`
- `Qwen3_VQA`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 4 | 67% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 50% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 50%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
