---
name: unknown_workflow_video_sampler_clip_10
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.994893
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/remix V3.0首-中-尾多帧生视频-无提示词工程_2039336981896892418.json, 视频生成/图生视频/全网最新首尾多帧视频_2008211461260189698.json, 视频生成/图生视频/首尾多帧视频 超流畅生视频_2008199309795266561.json, 视频生成/图生视频/首尾帧  wan2.2 wan22  图生视频   视频生成_2077269465192034306.json, 视频生成/图生视频/首尾帧  wan2.2 wan22  图生视频   视频生成_2077636142706552833.json, 视频生成/图生视频/首尾帧  wan2.2 wan22  图生视频   视频生成_2077677260378828801.json, 视频生成/图生视频/首尾帧  wan2.2 wan22  图生视频   视频生成_2078823475380318209.json, 视频生成/图生视频/首尾帧  wan2.2 图生视频   视频生成_2079016267759050753.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2071625785936539650.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2072403909544603649.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2074567411587702786.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2074915494896955394.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2075491112214679554.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2075510355111006210.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2075613549606563841.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2075960869892214786.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2076181570117005314.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2077642993561071617.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083124131020759041.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083420511694053378.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2070580986932449281.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2047152839029428226.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2047174431381921794.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2047224792201302017.json, 视频生成/图生视频/首尾帧 wan2.2  图生视频 视频生成 wan22_2074392701696565250.json, 视频生成/图生视频/首尾帧 wan2.2  图生视频_2075378321805897730.json, 视频生成/图生视频/首尾帧 wan2.2  图生视频_2077654737146695682.json, 视频生成/图生视频/首尾帧 预估54RH_2077306195379056642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/remix V3.0首-中-尾多帧生视频-无提示词工程_2039336981896892418.json、视频生成/图生视频/全网最新首尾多帧视频_2008211461260189698.json、视频生成/图生视频/首尾多帧视频 超流畅生视频_2008199309795266561.json、视频生成/图生视频/首尾帧  wan2.2 wan22  图生视频   视频生成_2077269465192034306.json、视频生成/图生视频/首尾帧  wan2.2 wan22  图生视频   视频生成_2077636142706552833.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 27/28 个有
- `SimpleMath+` —— 27/28 个有
- `LoraLoaderModelOnly` —— 25/28 个有
- `ModelPatchTorchSettings` —— 25/28 个有
- `PreviewAny` —— 2/28 个有
- `YC Color Match` —— 2/28 个有
- `CLIPVisionEncode` —— 1/28 个有
- `CLIPVisionLoader` —— 1/28 个有
- `LatentFromBatch` —— 1/28 个有
- `PreviewImage` —— 1/28 个有
- `PrimitiveStringMultiline` —— 1/28 个有
- `Seed (rgthree)` —— 1/28 个有
- `VHS_SelectFilename` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 28 | 96% |
| Prompt 约束强度(CFG) | 6 | 6 - 12 | 28 | 82% |
| 采样算法 | 1 | 1 - 1 | 28 | 100% |
| 调度器 | euler | - | 28 | 100% |
| 重绘幅度 | beta | - | 28 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，28 个样本，一致性 96%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 12，28 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，28 个样本，一致性 100%
- 重绘幅度 最常用 beta，28 个样本，一致性 82%
