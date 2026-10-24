---
name: unknown_workflow_video_sampler_clip_111
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.962
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, LoadAudio, ModelSamplingSD3, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanSoundImageToVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/S2V官流双采样文生视频_2039896508253868033.json, 视频生成/图生视频/S2V官流双采样文生视频 (1)_2065232096980987906.json, 视频生成/文生视频/S2V官流双采样文生视频_1960817006654238721.json, 视频生成/文生视频/S2V官流双采样文生视频_2039961005249273857.json, 视频生成/文生视频/Wan2.2_S2V文生“对口型”视频-双采样器工作流_1967886202416300034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/S2V官流双采样文生视频_2039896508253868033.json、视频生成/图生视频/S2V官流双采样文生视频 (1)_2065232096980987906.json、视频生成/文生视频/S2V官流双采样文生视频_1960817006654238721.json、视频生成/文生视频/S2V官流双采样文生视频_2039961005249273857.json、视频生成/文生视频/Wan2.2_S2V文生“对口型”视频-双采样器工作流_1967886202416300034.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadAudio`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideoV2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 5 | 100% |
| 采样算法 | 6 | 6 - 6 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
