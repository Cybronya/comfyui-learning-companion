---
name: unknown_workflow_video_lora_sampler_318
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.864
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, BerniniS2VConditioning, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, Float, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RH_Captioner, RIFEInterpolation, SoundFlow_GetLength, Text, TextConcatenate_UTK, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/bernini人物自然动态 开口说话_2082333319848615938.json, 视频生成/图生视频/bernini自然动态人物开口说话2_2082400679599108097.json, 视频生成/图生视频/bernini自然动态人物开口说话3_2082406303087022082.json, 视频生成/图生视频/最新视频人物开口唱歌_2078383851998629890.json, 视频生成/图生视频/跨境电商数字人开口说话V4_2079478844951715841.json, 视频生成/图生视频/跨境电商数字人开口说话V5_2079504635626352642.json, 视频生成/图生视频/跨境电商数字人开口说话V6_2079510043048890369.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_318

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/bernini人物自然动态 开口说话_2082333319848615938.json、视频生成/图生视频/bernini自然动态人物开口说话2_2082400679599108097.json、视频生成/图生视频/bernini自然动态人物开口说话3_2082406303087022082.json、视频生成/图生视频/最新视频人物开口唱歌_2078383851998629890.json、视频生成/图生视频/跨境电商数字人开口说话V4_2079478844951715841.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `RH_Captioner`
- `RIFEInterpolation`
- `SoundFlow_GetLength`
- `Text`
- `TextConcatenate_UTK`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/7 个有
- `GoogleTranslateTextNode` —— 4/7 个有
- `Float to Int` —— 3/7 个有
- `ImageFromBatch` —— 3/7 个有
- `RH_Translator` —— 3/7 个有
- `easy mathFloat` —— 3/7 个有
- `easy mathInt` —— 3/7 个有
- `PreviewAny` —— 1/7 个有
- `SaveImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | dpmpp_2m_sde | - | 7 | 100% |
| 重绘幅度 | sgm_uniform | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，7 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，7 个样本，一致性 100%
