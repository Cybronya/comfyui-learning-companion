---
name: unknown_workflow_video_sampler_clip_58
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.880111
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageLoader, ImageResize+, KSamplerAdvanced, ModelSamplingSD3, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1988486488964947969.json, 视频生成/图生视频/1986094815710511106.json, 视频生成/图生视频/1988479150342193154.json, 视频生成/图生视频/2057468310819786754.json, 视频生成/图生视频/wan2.2图生视频_2100280347178135554.json, 视频生成/图生视频/wan2.2图生视频_2101483714801913858.json, 视频生成/图生视频/wan2.2图生视频_2102213428411715585.json, 视频生成/图生视频/1986819504288296962.json, 视频生成/图生视频/2021849082557370369.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1988486488964947969.json、视频生成/图生视频/1986094815710511106.json、视频生成/图生视频/1988479150342193154.json、视频生成/图生视频/2057468310819786754.json、视频生成/图生视频/wan2.2图生视频_2100280347178135554.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageLoader`
- `ImageResize+`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `RIFEInterpolation` —— 5/9 个有
- `GetNode` —— 4/9 个有
- `Int` —— 4/9 个有
- `Qwen3_VQA` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `CR Text Concatenate` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `MultiplePathsInput` —— 2/9 个有
- `RIFE VFI` —— 2/9 个有
- `Text Multiline (Code Compatible)` —— 2/9 个有
- `IntToText` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `ttN concat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 56% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
