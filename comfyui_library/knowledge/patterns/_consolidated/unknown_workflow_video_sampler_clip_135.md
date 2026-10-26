---
name: unknown_workflow_video_sampler_clip_135
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6248
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/wan2.2_2013893086845341698.json, 视频生成/图生视频/wan2.2图生视频——高动态高遵循度_2055902519104163842.json, 视频生成/图生视频/【Work-FIsh】WAN2.2-RemixV2-I2V图生视频_1986333709685194753.json, 视频生成/图生视频/【gen全能视频Si】wan2.2-remixv2-i2v图生视频_1986747295184138242.json, 视频生成/图生视频/一键推图直出视频v1.0-anuo_2079816909545107457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/wan2.2_2013893086845341698.json、视频生成/图生视频/wan2.2图生视频——高动态高遵循度_2055902519104163842.json、视频生成/图生视频/【Work-FIsh】WAN2.2-RemixV2-I2V图生视频_1986333709685194753.json、视频生成/图生视频/【gen全能视频Si】wan2.2-remixv2-i2v图生视频_1986747295184138242.json、视频生成/图生视频/一键推图直出视频v1.0-anuo_2079816909545107457.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `Int` —— 4/5 个有
- `CR Text` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `KSampler` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `QwenImageLatentAspectRatio` —— 1/5 个有
- `RHLLMChatNode` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `easy promptReplace` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 5 | 82% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | normal | - | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，5 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 normal，5 个样本，一致性 100%
