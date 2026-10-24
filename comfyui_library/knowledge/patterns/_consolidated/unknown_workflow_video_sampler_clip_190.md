---
name: unknown_workflow_video_sampler_clip_190
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.971
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2八图首尾帧20秒分镜视频_1952310686854656002.json, 视频生成/图生视频/Wan2.2四图首尾帧10秒分镜视频_1952290446611525634.json, 视频生成/图生视频/Wan2.2首尾帧视频生成_1952049916556292097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_190

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2八图首尾帧20秒分镜视频_1952310686854656002.json、视频生成/图生视频/Wan2.2四图首尾帧10秒分镜视频_1952290446611525634.json、视频生成/图生视频/Wan2.2首尾帧视频生成_1952049916556292097.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 2/3 个有
- `GIMMVFI_interpolate` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageBatchMultiple+` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `SaveImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 3 | 100% |
| 采样算法 | 4 | 4 - 4 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
