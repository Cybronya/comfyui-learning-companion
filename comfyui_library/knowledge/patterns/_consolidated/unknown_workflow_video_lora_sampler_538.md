---
name: unknown_workflow_video_lora_sampler_538
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.885167
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, BerniniS2VConditioning, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, INTConstant, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RIFEInterpolation, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/参考声音和图片生成视频BerniniS2v_2075881409121701889.json, 视频生成/图生视频/声音生视频 数字人 Bernini S2V_2076477889901580289.json, 视频生成/图生视频/语音克隆生视频 S2v Bernini+IndexTTS_2076904015870390274.json, 视频生成/图生视频/音频生视频+角色参考数字人 Bernini_2076468920160186370.json, 视频生成/文生视频/数字人声音克隆生视频 Bernini + TTS_2076918978248790017.json, 视频生成/文生视频/🎬 【开源版 Seedance 2.0】Bernini 原生音画同步直出_2075962978561781762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_538

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/参考声音和图片生成视频BerniniS2v_2075881409121701889.json、视频生成/图生视频/声音生视频 数字人 Bernini S2V_2076477889901580289.json、视频生成/图生视频/语音克隆生视频 S2v Bernini+IndexTTS_2076904015870390274.json、视频生成/图生视频/音频生视频+角色参考数字人 Bernini_2076468920160186370.json、视频生成/文生视频/数字人声音克隆生视频 Bernini + TTS_2076918978248790017.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
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
- `AudioConcat` —— 5/6 个有
- `TrimAudioDuration` —— 5/6 个有
- `Text` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `IndexTTS2Run` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `BerniniS2VConditioningV2` —— 1/6 个有
- `FlashVSRNode` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `Sleep` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | dpmpp_2m_sde | - | 6 | 100% |
| 重绘幅度 | sgm_uniform | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，6 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，6 个样本，一致性 100%
