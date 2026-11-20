---
name: unknown_workflow_video_lora_clip_10
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.916
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, Text, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 直播生成抖音花瓣消失特效_1958440936764293122.json, 视频生成/图生视频/wan2.2图生视频 自动反推视频提示词_1950176781056786433.json, 视频生成/图生视频/最强首尾帧生成视频 Wan 2.2_1952355883244302337.json, 视频生成/图生视频/电商首尾帧生成视频 保持产品一致性 自动配音  Wan 2.2_2040437839665569793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.2 直播生成抖音花瓣消失特效_1958440936764293122.json、视频生成/图生视频/wan2.2图生视频 自动反推视频提示词_1950176781056786433.json、视频生成/图生视频/最强首尾帧生成视频 Wan 2.2_1952355883244302337.json、视频生成/图生视频/电商首尾帧生成视频 保持产品一致性 自动配音  Wan 2.2_2040437839665569793.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `ShowText` —— 2/4 个有
- `TextCombinerSix` —— 2/4 个有
- `Wan22PromptSelector` —— 2/4 个有
- `WanFirstLastFrameToVideo` —— 2/4 个有
- `HunyuanVideoFoley` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `TrimVideoLatent` —— 1/4 个有
- `WanMoeKSampler` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 75%
