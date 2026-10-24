---
name: unknown_workflow_video_sampler_clip_96
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.593429
common_nodes: [Any Switch (rgthree), Bookmark (rgthree), CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetNode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveString, PrimitiveStringMultiline, SetNode, StringConcatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy int, easy seed]
problems: []
missing: []
members: ["视频生成/文生视频/smoothMixWan图生视频，首尾帧生视频，文生视频,效果好速度快_1985642136488091650.json", 视频生成/文生视频/smoothMixWan生视频官方版本_全功能_1980313348170539010.json, 视频生成/文生视频/wan2.2_14B_文生图生视频_lightX加速版_1950129708211027969.json, 视频生成/文生视频/wan2.2_14B_文生图生视频原版+sage加速_1950329172787904513.json, 视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051901085580840962.json, 视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051927696871051266.json, 视频生成/文生视频/wan2.2_14B官方版本_全功能_1954176509042946049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_96

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/smoothMixWan图生视频，首尾帧生视频，文生视频,效果好速度快_1985642136488091650.json、视频生成/文生视频/smoothMixWan生视频官方版本_全功能_1980313348170539010.json、视频生成/文生视频/wan2.2_14B_文生图生视频_lightX加速版_1950129708211027969.json、视频生成/文生视频/wan2.2_14B_文生图生视频原版+sage加速_1950329172787904513.json、视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051901085580840962.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bookmark (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `SetNode`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 6/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `Fast Groups Muter (rgthree)` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `VAEDecodeTiled` —— 3/7 个有
- `WanFirstLastFrameToVideo` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `1hew_AnySwitchSelect` —— 2/7 个有
- `Int` —— 2/7 个有
- `ModelPatchTorchSettings` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `TT_img_enc_v2` —— 2/7 个有
- `text_mul_Join` —— 2/7 个有
- `wanBlockSwap` —— 2/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `TorchCompileModelWanVideoV2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 86% |
| Prompt 约束强度(CFG) | 10 | 6 - 20 | 7 | 52% |
| 采样算法 | 3.5 | 1 - 3.5 | 7 | 59% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 10，观测区间 6 - 20，7 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，7 个样本
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 71%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
