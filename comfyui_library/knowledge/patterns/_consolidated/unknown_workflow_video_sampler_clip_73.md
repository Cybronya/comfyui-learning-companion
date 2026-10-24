---
name: unknown_workflow_video_sampler_clip_73
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.48925
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/WAN2.2-LightX2V-I2V超强动态（邪修）_2002515455887720450.json, 图片生成/图生图/WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346.json, 图片生成/图生图/WAN2.2-RemixV2-I2V_2002500408180371457.json, 图片生成/图生图/WAN2.2-RemixV2-I2V首尾帧_2002505189661786113.json, 图片生成/图生图/Work-Fisher-自动产品多角度+图生_首尾帧_1984625142850535426.json, 图片生成/图生图/Work-Fisher-自动产品多角度+图生_首尾帧_1985014629644603394.json, 视频生成/图生视频/Supermate 推荐=Work-FIsh-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1981353708422348802.json, 视频生成/文生视频/1022Alan测-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980811965771763713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/WAN2.2-LightX2V-I2V超强动态（邪修）_2002515455887720450.json、图片生成/图生图/WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346.json、图片生成/图生图/WAN2.2-RemixV2-I2V_2002500408180371457.json、图片生成/图生图/WAN2.2-RemixV2-I2V首尾帧_2002505189661786113.json、图片生成/图生图/Work-Fisher-自动产品多角度+图生_首尾帧_1984625142850535426.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `WanImageToVideo` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `ImageLoader` —— 3/8 个有
- `WanFirstLastFrameToVideo` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `KSampler` —— 2/8 个有
- `ProcessString` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/8 个有
- `easy promptLine` —— 2/8 个有
- `easy showAnything` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 62% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | normal | - | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 normal，8 个样本，一致性 100%
