---
name: unknown_workflow_video_lora_sampler_575
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8355
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, Fast Bypasser (rgthree), GetNode, ImpactInt, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 图生视频(MOE官方流)｜Light2v 加速版_2104706846383759362.json, 视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流  动态增强V2版_1988440123446616065.json, 视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流-视频放大- 动态增强V2版_1989332274598563842.json, 视频生成/图生视频/【wan2.2 图生视频】light2v蒸馏加速主模型 MOE官方流_1978326367861366785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_575

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 图生视频(MOE官方流)｜Light2v 加速版_2104706846383759362.json、视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流  动态增强V2版_1988440123446616065.json、视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流-视频放大- 动态增强V2版_1989332274598563842.json、视频生成/图生视频/【wan2.2 图生视频】light2v蒸馏加速主模型 MOE官方流_1978326367861366785.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `Fast Bypasser (rgthree)`
- `GetNode`
- `ImpactInt`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 3/4 个有
- `WanImageToVideo` —— 3/4 个有
- `PainterI2V` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `CR Upscale Image` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | dpmpp_2m_sde | - | 4 | 100% |
| 重绘幅度 | beta | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，4 个样本，一致性 100%
- 重绘幅度 最常用 beta，4 个样本，一致性 100%
