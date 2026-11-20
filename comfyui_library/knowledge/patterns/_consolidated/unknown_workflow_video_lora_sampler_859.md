---
name: unknown_workflow_video_lora_sampler_859
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.872667
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, BerniniS2VConditioning, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Bernini 人物+场景+音频合成_2076950547332161538.json, 视频生成/图生视频/Bernini音频驱动数字人_2078320387280162818.json, 视频生成/图生视频/高动态图生视频_2079545449362575361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_859

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Bernini 人物+场景+音频合成_2076950547332161538.json、视频生成/图生视频/Bernini音频驱动数字人_2078320387280162818.json、视频生成/图生视频/高动态图生视频_2079545449362575361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
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
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `RIFEInterpolation` —— 2/3 个有
- `AudioConcat` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ImpactFloat` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `easy int` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | dpmpp_2m_sde | - | 3 | 100% |
| 重绘幅度 | sgm_uniform | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，3 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，3 个样本，一致性 100%
