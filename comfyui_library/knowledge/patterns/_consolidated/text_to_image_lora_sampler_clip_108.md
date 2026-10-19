---
name: text_to_image_lora_sampler_clip_108
type: Text To Image
frequency: 9
level: strong
coverage: 0.900444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/视频修复增强｜去噪清晰化画质提升，老片翻新必备_2101226303985901570.json, 视频生成/文生视频/Mini多模态视频生成｜Seedance2.0文生视频生视频_2095871844741111809.json, 视频生成/文生视频/RH Upscale视频极速高清放大工作流PR插件适配，视频超分高清增强工具_2107260285441634305.json, 视频生成/文生视频/RH Upscale视频极速高清放大工作流，PR插件适配视频超分工具_2106535133057740802.json, 视频生成/文生视频/RuningHub企业版Seedance2.0｜图生视频视频生视频一键生成_2094303698901102593.json, 视频生成/文生视频/RuningHub企业版不降智｜Seedance2.0图生视频秒出大片_2090829853393244162.json, 视频生成/文生视频/Seedance 2.0 Global Fast多模态全能参考视频｜4K文图视频参考_2097977539267489794.json, 视频生成/文生视频/Seedance 2.0 Global Mini多模态全能参考视频｜4K文图视频参考全支持_2097900436190752770.json, 视频生成/文生视频/Seedance2.0 Mini多模态｜文生图生视频全都能跑_2106629854375534594.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_108

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/视频修复增强｜去噪清晰化画质提升，老片翻新必备_2101226303985901570.json、视频生成/文生视频/Mini多模态视频生成｜Seedance2.0文生视频生视频_2095871844741111809.json、视频生成/文生视频/RH Upscale视频极速高清放大工作流PR插件适配，视频超分高清增强工具_2107260285441634305.json、视频生成/文生视频/RH Upscale视频极速高清放大工作流，PR插件适配视频超分工具_2106535133057740802.json、视频生成/文生视频/RuningHub企业版Seedance2.0｜图生视频视频生视频一键生成_2094303698901102593.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `LoadVideo` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `LoadAudio` —— 2/9 个有
- `MuyeTextEditOutput` —— 2/9 个有
- `RH_RhartVideoSparkvideo20FastImageToVideo` —— 2/9 个有
- `RH_RhartVideoSparkvideo20MiniMultimodalVideo` —— 2/9 个有
- `RH_Upscale` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_BytedanceSeedance20GlobalFastMultimodalVideo` —— 1/9 个有
- `RH_BytedanceSeedance20GlobalMiniMultimodalVideo` —— 1/9 个有
- `RH_TopazLabs_VideoUpscale` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
