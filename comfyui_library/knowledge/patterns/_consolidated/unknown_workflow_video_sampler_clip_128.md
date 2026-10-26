---
name: unknown_workflow_video_sampler_clip_128
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9786
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy int, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2-RemixV2-图生视频_2012399930219962370.json, 视频生成/图生视频/WAN2.2-Remix首尾帧_2012418080877580290.json, 视频生成/图生视频/Wan2.2-RemixV2图生视频（加速放大版）_2003147433540558850.json, 视频生成/图生视频/【GUGU】WAN2.2-RemixV2-I2V图生视频加速版_1986972038416019457.json, 视频生成/图生视频/【GUGU】WAN2.2-RemixV2-I2V首尾帧视频加速版_1986986221308194817.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/WAN2.2-RemixV2-图生视频_2012399930219962370.json、视频生成/图生视频/WAN2.2-Remix首尾帧_2012418080877580290.json、视频生成/图生视频/Wan2.2-RemixV2图生视频（加速放大版）_2003147433540558850.json、视频生成/图生视频/【GUGU】WAN2.2-RemixV2-I2V图生视频加速版_1986972038416019457.json、视频生成/图生视频/【GUGU】WAN2.2-RemixV2-I2V首尾帧视频加速版_1986986221308194817.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

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
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy int`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `GetImage` —— 2/5 个有
- `Textbox` —— 2/5 个有
- `WanFirstLastFrameToVideo` —— 2/5 个有
- `FlashVSRNode` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
