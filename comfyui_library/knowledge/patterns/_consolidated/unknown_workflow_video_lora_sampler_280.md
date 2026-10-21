---
name: unknown_workflow_video_lora_sampler_280
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.877625
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, BerniniS2VConditioning, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, INTConstant, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RIFEInterpolation, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2075881409121701889.json, 视频生成/图生视频/2076477889901580289.json, 视频生成/图生视频/2076518219430584321.json, 视频生成/图生视频/2076904015870390274.json, 视频生成/图生视频/2076468920160186370.json, 视频生成/图生视频/2079545449362575361.json, 视频生成/文生视频/数字人声音克隆生视频 Bernini + TTS_2076918978248790017.json, 视频生成/文生视频/🎬 【开源版 Seedance 2.0】Bernini 原生音画同步直出_2075962978561781762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_280

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2075881409121701889.json、视频生成/图生视频/2076477889901580289.json、视频生成/图生视频/2076518219430584321.json、视频生成/图生视频/2076904015870390274.json、视频生成/图生视频/2076468920160186370.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `BerniniS2VConditioning`
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
- `TrimAudioDuration` —— 7/8 个有
- `AudioConcat` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `Text` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `IndexTTS2Run` —— 3/8 个有
- `PreviewAudio` —— 3/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `BerniniS2VConditioningV2` —— 1/8 个有
- `FlashVSRNode` —— 1/8 个有
- `Float` —— 1/8 个有
- `RunningHub Deepcleaner` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `Sleep` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | dpmpp_2m_sde | - | 8 | 100% |
| 重绘幅度 | sgm_uniform | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，8 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，8 个样本，一致性 100%
