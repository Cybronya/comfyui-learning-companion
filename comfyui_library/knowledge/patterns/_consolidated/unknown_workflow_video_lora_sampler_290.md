---
name: unknown_workflow_video_lora_sampler_290
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8797
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, BerniniS2VConditioning, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, Float, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RIFEInterpolation, SoundFlow_GetLength, Text, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/bernini人物自然动态 开口说话_2082333319848615938.json, 视频生成/图生视频/bernini人物行走中开口说话_2081361413834108929.json, 视频生成/图生视频/bernini自然动态人物开口说话2_2082400679599108097.json, 视频生成/图生视频/bernini自然动态人物开口说话3_2082406303087022082.json, 视频生成/图生视频/bernini高清动态数字人_2081346958836461570.json, 视频生成/图生视频/bernini高清画质人物开口说话_2081307306670776321.json, 视频生成/图生视频/最新视频人物开口唱歌_2078383851998629890.json, 视频生成/图生视频/跨境电商数字人开口说话V4_2079478844951715841.json, 视频生成/图生视频/跨境电商数字人开口说话V5_2079504635626352642.json, 视频生成/图生视频/跨境电商数字人开口说话V6_2079510043048890369.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_290

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/bernini人物自然动态 开口说话_2082333319848615938.json、视频生成/图生视频/bernini人物行走中开口说话_2081361413834108929.json、视频生成/图生视频/bernini自然动态人物开口说话2_2082400679599108097.json、视频生成/图生视频/bernini自然动态人物开口说话3_2082406303087022082.json、视频生成/图生视频/bernini高清动态数字人_2081346958836461570.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `BerniniS2VConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `Float`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RIFEInterpolation`
- `SoundFlow_GetLength`
- `Text`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 8/10 个有
- `RH_Captioner` —— 7/10 个有
- `TextConcatenate_UTK` —— 7/10 个有
- `easy showAnything` —— 7/10 个有
- `GoogleTranslateTextNode` —— 4/10 个有
- `Float to Int` —— 3/10 个有
- `ImageFromBatch` —— 3/10 个有
- `RHHiddenNodes` —— 3/10 个有
- `RH_Translator` —— 3/10 个有
- `easy mathFloat` —— 3/10 个有
- `easy mathInt` —— 3/10 个有
- `PreviewAny` —— 1/10 个有
- `SaveImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | dpmpp_2m_sde | - | 10 | 100% |
| 重绘幅度 | sgm_uniform | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，10 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，10 个样本，一致性 100%
