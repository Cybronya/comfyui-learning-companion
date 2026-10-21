---
name: unknown_workflow_video_clip_unet_6
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.495667
common_nodes: [Bookmark (rgthree), CLIPLoader, CLIPTextEncode, GetNode, LoadImage, ModelSamplingSD3, PrimitiveString, PrimitiveStringMultiline, SetNode, StringConcatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy int, easy seed]
problems: []
missing: [Bookmark (rgthree), Label (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), easy int, easy seed]
members: [视频生成/图生视频/1950129189842280449.json, 视频生成/图生视频/1950129708211027969.json, 视频生成/图生视频/1950329172787904513.json, 视频生成/图生视频/1954176509042946049.json, 视频生成/文生视频/1950129708211027969.json, 视频生成/文生视频/1950329172787904513.json, 视频生成/文生视频/1954176509042946049.json, "视频生成/文生视频/smoothMixWan图生视频，首尾帧生视频，文生视频,效果好速度快_1985642136488091650.json", 视频生成/文生视频/smoothMixWan生视频官方版本_全功能_1980313348170539010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1950129189842280449.json、视频生成/图生视频/1950129708211027969.json、视频生成/图生视频/1950329172787904513.json、视频生成/图生视频/1954176509042946049.json、视频生成/文生视频/1950129708211027969.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 9 个 workflow 都包含：
- `Bookmark (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `SetNode`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 8/9 个有
- `EmptyHunyuanLatentVideo` —— 8/9 个有
- `KSamplerAdvanced` —— 8/9 个有
- `Label (rgthree)` —— 8/9 个有
- `Mute / Bypass Relay (rgthree)` —— 8/9 个有
- `Mute / Bypass Repeater (rgthree)` —— 8/9 个有
- `PathchSageAttentionKJ` —— 8/9 个有
- `WanImageToVideo` —— 8/9 个有
- `Fast Groups Muter (rgthree)` —— 4/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `VAEDecodeTiled` —— 4/9 个有
- `WanFirstLastFrameToVideo` —— 4/9 个有
- `ModelPatchTorchSettings` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `PrimitiveFloat` —— 2/9 个有
- `RH_LLMAPI_NODE` —— 2/9 个有
- `TorchCompileModelWanVideoV2` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `wanBlockSwap` —— 2/9 个有
- `KSampler` —— 1/9 个有
- `Wan22ImageToVideoLatent` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 67% |
| Prompt 约束强度(CFG) | 9 | 5 - 20 | 9 | 49% |
| 采样算法 | 3.5 | 1 - 3.5 | 8 | 62% |
| 调度器 | euler | - | 9 | 89% |
| 重绘幅度 | simple | - | 9 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 9，观测区间 5 - 20，9 个样本，取值分散，一致性仅 49%
- 采样算法 中位数 3.5，观测区间 1 - 3.5，8 个样本
- 调度器 最常用 euler，9 个样本，一致性 89%
- 重绘幅度 最常用 simple，9 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：Bookmark (rgthree)、Label (rgthree)、Mute / Bypass Relay (rgthree)、Mute / Bypass Repeater (rgthree)、easy int
