---
name: image_to_image_lora_sampler_clip_121
type: Image To Image
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_Sora2_I2V, ReferenceLatent, SaveVideo, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/全能视频S视频反推洗稿分镜短视频_1988340872406286337.json, 视频生成/图生视频/全能视频S2 图生视频（破除真人限制）_1983836311914258433.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_121

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/全能视频S视频反推洗稿分镜短视频_1988340872406286337.json、视频生成/图生视频/全能视频S2 图生视频（破除真人限制）_1983836311914258433.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Sora2_I2V`
- `ReferenceLatent`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V` —— 1/2 个有
- `AILab_MiniCPM_4_V_Advanced` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `RH_Sora2_T2V` —— 1/2 个有
- `SDVN Any Show` —— 1/2 个有
- `TTP_text_mix` —— 1/2 个有
- `TextInput_` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | - | 2 | 75% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
