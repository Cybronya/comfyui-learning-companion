---
name: unknown_workflow_video_lora_sampler_633
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5506
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/宠物吃播_SVI_2_Pro长视频_2018178886772727809.json, 视频生成/图生视频/顶峰--SVI+2.0Pro一镜到底！_2065196684543619074.json, 视频生成/图生视频/🐳SVI2.0PRO长视频生成 图生视频 KJ优化无限对接版 25-12-29🦋_2005505528635817986.json, 视频生成/图生视频/🦖(高动态版)SVI 2.0 图生长视频_2006221064216514562.json, 视频生成/图生视频/🦖SVI 2.0 Pro 图生长视频_2005914209638645762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_633

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/宠物吃播_SVI_2_Pro长视频_2018178886772727809.json、视频生成/图生视频/顶峰--SVI+2.0Pro一镜到底！_2065196684543619074.json、视频生成/图生视频/🐳SVI2.0PRO长视频生成 图生视频 KJ优化无限对接版 25-12-29🦋_2005505528635817986.json、视频生成/图生视频/🦖(高动态版)SVI 2.0 图生长视频_2006221064216514562.json、视频生成/图生视频/🦖SVI 2.0 Pro 图生长视频_2005914209638645762.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ImpactInt` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有
- `UNETLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 8 - 14 | 5 | 74% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 14，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
