---
name: text_to_image_video_lora_sampler_179
type: Text To Image
frequency: 4
level: strong
coverage: 0.6135
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Float, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SigmasGraph, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频_2090451614204252162.json, 视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频一键直出_2090274287373611010.json, 视频生成/图生视频/心然寻源MiniMax H3多模态参考数字人对口型｜图生视频_2100764134798352386.json, 视频生成/图生视频/音频驱动数字人｜MiniMax H3图生视频口播直出_2090205102572400642.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_179

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频_2090451614204252162.json、视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频一键直出_2090274287373611010.json、视频生成/图生视频/心然寻源MiniMax H3多模态参考数字人对口型｜图生视频_2100764134798352386.json、视频生成/图生视频/音频驱动数字人｜MiniMax H3图生视频口播直出_2090205102572400642.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Float`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SigmasGraph`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Divide [DVB]` —— 3/4 个有
- `FlashVSRNode` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `Int` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `Text` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `ZNGB_AudioCrop` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `SoundFlow_GetLength` —— 1/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
