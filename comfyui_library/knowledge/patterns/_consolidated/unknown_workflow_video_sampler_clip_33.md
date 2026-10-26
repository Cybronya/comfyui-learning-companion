---
name: unknown_workflow_video_sampler_clip_33
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.991857
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/万相图生视频_1953415257853186050.json, 图片生成/图生图/首尾帧工作流_2076180255999619073.json, 视频生成/图生视频/53.tonnie-Smooth+FMLF 首尾多帧视频_2007957873501937666.json, 视频生成/图生视频/DaSiWaWan-V10-动漫首尾多帧视频生成_2043159910917087233.json, 视频生成/图生视频/DaSiWaWan2.2-动漫多帧视频生成_2007811222472761345.json, 视频生成/图生视频/Remix-V2.1-首尾多帧视频生成_2011657248396808193.json, 视频生成/图生视频/Remix-V3.0-首尾多帧视频生成_2033890243190984706.json, 视频生成/图生视频/Smooth+FMLF 首尾多帧视频_1988615220765614082.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2010685472720293889.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2022695348518522881.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2059832130892550145.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2063803655928766465.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2069687401794064385.json, 视频生成/图生视频/Wan2.2 Remix2 图生视频创作版_2019298877509210114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/万相图生视频_1953415257853186050.json、图片生成/图生图/首尾帧工作流_2076180255999619073.json、视频生成/图生视频/53.tonnie-Smooth+FMLF 首尾多帧视频_2007957873501937666.json、视频生成/图生视频/DaSiWaWan-V10-动漫首尾多帧视频生成_2043159910917087233.json、视频生成/图生视频/DaSiWaWan2.2-动漫多帧视频生成_2007811222472761345.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 13/14 个有
- `ImageResizeKJv2` —— 13/14 个有
- `SimpleMath+` —— 13/14 个有
- `WanFirstMiddleLastFrameToVideo` —— 12/14 个有
- `ModelPatchTorchSettings` —— 11/14 个有
- `LoraLoaderModelOnly` —— 9/14 个有
- `YC Color Match` —— 3/14 个有
- `CR Text` —— 2/14 个有
- `WanImageToVideo` —— 2/14 个有
- `ComfyMathExpression` —— 1/14 个有
- `DF_Int_to_Float` —— 1/14 个有
- `ImpactInt` —— 1/14 个有
- `ImpactSwitch` —— 1/14 个有
- `JWInteger` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 86% |
| Prompt 约束强度(CFG) | 6 | 4 - 35 | 14 | 9% |
| 采样算法 | 1 | 1 - 7.5 | 14 | 0% |
| 调度器 | euler | - | 14 | 100% |
| 重绘幅度 | simple | - | 14 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 35，14 个样本，取值分散，一致性仅 9%
- 采样算法 中位数 1，观测区间 1 - 7.5，14 个样本，取值分散，一致性仅 0%
- 调度器 最常用 euler，14 个样本，一致性 100%
- 重绘幅度 最常用 simple，14 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 35，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
