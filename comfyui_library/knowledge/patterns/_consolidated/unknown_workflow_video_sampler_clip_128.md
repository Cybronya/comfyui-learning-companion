---
name: unknown_workflow_video_sampler_clip_128
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.948
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Bypasser (rgthree), ImageScaleBy, ImpactInt, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveStringMultiline, RIFE VFI, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 Remix-高动态电影质感模型 图生视频_1988090119234236418.json, 视频生成/图生视频/wan2.2 Smooth Mix V2高动态电影质感 图生视频_2013454725135470593.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1980432616040148994.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1983880606536925186.json, 视频生成/图生视频/双图--首尾帧图生视频【2025-11-13】_2010579095784001537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/wan2.2 Remix-高动态电影质感模型 图生视频_1988090119234236418.json、视频生成/图生视频/wan2.2 Smooth Mix V2高动态电影质感 图生视频_2013454725135470593.json、视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1980432616040148994.json、视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1983880606536925186.json、视频生成/图生视频/双图--首尾帧图生视频【2025-11-13】_2010579095784001537.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Fast Bypasser (rgthree)`
- `ImageScaleBy`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `WanImageToVideo` —— 4/5 个有
- `AILab_QwenVL` —— 2/5 个有
- `GetImageSize+` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PurgeVRAM_UTK` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `Text Concatenate` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有
- `Wan22PromptSelector` —— 1/5 个有
- `WanFirstLastFrameToVideo` —— 1/5 个有
- `easy imageScaleDownToSize` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `ttN text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 80%
