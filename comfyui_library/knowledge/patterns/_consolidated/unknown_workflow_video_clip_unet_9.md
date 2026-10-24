---
name: unknown_workflow_video_clip_unet_9
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.952
common_nodes: [CLIPLoader, CLIPTextEncode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 视频生成 图生视频_文生视频工作流_1950807946525614081.json, 视频生成/文生视频/Wan2.2+MoeKSampler+lightx2v加速_1955923712228950018.json, 视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json, 视频生成/文生视频/wan2.2工作流_2034980882162917377.json, 视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json, 视频生成/文生视频/wan文生视频_2009970396799442946.json, 视频生成/文生视频/【优化版】最强图生视频万相wan2.2_1952999225413070849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 视频生成 图生视频_文生视频工作流_1950807946525614081.json、视频生成/文生视频/Wan2.2+MoeKSampler+lightx2v加速_1955923712228950018.json、视频生成/文生视频/Wan2.2-T2V-A14B-4steps-250928-dyno-NativeComfy_1974515256741507074.json、视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json、视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `ModelSamplingSD3` —— 8/9 个有
- `EmptyHunyuanLatentVideo` —— 6/9 个有
- `LoadImage` —— 4/9 个有
- `WanImageToVideo` —— 4/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `RIFE VFI` —— 2/9 个有
- `WanMoeKSampler` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 44% |
| Prompt 约束强度(CFG) | 12 | 4 - 20 | 9 | 53% |
| 采样算法 | 1 | 1 - 4 | 9 | 40% |
| 调度器 | euler | - | 9 | 89% |
| 重绘幅度 | simple | - | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 44%
- Prompt 约束强度(CFG) 中位数 12，观测区间 4 - 20，9 个样本
- 采样算法 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，9 个样本，一致性 89%
- 重绘幅度 最常用 simple，9 个样本，一致性 89%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
