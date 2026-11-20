---
name: unknown_workflow_video_lora_sampler_60
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.886826
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RIFEInterpolation, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/数字人视频+BerniniS2V+Index图生视频_2084101037882957826.json, 平台全量/bernini人物开口说话视频_2118515857029681154.json, 数字人/数字人/Bernini S2V高动态数字人V1_2076481694571524098.json, 视频生成/图生视频/Bernini S2V高动态数字人V2_2075633285170032642.json, 视频生成/图生视频/Bernini V2_音视频_2075860093270323201.json, 视频生成/图生视频/BerniniS2v+IndexTTS_2075534910647005186.json, 视频生成/图生视频/BerniniS2v+IndexTTS数字人_2076643931248488450.json, 视频生成/图生视频/Bernini音频驱动+单双图角色参考_2077033010171568129.json, 视频生成/图生视频/Bernini音频驱动+角色参考数字人_2075515497583570946.json, 视频生成/图生视频/Bernini音频驱动+角色参考数字人（视频生成）_2076480633026727938.json, 视频生成/图生视频/bernini丰富表情动作数字人_2081275038845726722.json, 视频生成/图生视频/bernini人物对口型_2079327737751359489.json, 视频生成/图生视频/bernini人物开口说话_2077628506321805314.json, 视频生成/图生视频/bernini人物开口说话视频_2077569166571294722.json, 视频生成/图生视频/bernini人物开口说话视频_2079048469997772802.json, 视频生成/图生视频/bernini人物开口说话视频_2079366355974975489.json, 视频生成/图生视频/bernini数字人开口说话视频图生视频_2077701219740639233.json, 视频生成/图生视频/bernini数字人开口说话视频图生视频_2077741026973937666.json, 视频生成/图生视频/bernini数字人开口说话视频图生视频_2088247090945286146.json, 视频生成/图生视频/bernini角色开口唱歌_2077570082494050305.json, 视频生成/图生视频/人物开口说话视频-bernini_2080089032889036801.json, 视频生成/图生视频/数字人视频 BerniniS2V+IndexTTS_2076518219430584321.json, 视频生成/图生视频/（1图 1音频）WAN2.2  Bernini人物开口说话视频_2111395780270575618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/数字人视频+BerniniS2V+Index图生视频_2084101037882957826.json、平台全量/bernini人物开口说话视频_2118515857029681154.json、数字人/数字人/Bernini S2V高动态数字人V1_2076481694571524098.json、视频生成/图生视频/Bernini S2V高动态数字人V2_2075633285170032642.json、视频生成/图生视频/Bernini V2_音视频_2075860093270323201.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 23 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RIFEInterpolation`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BerniniS2VConditioning` —— 22/23 个有
- `Float` —— 15/23 个有
- `Int` —— 13/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/23 个有
- `RHHiddenNodes` —— 13/23 个有
- `Text` —— 13/23 个有
- `PreviewAny` —— 12/23 个有
- `Fast Groups Bypasser (rgthree)` —— 10/23 个有
- `INTConstant` —— 10/23 个有
- `AudioConcat` —— 6/23 个有
- `PreviewAudio` —— 5/23 个有
- `IndexTTS2Run` —— 4/23 个有
- `RunningHub Deepcleaner` —— 4/23 个有
- `easy cleanGpuUsed` —— 4/23 个有
- `BerniniS2VConditioningV2` —— 1/23 个有
- `Label (rgthree)` —— 1/23 个有
- `PreviewImage` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 23 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 23 | 100% |
| 采样算法 | 1 | 1 - 1 | 23 | 100% |
| 调度器 | dpmpp_2m_sde | - | 23 | 100% |
| 重绘幅度 | sgm_uniform | - | 23 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，23 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，23 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，23 个样本，一致性 100%
