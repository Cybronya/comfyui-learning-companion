---
name: unknown_workflow_video_sampler_unet_52
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.912429
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyHunyuanLatentVideo, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, PromptRelayEncodeTimeline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-Prompt Relay-单图参考精准控制-电商带货_2064248756870139905.json, 视频生成/图生视频/Wan2.2-PromptRelay-单图参考精准控制_2057114333976555522.json, 视频生成/图生视频/Wan2.2_PromptRelay_2053855379406245890.json, 视频生成/图生视频/Wan2.2_PromptRelay_2058829735278497793.json, 视频生成/图生视频/Wan2.2_PromptRelay动作控制_2054887639500763138.json, 视频生成/图生视频/Wan2.2_PromptRelay图生视频（分镜提示词精准控制）_2059203324586577922.json, 视频生成/图生视频/重大进步2_Wan2.2_PromptRelay多段提示词精准控制_2054717028392546306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_52

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-Prompt Relay-单图参考精准控制-电商带货_2064248756870139905.json、视频生成/图生视频/Wan2.2-PromptRelay-单图参考精准控制_2057114333976555522.json、视频生成/图生视频/Wan2.2_PromptRelay_2053855379406245890.json、视频生成/图生视频/Wan2.2_PromptRelay_2058829735278497793.json、视频生成/图生视频/Wan2.2_PromptRelay动作控制_2054887639500763138.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyHunyuanLatentVideo`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PromptRelayEncodeTimeline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `FlashVSRInitPipe` —— 1/7 个有
- `FlashVSRNodeAdv` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 7 | 91% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | uni_pc | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，7 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
