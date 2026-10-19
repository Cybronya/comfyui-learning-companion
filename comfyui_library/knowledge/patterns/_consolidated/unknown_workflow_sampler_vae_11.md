---
name: unknown_workflow_sampler_vae_11
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.854632
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [数字人/数字人/MiniMax H3 -首帧参考生视频 (1)_2084123367581507586.json, 数字人/数字人/MiniMax H3 FL2VA开源版-首帧参考生视频_2102269100943822850.json, 视频生成/图生视频/A-4 MiniMax-H3 图生视频 RH版 _ 首帧驱动_2085040525719195649.json, 视频生成/图生视频/MINI max首位帧工作流_2084157900280389634.json, 视频生成/图生视频/MiniMax H3 FL2VA-图生视频-口播10秒_2095680024237137922.json, 视频生成/图生视频/MiniMax H3 FL2VA-图生视频_2093100115979489282.json, 视频生成/图生视频/MiniMax H3 FL2VA_2084272351662927873.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 - 首尾帧参考生视频_2084449894806409218.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-单图参考生视频_2084124320309272578.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-单图参考生视频_2084137001363787778.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-单图参考生视频_2084163168024223746.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-非API 首帧参考生视频_2084116326469169153.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧参考生视频_2084070256573767682.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧参考生视频_2084110735633903618.json, 视频生成/图生视频/首尾帧图生视频MiniMax+H3+FL2VA开源版-首尾帧参考生视频_2084125402418733057.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-首尾帧10秒视频_2084170874189598722.json, 视频生成/文生视频/MiniMax H3 开源版-首帧参考生视频_2084478495324987394.json, 视频生成/文生视频/MiniMax+H3+FL2VA开源版-首尾帧参考生视频_2084175487978524673.json, 视频生成/文生视频/MiniMax+H3+FL2VA开源版-首帧参考生视频_2084171293531922434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_11

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（数字人/数字人/MiniMax H3 -首帧参考生视频 (1)_2084123367581507586.json、数字人/数字人/MiniMax H3 FL2VA开源版-首帧参考生视频_2102269100943822850.json、视频生成/图生视频/A-4 MiniMax-H3 图生视频 RH版 _ 首帧驱动_2085040525719195649.json、视频生成/图生视频/MINI max首位帧工作流_2084157900280389634.json、视频生成/图生视频/MiniMax H3 FL2VA-图生视频-口播10秒_2095680024237137922.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 19 个 workflow 都包含：
- `CreateVideo`
- `LoadImage`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAFirstFrameCondition`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `Int` —— 16/19 个有
- `ImageResize+` —— 14/19 个有
- `ImpactSwitch` —— 14/19 个有
- `PreviewImage` —— 13/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/19 个有
- `Text` —— 3/19 个有
- `easy convertAnything` —— 3/19 个有
- `孤海注释` —— 3/19 个有
- `Reroute (rgthree)` —— 1/19 个有
- `ResizeImagesByLongerEdge` —— 1/19 个有
- `ZNGB_ResizeImage` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
