---
name: unknown_workflow_video_lora_sampler_185
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.820846
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/视频-Wan2.2首中尾帧FMLF，首中尾三帧参考_2068809925526118401.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2053500201926705153.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2054607136101027841.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063711056727461890.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063712287315292162.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063714093613281281.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063914082952114178.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2072973666828251138.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2048315037026099202.json, 视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2078764896707244034.json, 视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2087965953232556033.json, 视频生成/图生视频/首尾祯动感转场_1994048317403447297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_185

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/视频-Wan2.2首中尾帧FMLF，首中尾三帧参考_2068809925526118401.json、视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2053500201926705153.json、视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2054607136101027841.json、视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063711056727461890.json、视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063712287315292162.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `WanFirstMiddleLastFrameToVideo` —— 12/13 个有
- `ModelPatchTorchSettings` —— 11/13 个有
- `SimpleMath+` —— 11/13 个有
- `CFGZeroStar` —— 2/13 个有
- `CLIPVisionEncode` —— 2/13 个有
- `CLIPVisionLoader` —— 2/13 个有
- `WanVideoNAG` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `CM_IntToFloat` —— 1/13 个有
- `CR Seed` —— 1/13 个有
- `ComfyMathExpression` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `WanFirstLastFrameToVideo` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 13 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 13 | 91% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | euler | - | 13 | 92% |
| 重绘幅度 | beta | - | 13 | 69% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，13 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，13 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，13 个样本，一致性 92%
- 重绘幅度 最常用 beta，13 个样本，一致性 69%
