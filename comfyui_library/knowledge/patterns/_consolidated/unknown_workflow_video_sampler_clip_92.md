---
name: unknown_workflow_video_sampler_clip_92
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.688714
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/AI代码侠土豆-WAN2.2-LightX2V-I2V_1981260473284943874.json, 视频生成/图生视频/AI代码侠土豆-Wan2.2_SmoothMix_I2V（图生视频）电影级动效_1980195972468871170.json, 视频生成/图生视频/Wan2.2_Smooth 图生视频超级快_2012356718814040065.json, 视频生成/图生视频/Wan2.2_Smooth 首尾帧_2012366284465377282.json, 视频生成/图生视频/Wan2.2_SmoothMix_I2V动作特效_2008338677897895938.json, 视频生成/图生视频/（图生视频）电影级动效_2050914662958542849.json, 视频生成/文生视频/影视级图生视频+文生视频Wan2.2-LightX2V-I2V高级动态+超真实光影_2002055798597533698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/AI代码侠土豆-WAN2.2-LightX2V-I2V_1981260473284943874.json、视频生成/图生视频/AI代码侠土豆-Wan2.2_SmoothMix_I2V（图生视频）电影级动效_1980195972468871170.json、视频生成/图生视频/Wan2.2_Smooth 图生视频超级快_2012356718814040065.json、视频生成/图生视频/Wan2.2_Smooth 首尾帧_2012366284465377282.json、视频生成/图生视频/Wan2.2_SmoothMix_I2V动作特效_2008338677897895938.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 6/7 个有
- `CLIPVisionEncode` —— 5/7 个有
- `CLIPVisionLoader` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `ImpactInt` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `RIFE VFI` —— 3/7 个有
- `DF_Integer` —— 2/7 个有
- `Int` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `Text` —— 1/7 个有
- `Textbox` —— 1/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 86% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 7 | 86% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | 1 | 1 - 1 | 7 | 100% |
| 重绘幅度 | euler_ancestral | - | 7 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，7 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，7 个样本，一致性 71%
