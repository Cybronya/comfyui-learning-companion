---
name: unknown_workflow_video_lora_sampler_567
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.903
common_nodes: [CLIPLoader, CLIPTextEncode, ImageLoader, ImageResizeKJv2, Int, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, MultiplePathsInput, PathchSageAttentionKJ, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [图片生成/图生图/影视短剧导演之四_图生视频_首尾帧生视频_1989856749970706433.json, 视频生成/图生视频/Qwen  首尾帧  图生视频_2042258477560631298.json, 视频生成/图生视频/影视短剧导演之五_多帧生视频_1989856817062793218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_567

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/影视短剧导演之四_图生视频_首尾帧生视频_1989856749970706433.json、视频生成/图生视频/Qwen  首尾帧  图生视频_2042258477560631298.json、视频生成/图生视频/影视短剧导演之五_多帧生视频_1989856817062793218.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageLoader`
- `ImageResizeKJv2`
- `Int`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `MultiplePathsInput`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `WanFirstLastFrameToVideo` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ColorMatch` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `workflow>getPath` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | normal | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 normal，3 个样本，一致性 67%
