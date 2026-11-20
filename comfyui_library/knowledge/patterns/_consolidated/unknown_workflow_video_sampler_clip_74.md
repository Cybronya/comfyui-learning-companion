---
name: unknown_workflow_video_sampler_clip_74
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.901
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/wan2.2+2.1二阶文生视频_2057632025691115522.json, 图片生成/文生图/Comfyui教学第二期-文_图生视频_2008727256675389442.json, 数字人/数字人/MV制作流程2-空镜制作_2005153306941030401.json, 视频生成/图生视频/AA--金子雨特效lora-wan2.2 加速图生视频+独立放大插帧_2003814653497122818.json, 视频生成/图生视频/WAN2.2 图生视频女孩微笑_1950190982249799682.json, 视频生成/图生视频/WAN2.2图生视频_2025568584335892482.json, 视频生成/图生视频/图生视频_2077340089688088578.json, 视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/wan2.2+2.1二阶文生视频_2057632025691115522.json、图片生成/文生图/Comfyui教学第二期-文_图生视频_2008727256675389442.json、数字人/数字人/MV制作流程2-空镜制作_2005153306941030401.json、视频生成/图生视频/AA--金子雨特效lora-wan2.2 加速图生视频+独立放大插帧_2003814653497122818.json、视频生成/图生视频/WAN2.2 图生视频女孩微笑_1950190982249799682.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `WanImageToVideo` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `Int` —— 4/8 个有
- `EmptyHunyuanLatentVideo` —— 3/8 个有
- `ImageResize+` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `wanBlockSwap` —— 3/8 个有
- `SimpleMath+` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Float` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `RunningHub Deepcleaner` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 50% |
| Prompt 约束强度(CFG) | 8 | 4 - 14 | 8 | 61% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 40% |
| 调度器 | euler | - | 8 | 50% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 14，8 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，8 个样本，一致性 50%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
