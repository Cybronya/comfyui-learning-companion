---
name: unknown_workflow_video_lora_sampler_81
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.873111
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, INTConstant, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RIFEInterpolation, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/数字人视频+BerniniS2V+Index图生视频_2084101037882957826.json, 数字人/数字人/Bernini S2V高动态数字人V1_2076481694571524098.json, 视频生成/图生视频/Bernini S2V高动态数字人V2_2075633285170032642.json, 视频生成/图生视频/Bernini V2_音视频_2075860093270323201.json, 视频生成/图生视频/BerniniS2v+IndexTTS_2075534910647005186.json, 视频生成/图生视频/BerniniS2v+IndexTTS数字人_2076643931248488450.json, 视频生成/图生视频/Bernini音频驱动+单双图角色参考_2077033010171568129.json, 视频生成/图生视频/Bernini音频驱动+角色参考数字人_2075515497583570946.json, 视频生成/图生视频/Bernini音频驱动+角色参考数字人（视频生成）_2076480633026727938.json, 视频生成/图生视频/Bernini音频驱动数字人_2078320387280162818.json, 视频生成/图生视频/参考声音和图片生成视频BerniniS2v_2075881409121701889.json, 视频生成/图生视频/声音生视频 数字人 Bernini S2V_2076477889901580289.json, 视频生成/图生视频/数字人视频 BerniniS2V+IndexTTS_2076518219430584321.json, 视频生成/图生视频/语音克隆生视频 S2v Bernini+IndexTTS_2076904015870390274.json, 视频生成/图生视频/音频生视频+角色参考数字人 Bernini_2076468920160186370.json, 视频生成/图生视频/高动态图生视频_2079545449362575361.json, 视频生成/文生视频/数字人声音克隆生视频 Bernini + TTS_2076918978248790017.json, 视频生成/文生视频/🎬 【开源版 Seedance 2.0】Bernini 原生音画同步直出_2075962978561781762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/数字人视频+BerniniS2V+Index图生视频_2084101037882957826.json、数字人/数字人/Bernini S2V高动态数字人V1_2076481694571524098.json、视频生成/图生视频/Bernini S2V高动态数字人V2_2075633285170032642.json、视频生成/图生视频/Bernini V2_音视频_2075860093270323201.json、视频生成/图生视频/BerniniS2v+IndexTTS_2075534910647005186.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 18 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RIFEInterpolation`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BerniniS2VConditioning` —— 17/18 个有
- `TrimAudioDuration` —— 17/18 个有
- `Fast Groups Bypasser (rgthree)` —— 14/18 个有
- `AudioConcat` —— 12/18 个有
- `easy cleanGpuUsed` —— 7/18 个有
- `IndexTTS2Run` —— 6/18 个有
- `PreviewAudio` —— 6/18 个有
- `RunningHub Deepcleaner` —— 4/18 个有
- `Text` —— 4/18 个有
- `Float` —— 3/18 个有
- `BerniniS2VConditioningV2` —— 2/18 个有
- `PrimitiveFloat` —— 2/18 个有
- `FlashVSRNode` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有
- `SaveImage` —— 1/18 个有
- `Sleep` —— 1/18 个有
- `easy clearCacheAll` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 18 | 89% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 18 | 100% |
| 采样算法 | 1 | 1 - 1 | 18 | 100% |
| 调度器 | dpmpp_2m_sde | - | 18 | 100% |
| 重绘幅度 | sgm_uniform | - | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，18 个样本，一致性 89%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，18 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，18 个样本，一致性 100%
