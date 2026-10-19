---
name: unknown_workflow_video_clip_unet_5
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.987833
common_nodes: [CLIPLoader, CLIPTextEncode, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/1902941440509382658.json, 图片生成/文生图/1930295791557185537.json, 图片生成/文生图/1951273402428502018.json, 视频生成/图生视频/1951274276659867650.json, 视频生成/图生视频/1987307533339701250.json, 视频生成/图生视频/1951277844100009986.json, 视频生成/图生视频/1952539360614920193.json, 视频生成/文生视频/1930295791557185537.json, 视频生成/文生视频/1950378020252073986.json, 视频生成/文生视频/ComfyUI官方图生视频工作流搭建_2050410359365881858.json, 视频生成/文生视频/Remix_i2v_v2.1工作流_2050521770255495170.json, 视频生成/文生视频/Wan2.2官网14B图生视频&文生视频&5B文or图生视频_2072999658865336320.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1902941440509382658.json、图片生成/文生图/1930295791557185537.json、图片生成/文生图/1951273402428502018.json、视频生成/图生视频/1951274276659867650.json、视频生成/图生视频/1987307533339701250.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 10/12 个有
- `LoadImage` —— 8/12 个有
- `EmptyHunyuanLatentVideo` —— 7/12 个有
- `Wan22ImageToVideoLatent` —— 7/12 个有
- `KSamplerAdvanced` —— 4/12 个有
- `WanImageToVideo` —— 4/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `SaveAnimatedWEBP` —— 2/12 个有
- `SaveImage` —— 1/12 个有
- `TeaCache` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 10 | 86% |
| Prompt 约束强度(CFG) | 5 | 5 - 6 | 12 | 91% |
| 采样算法 | uni_pc | - | 12 | 83% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，10 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 6，12 个样本，取值集中（一致性 91%）
- 采样算法 最常用 uni_pc，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
