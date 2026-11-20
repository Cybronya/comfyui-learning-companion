---
name: unknown_workflow_video_lora_sampler_102
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.9035
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, BerniniS2VConditioning, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, Float, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Bernini 人物+场景+音频合成_2076950547332161538.json, 视频生成/图生视频/bernini丰富表情动作数字人_2081275038845726722.json, 视频生成/图生视频/bernini人物对口型_2079327737751359489.json, 视频生成/图生视频/bernini人物开口说话_2077628506321805314.json, 视频生成/图生视频/bernini人物开口说话视频_2077569166571294722.json, 视频生成/图生视频/bernini人物开口说话视频_2079048469997772802.json, 视频生成/图生视频/bernini人物开口说话视频_2079366355974975489.json, 视频生成/图生视频/bernini人物行走中开口说话_2081361413834108929.json, 视频生成/图生视频/bernini数字人开口说话视频图生视频_2077701219740639233.json, 视频生成/图生视频/bernini数字人开口说话视频图生视频_2077741026973937666.json, 视频生成/图生视频/bernini数字人开口说话视频图生视频_2088247090945286146.json, 视频生成/图生视频/bernini角色开口唱歌_2077570082494050305.json, 视频生成/图生视频/bernini高清动态数字人_2081346958836461570.json, 视频生成/图生视频/bernini高清画质人物开口说话_2081307306670776321.json, 视频生成/图生视频/人物开口说话视频-bernini_2080089032889036801.json, 视频生成/图生视频/（1图 1音频）WAN2.2  Bernini人物开口说话视频_2111395780270575618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_102

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/Bernini 人物+场景+音频合成_2076950547332161538.json、视频生成/图生视频/bernini丰富表情动作数字人_2081275038845726722.json、视频生成/图生视频/bernini人物对口型_2079327737751359489.json、视频生成/图生视频/bernini人物开口说话_2077628506321805314.json、视频生成/图生视频/bernini人物开口说话视频_2077569166571294722.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `BerniniS2VConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `Float`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 15/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/16 个有
- `RHHiddenNodes` —— 15/16 个有
- `RIFEInterpolation` —— 15/16 个有
- `Text` —— 15/16 个有
- `PreviewAny` —— 11/16 个有
- `PreviewImage` —— 4/16 个有
- `CR Text` —— 1/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `ImpactFloat` —— 1/16 个有
- `Note Plus (mtb)` —— 1/16 个有
- `PreviewAudio` —— 1/16 个有
- `RIFE VFI` —— 1/16 个有
- `easy int` —— 1/16 个有
- `孤海注释` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 16 | 94% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 16 | 100% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | dpmpp_2m_sde | - | 16 | 100% |
| 重绘幅度 | sgm_uniform | - | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，16 个样本，一致性 94%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，16 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，16 个样本，一致性 100%
