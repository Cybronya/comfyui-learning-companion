---
name: unknown_workflow_video_lora_sampler_628
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.493
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, SetNode, Switch, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/YJ-FAST-wan2.2-分镜视频-grand-tmp2-step2_2038262525682257922.json, 图片生成/图生图/YJ-FAST-wan2.2-分镜视频-jianan2-tmp2-step2_2039371091650547714.json, 数字人/数字人/YJ-APP-Wan2.2_I2V_图生视频_2029925798953619457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_628

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/YJ-FAST-wan2.2-分镜视频-grand-tmp2-step2_2038262525682257922.json、图片生成/图生图/YJ-FAST-wan2.2-分镜视频-jianan2-tmp2-step2_2039371091650547714.json、数字人/数字人/YJ-APP-Wan2.2_I2V_图生视频_2029925798953619457.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `SetNode`
- `Switch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `Float` —— 1/3 个有
- `Int` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `Text` —— 1/3 个有
- `WanImageToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
