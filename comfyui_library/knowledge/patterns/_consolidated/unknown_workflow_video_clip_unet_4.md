---
name: unknown_workflow_video_clip_unet_4
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.859182
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/251223001-14.WanSmoothMix首尾帧-NF_2003138334044168194.json, 视频生成/图生视频/Wan2.1 FL2fV 首尾帧_1948615618990866434.json, 视频生成/图生视频/Wan2.2 SmoothMix图生视频高动态（官方版）_1980507194548469761.json, 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_1980673656160436226.json, 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_2049663225859457025.json, 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_2050777904669306881.json, 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）（双图）_1983902184238710786.json, 视频生成/图生视频/Wan2.2-SmoothMix高动态图生视频，动态加强_1979742422047559681.json, 视频生成/图生视频/Wan2.2SmoothMix首尾帧高动态视频生成_1979871682087260162.json, 视频生成/图生视频/Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json, 音频生成/音频生成/Wan2.2图生视频动态字幕+画外音（indexTTS2）_1983724744073781249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/251223001-14.WanSmoothMix首尾帧-NF_2003138334044168194.json、视频生成/图生视频/Wan2.1 FL2fV 首尾帧_1948615618990866434.json、视频生成/图生视频/Wan2.2 SmoothMix图生视频高动态（官方版）_1980507194548469761.json、视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_1980673656160436226.json、视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_2049663225859457025.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 10/11 个有
- `KSamplerAdvanced` —— 10/11 个有
- `PrimitiveInt` —— 10/11 个有
- `SimpleMath+` —— 8/11 个有
- `CLIPVisionEncode` —— 7/11 个有
- `CLIPVisionLoader` —— 7/11 个有
- `WanFirstLastFrameToVideo` —— 7/11 个有
- `WanImageToVideo` —— 4/11 个有
- `HAIGC_VideoSubtitleEnhanced` —— 2/11 个有
- `孤海-取色器` —— 2/11 个有
- `KSampler` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `LoadImageFromUrl` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `SaveAudioMP3` —— 1/11 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/11 个有
- `easy indexTTSGenerateSimple` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 55% |
| Prompt 约束强度(CFG) | 8 | 3 - 8 | 11 | 81% |
| 采样算法 | 1 | 1 - 1.5 | 10 | 80% |
| 调度器 | uni_pc | - | 11 | 82% |
| 重绘幅度 | simple | - | 11 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 55%
- Prompt 约束强度(CFG) 中位数 8，观测区间 3 - 8，11 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1.5，10 个样本
- 调度器 最常用 uni_pc，11 个样本，一致性 82%
- 重绘幅度 最常用 simple，11 个样本，一致性 91%
