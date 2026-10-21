---
name: unknown_workflow_video_sampler_clip_147
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.889
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1983546218196443137.json, 视频生成/图生视频/1950004160121978881.json, 视频生成/图生视频/2029088291949121537.json, 音频生成/音频生成/Wan2.2图生视频动态字幕+画外音（indexTTS2）_1983724744073781249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1983546218196443137.json、视频生成/图生视频/1950004160121978881.json、视频生成/图生视频/2029088291949121537.json、音频生成/音频生成/Wan2.2图生视频动态字幕+画外音（indexTTS2）_1983724744073781249.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `HAIGC_VideoSubtitleEnhanced` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `孤海-取色器` —— 2/4 个有
- `FL_RIFE` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `SaveAudioMP3` —— 1/4 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/4 个有
- `easy indexTTSGenerateSimple` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 6 - 14 | 4 | 67% |
| 采样算法 | 1.25 | 1 - 1.5 | 4 | 80% |
| 调度器 | uni_pc | - | 4 | 50% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 14，4 个样本
- 采样算法 中位数 1.25，观测区间 1 - 1.5，4 个样本，取值集中（一致性 80%）
- 调度器 最常用 uni_pc，4 个样本，一致性 50%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
