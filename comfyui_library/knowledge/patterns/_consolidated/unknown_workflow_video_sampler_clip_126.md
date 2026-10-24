---
name: unknown_workflow_video_sampler_clip_126
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9496
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, ModelSamplingSD3, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Remix图生视频_2041549150814216193.json, 视频生成/图生视频/Wan2.2 Smooth 图生视频_2041522312066895874.json, 视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json, 视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json, 视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Remix图生视频_2041549150814216193.json、视频生成/图生视频/Wan2.2 Smooth 图生视频_2041522312066895874.json、视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json、视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json、视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `Qwen3_VQA`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 4/5 个有
- `MultiplePathsInput` —— 4/5 个有
- `PainterI2V` —— 4/5 个有
- `CLIPVisionEncode` —— 3/5 个有
- `CLIPVisionLoader` —— 3/5 个有
- `CR Prompt Text` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `Seed (rgthree)` —— 3/5 个有
- `Text Concatenate` —— 3/5 个有
- `ImageResize+` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `Any To Any` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `VHS_SelectFilename` —— 1/5 个有
- `WanImageToVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 4 - 8 | 5 | 69% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 8，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
