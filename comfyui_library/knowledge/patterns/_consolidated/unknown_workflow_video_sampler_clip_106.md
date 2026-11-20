---
name: unknown_workflow_video_sampler_clip_106
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.958
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/图生表情包_2035645245035126785.json, 视频生成/图生视频/Wan2.2 Remix图生视频_2041549150814216193.json, 视频生成/图生视频/Wan2.2 Smooth 图生视频_2041522312066895874.json, 视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json, 视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json, 视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/图生表情包_2035645245035126785.json、视频生成/图生视频/Wan2.2 Remix图生视频_2041549150814216193.json、视频生成/图生视频/Wan2.2 Smooth 图生视频_2041522312066895874.json、视频生成/文生视频/native图生视频wan2.2-Reward-Pusa-1022lightx2v-Painter_1988874017887096833.json、视频生成/文生视频/native超大动态图生视频wan2.2-Reward-Pusa-lightx2v-Painter_1988866929752420354.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 5/6 个有
- `MultiplePathsInput` —— 5/6 个有
- `PainterI2V` —— 5/6 个有
- `Qwen3_VQA` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `CLIPVisionEncode` —— 4/6 个有
- `CLIPVisionLoader` —— 4/6 个有
- `JWInteger` —— 4/6 个有
- `Seed (rgthree)` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `ImageResize+` —— 3/6 个有
- `Text Concatenate` —— 3/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `Any To Any` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `VHS_SelectFilename` —— 1/6 个有
- `WanImageToVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 67% |
| Prompt 约束强度(CFG) | 8 | 4 - 8 | 6 | 72% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler_ancestral | - | 6 | 67% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 8，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 67%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
