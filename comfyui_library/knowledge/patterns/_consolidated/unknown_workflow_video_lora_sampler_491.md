---
name: unknown_workflow_video_lora_sampler_491
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.804833
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, INTConstant, KSampler, LoadAudio, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSoundImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Wan2.2-S2V动作+表情+对口型视频生视频_2043880488292589569.json, 平台全量/Wan2.2-S2V对口型-文本+音频+控制视频生视频_1961064952733876225.json, 平台全量/Wan2.2-S2V对口型-视频到视频动态参考_1961064943288303618.json, 数字人/数字人/04-06-01-WAN2.2-数字人-S2V-原生_1991727262569541633.json, 数字人/数字人/S2V数字人（ComfyUI官方版全功能）楚门的AI世界_1961358409335508993.json, 数字人/数字人/【gen全能视频Si】s2v数字人（comfyui官方版全功能）_1967813991944826882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_491

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Wan2.2-S2V动作+表情+对口型视频生视频_2043880488292589569.json、平台全量/Wan2.2-S2V对口型-文本+音频+控制视频生视频_1961064952733876225.json、平台全量/Wan2.2-S2V对口型-视频到视频动态参考_1961064943288303618.json、数字人/数字人/04-06-01-WAN2.2-数字人-S2V-原生_1991727262569541633.json、数字人/数字人/S2V数字人（ComfyUI官方版全功能）楚门的AI世界_1961358409335508993.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 5/6 个有
- `AudioCrop` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `TorchCompileModel` —— 3/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ContextWindowsManual` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageFromBatch+` —— 1/6 个有
- `JWIntegerToString` —— 1/6 个有
- `PreViewVideo` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 20 | 6 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 6 | 12% |
| 采样算法 | uni_pc | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 20，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，6 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 uni_pc，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
