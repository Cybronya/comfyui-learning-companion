---
name: unknown_workflow_video_clip_unet_16
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85475
common_nodes: [CLIPLoader, CLIPTextEncode, ImpactInt, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [视频生成/文生视频/AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889.json, 视频生成/文生视频/Holo长视频生成 官方流 文生视频_1983758575547949058.json, 视频生成/文生视频/Holo长视频生成 官方流 文生视频_2045400394263699457.json, 视频生成/文生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889.json、视频生成/文生视频/Holo长视频生成 官方流 文生视频_1983758575547949058.json、视频生成/文生视频/Holo长视频生成 官方流 文生视频_2045400394263699457.json、视频生成/文生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 文生视频🚵_1979382260715655170.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImpactInt`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `WanMoeKSampler` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `EmptyHunyuanLatentVideo` —— 2/4 个有
- `ModelPatchTorchSettings` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ImageScaleBy` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 10 | 6 - 12 | 4 | 73% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | euler | - | 4 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 10，观测区间 6 - 12，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，4 个样本，一致性 50%
