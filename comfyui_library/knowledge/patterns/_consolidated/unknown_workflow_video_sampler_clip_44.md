---
name: unknown_workflow_video_sampler_clip_44
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.950727
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/wan2.2+2.1二阶文生视频_2057632025691115522.json, 图片生成/文生图/Comfyui教学第二期-文_图生视频_2008727256675389442.json, 数字人/数字人/MV制作流程2-空镜制作_2005153306941030401.json, 视频生成/图生视频/WAN2.2 图生视频 4步出图_2016945597965672449.json, 视频生成/图生视频/WAN2.2 图生视频-首帧参考版_2027809490925527041.json, 视频生成/图生视频/WAN2.2 图生视频女孩微笑_1950190982249799682.json, 视频生成/图生视频/Wan2.2  图生视频_2018573357712674817.json, 视频生成/图生视频/Wan2.2 14B 6步超极速图生视频_1949992607571206146.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996104036933910529.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1950344638181892097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/wan2.2+2.1二阶文生视频_2057632025691115522.json、图片生成/文生图/Comfyui教学第二期-文_图生视频_2008727256675389442.json、数字人/数字人/MV制作流程2-空镜制作_2005153306941030401.json、视频生成/图生视频/WAN2.2 图生视频 4步出图_2016945597965672449.json、视频生成/图生视频/WAN2.2 图生视频-首帧参考版_2027809490925527041.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `WanImageToVideo` —— 10/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `PathchSageAttentionKJ` —— 6/11 个有
- `LayerUtility: PurgeVRAM` —— 5/11 个有
- `JWInteger` —— 4/11 个有
- `EmptyHunyuanLatentVideo` —— 3/11 个有
- `Int` —— 3/11 个有
- `MathExpression|pysssss` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `Float` —— 1/11 个有
- `LoadImagesFromURL` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `Primitive integer [Crystools]` —— 1/11 个有
- `RunningHub Deepcleaner` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 55% |
| Prompt 约束强度(CFG) | 6 | 4 - 14 | 11 | 55% |
| 采样算法 | 1 | 1 - 3.5 | 11 | 37% |
| 调度器 | euler | - | 11 | 55% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 55%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 14，11 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，11 个样本，取值分散，一致性仅 37%
- 调度器 最常用 euler，11 个样本，一致性 55%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
