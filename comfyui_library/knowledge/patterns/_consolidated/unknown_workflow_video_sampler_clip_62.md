---
name: unknown_workflow_video_sampler_clip_62
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.934889
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/wan2.2+2.1二阶文生视频_2057632025691115522.json, 图片生成/文生图/Comfyui教学第二期-文_图生视频_2008727256675389442.json, 图片生成/文生图/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1978391537375662082.json, 视频生成/图生视频/90秒81帧6步超极速图生视频_1995392959409479682.json, 视频生成/图生视频/AA--金子雨特效lora-wan2.2 加速图生视频+独立放大插帧_2003814653497122818.json, 视频生成/图生视频/WAN2.2 图生视频女孩微笑_1950190982249799682.json, 视频生成/图生视频/WAN2.2图生视频_2025568584335892482.json, 视频生成/图生视频/Wan2.2  图生视频_2018573357712674817.json, 视频生成/图生视频/图生视频_2077340089688088578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/wan2.2+2.1二阶文生视频_2057632025691115522.json、图片生成/文生图/Comfyui教学第二期-文_图生视频_2008727256675389442.json、图片生成/文生图/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1978391537375662082.json、视频生成/图生视频/90秒81帧6步超极速图生视频_1995392959409479682.json、视频生成/图生视频/AA--金子雨特效lora-wan2.2 加速图生视频+独立放大插帧_2003814653497122818.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `WanImageToVideo` —— 7/9 个有
- `LayerUtility: PurgeVRAM` —— 5/9 个有
- `EmptyHunyuanLatentVideo` —— 4/9 个有
- `Int` —— 3/9 个有
- `JWInteger` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `ImageResize+` —— 2/9 个有
- `wanBlockSwap` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `RunningHub Deepcleaner` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 44% |
| Prompt 约束强度(CFG) | 8 | 4 - 14 | 9 | 65% |
| 采样算法 | 1 | 1 - 3.5 | 9 | 33% |
| 调度器 | euler | - | 9 | 33% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 44%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 14，9 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，9 个样本，一致性 33%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
