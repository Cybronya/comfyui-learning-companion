---
name: unknown_workflow_video_lora_sampler_604
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.95125
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/角色Lora训练素材生成_1963220175883571201.json, 视频生成/图生视频/（自用）Wan2.2高质量图生视频工作流81帧50秒_1952579457632669698.json, 视频生成/图生视频/（（自用）官方版）Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1952589946924273666.json, 视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_604

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/角色Lora训练素材生成_1963220175883571201.json、视频生成/图生视频/（自用）Wan2.2高质量图生视频工作流81帧50秒_1952579457632669698.json、视频生成/图生视频/（（自用）官方版）Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1952589946924273666.json、视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LoadLatent` —— 2/4 个有
- `Seed Generator` —— 2/4 个有
- `ImageResize+` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `SaveLatent` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 50% |
| Prompt 约束强度(CFG) | 10 | 6 - 12 | 4 | 73% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 10，观测区间 6 - 12，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
