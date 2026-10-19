---
name: unknown_workflow_video_lora_sampler_36
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.892565
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, BerniniS2VConditioning, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RIFEInterpolation, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2078320387280162818.json, 视频生成/图生视频/2081275038845726722.json, 视频生成/图生视频/2079327737751359489.json, 视频生成/图生视频/2077628506321805314.json, 视频生成/图生视频/2077569166571294722.json, 视频生成/图生视频/2079048469997772802.json, 视频生成/图生视频/2079366355974975489.json, 视频生成/图生视频/bernini人物自然动态 开口说话_2082333319848615938.json, 视频生成/图生视频/2081361413834108929.json, 视频生成/图生视频/2077701219740639233.json, 视频生成/图生视频/2077741026973937666.json, 视频生成/图生视频/bernini数字人开口说话视频图生视频_2088247090945286146.json, 视频生成/图生视频/2082400679599108097.json, 视频生成/图生视频/2082406303087022082.json, 视频生成/图生视频/2077570082494050305.json, 视频生成/图生视频/2081346958836461570.json, 视频生成/图生视频/2081307306670776321.json, 视频生成/图生视频/2080089032889036801.json, 视频生成/图生视频/2078383851998629890.json, 视频生成/图生视频/2079478844951715841.json, 视频生成/图生视频/2079504635626352642.json, 视频生成/图生视频/2079510043048890369.json, 视频生成/图生视频/（1图 1音频）WAN2.2  Bernini人物开口说话视频_2111395780270575618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/2078320387280162818.json、视频生成/图生视频/2081275038845726722.json、视频生成/图生视频/2079327737751359489.json、视频生成/图生视频/2077628506321805314.json、视频生成/图生视频/2077569166571294722.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 23 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `BerniniS2VConditioning`
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
- `Float` —— 22/23 个有
- `Int` —— 22/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 22/23 个有
- `Text` —— 22/23 个有
- `RHHiddenNodes` —— 15/23 个有
- `PreviewAny` —— 12/23 个有
- `PreviewImage` —— 9/23 个有
- `RH_Captioner` —— 7/23 个有
- `TextConcatenate_UTK` —— 7/23 个有
- `easy showAnything` —— 7/23 个有
- `GoogleTranslateTextNode` —— 4/23 个有
- `Float to Int` —— 3/23 个有
- `ImageFromBatch` —— 3/23 个有
- `RH_Translator` —— 3/23 个有
- `easy mathFloat` —— 3/23 个有
- `easy mathInt` —— 3/23 个有
- `INTConstant` —— 1/23 个有
- `PreviewAudio` —— 1/23 个有
- `SaveImage` —— 1/23 个有

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
