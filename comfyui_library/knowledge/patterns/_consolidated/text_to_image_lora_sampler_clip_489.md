---
name: text_to_image_lora_sampler_clip_489
type: Text To Image
frequency: 4
level: strong
coverage: 0.91425
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadVideo, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/星光视频超分高清放大，视频生视频画质增强利器_2113470381557374978.json, 视频生成/图生视频/视频修复增强｜去噪清晰化画质提升，老片翻新必备_2101226303985901570.json, 视频生成/文生视频/RH Upscale视频极速高清放大工作流PR插件适配，视频超分高清增强工具_2107260285441634305.json, 视频生成/文生视频/RH Upscale视频极速高清放大工作流，PR插件适配视频超分工具_2106535133057740802.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_489

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/星光视频超分高清放大，视频生视频画质增强利器_2113470381557374978.json、视频生成/图生视频/视频修复增强｜去噪清晰化画质提升，老片翻新必备_2101226303985901570.json、视频生成/文生视频/RH Upscale视频极速高清放大工作流PR插件适配，视频超分高清增强工具_2107260285441634305.json、视频生成/文生视频/RH Upscale视频极速高清放大工作流，PR插件适配视频超分工具_2106535133057740802.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_Upscale` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `QZ_ResolutionPreset` —— 1/4 个有
- `RH_Astra` —— 1/4 个有
- `RH_TopazLabs_VideoUpscale` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
