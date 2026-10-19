---
name: unknown_workflow_video_lora_sampler_257
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.87
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2075633285170032642.json, 视频生成/图生视频/2075860093270323201.json, 视频生成/图生视频/2076950547332161538.json, 视频生成/图生视频/2075534910647005186.json, 视频生成/图生视频/2076643931248488450.json, 视频生成/图生视频/2077033010171568129.json, 视频生成/图生视频/2075515497583570946.json, 视频生成/图生视频/2076480633026727938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_257

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2075633285170032642.json、视频生成/图生视频/2075860093270323201.json、视频生成/图生视频/2076950547332161538.json、视频生成/图生视频/2075534910647005186.json、视频生成/图生视频/2076643931248488450.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
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
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BerniniS2VConditioning` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `RIFEInterpolation` —— 7/8 个有
- `AudioConcat` —— 5/8 个有
- `Float` —— 2/8 个有
- `IndexTTS2Run` —— 2/8 个有
- `PreviewAudio` —— 2/8 个有
- `RunningHub Deepcleaner` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `BerniniS2VConditioningV2` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `ImpactFloat` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有
- `easy int` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | dpmpp_2m_sde | - | 8 | 100% |
| 重绘幅度 | sgm_uniform | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，8 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，8 个样本，一致性 100%
