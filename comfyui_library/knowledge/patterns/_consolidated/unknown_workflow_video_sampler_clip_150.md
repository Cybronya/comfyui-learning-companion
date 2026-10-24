---
name: unknown_workflow_video_sampler_clip_150
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.46325
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveStringMultiline, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanMoeKSampler, easy float, easy int, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/Remix i2v v2 + qwen3_尾图_1986675501609742338.json, 视频生成/图生视频/Remix i2v v2 + qwen3_首图_1986670301834604545.json, 视频生成/图生视频/Remix i2v v2+ qwen3_首尾帧_1986675520580550658.json, 视频生成/图生视频/Remix 图生视频  v2 首帧尾帧首尾帧  手动_1986648749831290881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Remix i2v v2 + qwen3_尾图_1986675501609742338.json、视频生成/图生视频/Remix i2v v2 + qwen3_首图_1986670301834604545.json、视频生成/图生视频/Remix i2v v2+ qwen3_首尾帧_1986675520580550658.json、视频生成/图生视频/Remix 图生视频  v2 首帧尾帧首尾帧  手动_1986648749831290881.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveStringMultiline`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler`
- `easy float`
- `easy int`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 3/4 个有
- `MultiplePathsInput` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `String Replace (mtb)` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `easy convertAnything` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `easy boolean` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 1 | 1 - 1 | 4 | 100% |
| 重绘幅度 | euler | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，4 个样本，一致性 100%
