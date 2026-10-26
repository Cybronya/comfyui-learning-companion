---
name: unknown_workflow_video_sampler_clip_191
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.918333
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2+Smooth+Mix高质量图生视频_1980210462413459458.json, 视频生成/图生视频/背摔视频特效wan2.2_1981669095458381825.json, 视频生成/图生视频/通义万相wan2.2图生视频（lightx2v加速6步）_1949968677410136066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_191

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/WAN2.2+Smooth+Mix高质量图生视频_1980210462413459458.json、视频生成/图生视频/背摔视频特效wan2.2_1981669095458381825.json、视频生成/图生视频/通义万相wan2.2图生视频（lightx2v加速6步）_1949968677410136066.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 6 - 10 | 3 | 80% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 10，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
